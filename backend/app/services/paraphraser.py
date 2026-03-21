"""
Paraphrasing service using HuggingFace Transformers.
Uses T5-based paraphrasing model.
"""
import logging

logger = logging.getLogger(__name__)

class ParaphraseModel:
    """Singleton class for paraphrasing operations"""
    
    _instance = None
    
    def __init__(self):
        """Initialize the paraphrase model"""
        import torch
        from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

        self.torch = torch
        self.model_name = "Vamsi/T5_Paraphrase_Paws"
        self.device = "cuda" if self.torch.cuda.is_available() else "cpu"
        
        logger.info(f"Loading paraphrase model: {self.model_name} on {self.device}")
        
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
            self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_name)
            self.model.to(self.device)
            self.model.eval()
            logger.info("✅ Paraphrase model loaded successfully")
        except Exception as e:
            logger.error(f"Error loading paraphrase model: {str(e)}")
            raise
    
    @classmethod
    def get_instance(cls):
        """Get or create singleton instance"""
        if cls._instance is None:
            logger.info("📦 Loading paraphrase model (lazy)...")
            cls._instance = cls()
        return cls._instance
    
    def paraphrase(self, text: str, num_beams: int = 5, max_length: int = 512) -> str:
        """
        Paraphrase input text using T5 model.
        
        Args:
            text: Text to paraphrase
            num_beams: Number of beams for beam search
            max_length: Maximum length of generated text
        
        Returns:
            Paraphrased text
        """
        try:
            if not text or not text.strip():
                return text
            
            # Prepare input
            input_text = f"paraphrase: {text.strip()}"
            
            # Tokenize
            inputs = self.tokenizer.encode(
                input_text,
                return_tensors="pt",
                max_length=max_length,
                truncation=True
            ).to(self.device)
            
            # Generate paraphrase
            with self.torch.no_grad():
                outputs = self.model.generate(
                    inputs,
                    max_length=max_length,
                    num_beams=num_beams,
                    temperature=1.5,
                    top_p=0.95,
                    do_sample=True,
                    early_stopping=True,
                    num_return_sequences=1
                )
            
            # Decode
            paraphrase = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            
            logger.debug(f"Paraphrased: {text[:50]}... -> {paraphrase[:50]}...")
            
            return paraphrase if paraphrase else text
        
        except Exception as e:
            logger.error(f"Error in paraphrase: {str(e)}")
            return text  # Return original if paraphrasing fails
    
    def paraphrase_batch(self, texts: list, **kwargs) -> list:
        """
        Paraphrase multiple texts.
        
        Args:
            texts: List of texts to paraphrase
            **kwargs: Additional arguments for paraphrase()
        
        Returns:
            List of paraphrased texts
        """
        return [self.paraphrase(text, **kwargs) for text in texts]
