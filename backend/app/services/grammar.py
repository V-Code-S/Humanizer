"""
Grammar correction service.
Ensures text is grammatically correct and well-formatted.
"""
import logging
from typing import Optional
import re

logger = logging.getLogger(__name__)

class GrammarCorrector:
    """Grammar and spelling correction service"""
    
    def __init__(self):
        """Initialize grammar corrector"""
        try:
            import language_tool_python
            self.tool = language_tool_python.LanguageTool('en-US')
            logger.info("✅ Grammar corrector initialized")
        except ImportError:
            logger.warning("language_tool_python not installed, using basic correction only")
            self.tool = None
    
    def correct(self, text: str) -> str:
        """
        Apply grammar and basic corrections to text.
        
        Args:
            text: Text to correct
        
        Returns:
            Corrected text
        """
        try:
            if not text or not text.strip():
                return text
            
            corrected = text.strip()
            
            # Apply basic corrections
            corrected = self._fix_basic_issues(corrected)
            
            # Use language tool if available
            if self.tool:
                try:
                    matches = self.tool.check(corrected)
                    if matches:
                        corrected = language_tool_python.utils.correct(corrected, matches)
                except Exception as e:
                    logger.warning(f"LanguageTool correction failed: {str(e)}, using basic correction")
            
            return corrected
        
        except Exception as e:
            logger.error(f"Error in grammar correction: {str(e)}")
            return text
    
    def _fix_basic_issues(self, text: str) -> str:
        """Fix common grammar and formatting issues"""
        
        # Fix spacing around punctuation
        text = re.sub(r'\s+([.,!?;:])', r'\1', text)  # Space before punctuation
        text = re.sub(r'([.,!?;:])\s+', r'\1 ', text)
        
        # Fix multiple spaces
        text = re.sub(r'\s{2,}', ' ', text)
        
        # Fix capitalization after periods
        sentences = text.split('. ')
        corrected_sentences = []
        for sent in sentences:
            if sent.strip():
                # Capitalize first letter
                sent = sent.strip()
                if sent:
                    sent = sent[0].upper() + sent[1:] if len(sent) > 1 else sent.upper()
                corrected_sentences.append(sent)
        
        text = '. '.join(corrected_sentences)
        
        # Ensure text ends with proper punctuation
        if text and text[-1] not in '.!?':
            text += '.'
        
        # Fix common mistakes
        text = re.sub(r'\bi\b', 'I', text)  # Capitalize 'I'
        text = re.sub(r'\b(it\'s|its)\b', lambda m: "it's" if "I" in m.group() else "its", text)
        
        # Remove excessive punctuation
        text = re.sub(r'[!?\.]{2,}', '...', text)
        
        # Fix spacing with quotes
        text = re.sub(r'\s+"', '"', text)
        text = re.sub(r'"\s+', '"', text)
        
        return text
    
    def analyze_grammar(self, text: str) -> dict:
        """
        Analyze grammar issues in text.
        
        Args:
            text: Text to analyze
        
        Returns:
            Dictionary with grammar analysis
        """
        try:
            issues = []
            error_types = {}
            
            if self.tool:
                matches = self.tool.check(text)
                for match in matches:
                    issues.append({
                        "error": match.message,
                        "position": (match.offset, match.offset + match.length),
                        "suggestion": match.replacements[:3] if match.replacements else [],
                        "type": match.category
                    })
                    error_types[match.category] = error_types.get(match.category, 0) + 1
            
            return {
                "total_issues": len(issues),
                "issues": issues,
                "error_types": error_types,
                "text": text
            }
        
        except Exception as e:
            logger.error(f"Error in analyze_grammar: {str(e)}")
            return {
                "total_issues": 0,
                "issues": [],
                "error": str(e)
            }
