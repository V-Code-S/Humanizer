"""
Humanization routes.
Handles text humanization requests.
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
import logging

from app.services.paraphraser import ParaphraseModel
from app.services.humanizer import HumanizationEngine
from app.services.grammar import GrammarCorrector
from app.utils.text_processing import TextProcessor

# Setup logger
logger = logging.getLogger(__name__)

router = APIRouter()

# Pydantic models
class HumanizeRequest(BaseModel):
    """Request model for humanization"""
    text: str = Field(..., min_length=10, max_length=5000, description="Text to humanize")
    style: Optional[str] = Field(default="default", description="Writing style: casual, professional, academic, blog")

class HumanizeResponse(BaseModel):
    """Response model for humanization"""
    original_text: str
    humanized_text: str
    style: str
    processing_time: float

class BulkHumanizeRequest(BaseModel):
    """Request model for bulk humanization"""
    texts: list[str] = Field(..., max_items=10, description="List of texts to humanize")
    style: Optional[str] = Field(default="default")

class BulkHumanizeResponse(BaseModel):
    """Response model for bulk humanization"""
    results: list[dict]
    total_time: float

# Endpoints
@router.post("/humanize", response_model=HumanizeResponse, summary="Humanize text")
async def humanize_text(request: HumanizeRequest):
    """
    Transform AI-generated text into natural, human-like writing.
    
    Args:
        text: The text to humanize
        style: Writing style (casual, professional, academic, blog)
    
    Returns:
        Humanized text with metadata
    """
    try:
        import time
        start_time = time.time()
        
        # Validate and clean input
        text = request.text.strip()
        if not text:
            raise HTTPException(status_code=400, detail="Text cannot be empty")
        
        if len(text) < 10:
            raise HTTPException(status_code=400, detail="Text is too short (minimum 10 characters)")
        
        if len(text) > 5000:
            raise HTTPException(status_code=400, detail="Text is too long (maximum 5000 characters)")
        
        # Process text
        logger.info(f"Processing text with style: {request.style}")
        
        # Get services
        paraphraser = ParaphraseModel.get_instance()
        humanizer = HumanizationEngine.get_instance()
        
        # Step 1: Paraphrase
        paraphrased = paraphraser.paraphrase(text)
        logger.debug(f"Paraphrased: {paraphrased[:50]}...")
        
        # Step 2: Humanize
        humanized = humanizer.humanize(paraphrased, style=request.style)
        logger.debug(f"Humanized: {humanized[:50]}...")
        
        # Step 3: Grammar correction
        grammar_corrector = GrammarCorrector()
        final_text = grammar_corrector.correct(humanized)
        
        processing_time = time.time() - start_time
        
        return HumanizeResponse(
            original_text=text,
            humanized_text=final_text,
            style=request.style or "default",
            processing_time=round(processing_time, 2)
        )
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error in humanize_text: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Error processing text: {str(e)}")

@router.post("/humanize/bulk", response_model=BulkHumanizeResponse, summary="Bulk humanize texts")
async def bulk_humanize(request: BulkHumanizeRequest):
    """
    Humanize multiple texts at once.
    
    Args:
        texts: List of texts to humanize (max 10)
        style: Writing style
    
    Returns:
        List of humanized texts with metadata
    """
    try:
        import time
        start_time = time.time()
        
        if not request.texts:
            raise HTTPException(status_code=400, detail="Texts list cannot be empty")
        
        if len(request.texts) > 10:
            raise HTTPException(status_code=400, detail="Maximum 10 texts per request")
        
        results = []
        paraphraser = ParaphraseModel.get_instance()
        humanizer = HumanizationEngine.get_instance()
        grammar_corrector = GrammarCorrector()
        
        for text in request.texts:
            text = text.strip()
            if not text or len(text) < 10:
                results.append({
                    "original": text,
                    "humanized": text,
                    "error": "Text too short"
                })
                continue
            
            try:
                paraphrased = paraphraser.paraphrase(text)
                humanized = humanizer.humanize(paraphrased, style=request.style)
                final = grammar_corrector.correct(humanized)
                
                results.append({
                    "original": text,
                    "humanized": final
                })
            except Exception as e:
                logger.error(f"Error processing individual text: {str(e)}")
                results.append({
                    "original": text,
                    "humanized": text,
                    "error": str(e)
                })
        
        total_time = time.time() - start_time
        
        return BulkHumanizeResponse(
            results=results,
            total_time=round(total_time, 2)
        )
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error in bulk_humanize: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Error processing texts: {str(e)}")

@router.get("/styles", summary="Get available styles")
async def get_styles():
    """Get list of available writing styles"""
    styles = {
        "default": "Natural, balanced writing style",
        "casual": "Conversational and informal tone",
        "professional": "Formal and business-like tone",
        "academic": "Scholarly and detailed writing",
        "blog": "Engaging and narrative style"
    }
    return {"styles": styles}

@router.post("/analyze", summary="Analyze text humanization metrics")
async def analyze_text(request: HumanizeRequest):
    """
    Analyze text metrics before and after humanization.
    
    Returns:
        Metrics comparing original and humanized text
    """
    try:
        from app.utils.text_processing import TextProcessor
        
        text = request.text.strip()
        if not text:
            raise HTTPException(status_code=400, detail="Text cannot be empty")
        
        paraphraser = ParaphraseModel.get_instance()
        humanizer = HumanizationEngine.get_instance()
        grammar_corrector = GrammarCorrector()
        
        paraphrased = paraphraser.paraphrase(text)
        humanized = humanizer.humanize(paraphrased, style=request.style)
        final_text = grammar_corrector.correct(humanized)
        
        original_metrics = TextProcessor.get_text_metrics(text)
        humanized_metrics = TextProcessor.get_text_metrics(final_text)
        
        return {
            "original": {
                "text": text,
                "metrics": original_metrics
            },
            "humanized": {
                "text": final_text,
                "metrics": humanized_metrics
            },
            "improvements": {
                "sentence_variation_increase": humanized_metrics.get("avg_sentence_length") - original_metrics.get("avg_sentence_length"),
                "readability_score": "improved" if humanized_metrics.get("unique_words") > original_metrics.get("unique_words") else "similar"
            }
        }
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error in analyze_text: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Error analyzing text: {str(e)}")
