"""
Text processing utilities.
Handles sentence segmentation, metrics, and text analysis.
"""
import logging
import re
from typing import List, Dict
from collections import Counter

try:
    import nltk
    from nltk.tokenize import sent_tokenize, word_tokenize
    from nltk.corpus import stopwords

    HAS_NLTK = True
except ImportError:
    HAS_NLTK = False

logger = logging.getLogger(__name__)

class TextProcessor:
    """Utility class for text processing operations"""

    @staticmethod
    def _has_nltk_resource(resource_path: str) -> bool:
        """Check whether an NLTK resource is available locally."""
        if not HAS_NLTK:
            return False

        try:
            nltk.data.find(resource_path)
            return True
        except LookupError:
            logger.warning("NLTK resource missing: %s. Using lightweight fallback.", resource_path)
            return False
    
    @staticmethod
    def segment_sentences(text: str) -> List[str]:
        """
        Split text into sentences.
        
        Args:
            text: Input text
        
        Returns:
            List of sentences
        """
        if not text:
            return []
        
        try:
            if HAS_NLTK and TextProcessor._has_nltk_resource('tokenizers/punkt'):
                return sent_tokenize(text)
            else:
                # Fallback to simple regex splitting
                sentences = re.split(r'(?<=[.!?])\s+', text)
                return [s.strip() for s in sentences if s.strip()]
        except Exception as e:
            logger.error(f"Error segmenting sentences: {str(e)}")
            return [text]
    
    @staticmethod
    def tokenize_words(text: str) -> List[str]:
        """
        Split text into words.
        
        Args:
            text: Input text
        
        Returns:
            List of words
        """
        if not text:
            return []
        
        try:
            if HAS_NLTK and TextProcessor._has_nltk_resource('tokenizers/punkt'):
                return word_tokenize(text)
            else:
                # Fallback to simple regex tokenization
                words = re.findall(r'\b\w+\b', text.lower())
                return words
        except Exception as e:
            logger.error(f"Error tokenizing words: {str(e)}")
            return text.split()
    
    @staticmethod
    def get_text_metrics(text: str) -> Dict:
        """
        Calculate various metrics about the text.
        
        Args:
            text: Input text
        
        Returns:
            Dictionary with text metrics
        """
        try:
            sentences = TextProcessor.segment_sentences(text)
            words = TextProcessor.tokenize_words(text)
            
            # Basic metrics
            word_count = len(words)
            sentence_count = len(sentences)
            char_count = len(text)
            
            # Advanced metrics
            unique_words = len(set(word.lower() for word in words))
            avg_sentence_length = word_count / sentence_count if sentence_count > 0 else 0
            avg_word_length = char_count / word_count if word_count > 0 else 0
            
            # Readability metrics
            reading_time = max(1, word_count // 200)  # Assuming 200 words per minute
            
            # Burstiness (sentence length variation)
            sentence_lengths = [len(TextProcessor.tokenize_words(sent)) for sent in sentences]
            burstiness = max(sentence_lengths) - min(sentence_lengths) if sentence_lengths else 0
            
            # Stopword ratio
            if HAS_NLTK and TextProcessor._has_nltk_resource('corpora/stopwords'):
                try:
                    stop_words = set(stopwords.words('english'))
                    stopword_count = sum(1 for word in words if word.lower() in stop_words)
                    stopword_ratio = stopword_count / word_count if word_count > 0 else 0
                except Exception:
                    stopword_ratio = 0
            else:
                stopword_ratio = 0
            
            return {
                "word_count": word_count,
                "sentence_count": sentence_count,
                "character_count": char_count,
                "unique_words": unique_words,
                "avg_sentence_length": round(avg_sentence_length, 2),
                "avg_word_length": round(avg_word_length, 2),
                "reading_time_minutes": reading_time,
                "sentence_burstiness": burstiness,
                "stopword_ratio": round(stopword_ratio, 3) if stopword_ratio else 0,
                "lexical_diversity": round(unique_words / word_count, 3) if word_count > 0 else 0,
            }
        
        except Exception as e:
            logger.error(f"Error calculating text metrics: {str(e)}")
            return {}
    
    @staticmethod
    def detect_ai_pattern(text: str) -> Dict:
        """
        Detect common AI-generated text patterns.
        
        Args:
            text: Input text to analyze
        
        Returns:
            Dictionary with detected patterns and scores
        """
        patterns = {
            "repetition": r'\b(\w+)\s+\1\b',
            "passive_voice": r'\b(is|was|be|been|being)\s+\w+ed\b',
            "complex_intro": r'(In light of|In the context of|It is important to note)',
            "list_structure": r'(First|Second|Third|Finally)',
            "robotic_connectors": r'(Furthermore|Moreover|In conclusion|To summarize)',
            "generic_phrases": r'(It is clear that|It can be seen that|It is well known)',
        }
        
        detected_patterns = {}
        
        for pattern_name, pattern in patterns.items():
            matches = re.findall(pattern, text, re.IGNORECASE)
            detected_patterns[pattern_name] = len(matches)
        
        # Calculate AI score (0-100)
        total_patterns = sum(detected_patterns.values())
        ai_score = min(100, (total_patterns / len(text.split()) * 100)) if text.split() else 0
        
        return {
            "detected_patterns": detected_patterns,
            "ai_score": round(ai_score, 2),
            "is_likely_ai": ai_score > 30,
        }
    
    @staticmethod
    def clean_text(text: str) -> str:
        """
        Clean and normalize text.
        
        Args:
            text: Text to clean
        
        Returns:
            Cleaned text
        """
        if not text:
            return text
        
        # Remove extra whitespace
        text = ' '.join(text.split())
        
        # Remove special characters but keep punctuation
        text = re.sub(r'[^\w\s.,!?;:\'\"-]', '', text)
        
        # Normalize quotes
        text = text.replace('"', '"').replace('"', '"')
        
        return text.strip()
