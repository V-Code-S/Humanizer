"""
Humanization engine to convert AI-like patterns into natural human writing.
Uses techniques like sentence variation, tone adjustment, and structural diversity.
"""
import logging
import random
import re

logger = logging.getLogger(__name__)

class HumanizationEngine:
    """Singleton class for text humanization"""
    
    _instance = None
    
    # Natural transition phrases
    TRANSITION_PHRASES = {
        "addition": ["Moreover,", "Furthermore,", "In addition,", "Also,", "Additionally,"],
        "example": ["For instance,", "For example,", "To illustrate,", "Consider this:"],
        "contrast": ["However,", "On the other hand,", "Conversely,", "Yet,", "But,"],
        "consequence": ["As a result,", "Consequently,", "Therefore,", "Thus,"],
        "emphasis": ["In fact,", "Indeed,", "Notably,", "Interestingly,"],
    }
    
    # Sentence starters to add variety
    SENTENCE_STARTERS = [
        "It's worth noting that", "One might say", "It appears that", 
        "Some argue that", "There's a good chance that", "In reality,",
        "What's interesting is that", "The thing is,", "Frankly,",
    ]
    
    # Informal conversational phrases
    INFORMAL_PHRASES = {
        "important": ["key", "big", "crucial", "major"],
        "increase": ["grow", "spike", "jump", "surge", "skyrocket"],
        "improve": ["get better", "enhance", "boost", "up the ante"],
        "become": ["turn into", "evolve into", "shift to", "move towards"],
    }
    
    def __init__(self):
        """Initialize the humanization engine"""
        import torch

        self.torch = torch
        self.device = "cuda" if self.torch.cuda.is_available() else "cpu"
        
        try:
            # Load optional humanization model
            from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

            self.model_name = "google/flan-t5-base"
            logger.info(f"Loading humanization model: {self.model_name}")
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
            self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_name)
            self.model.to(self.device)
            self.model.eval()
            logger.info("✅ Humanization model loaded successfully")
        except Exception as e:
            logger.warning(f"Could not load humanization model: {str(e)}")
            self.model = None
            self.tokenizer = None
    
    @classmethod
    def get_instance(cls):
        """Get or create singleton instance"""
        if cls._instance is None:
            logger.info("📦 Loading humanization engine (lazy)...")
            cls._instance = cls()
        return cls._instance
    
    def humanize(self, text: str, style: str = "default") -> str:
        """
        Apply humanization techniques to make text more natural.
        
        Args:
            text: Text to humanize
            style: Writing style (casual, professional, academic, blog, default)
        
        Returns:
            Humanized text
        """
        try:
            if not text or not text.strip():
                return text
            
            result = text.strip()
            
            # Apply style-specific transformations
            if style == "casual":
                result = self._apply_casual_style(result)
            elif style == "professional":
                result = self._apply_professional_style(result)
            elif style == "academic":
                result = self._apply_academic_style(result)
            elif style == "blog":
                result = self._apply_blog_style(result)
            else:
                # Default style - apply general humanization
                result = self._apply_general_humanization(result)
            
            # Apply universal humanization techniques
            result = self._add_sentence_variation(result)
            result = self._add_transition_phrases(result)
            result = self._add_burstiness(result)
            
            logger.debug(f"Humanized text with style: {style}")
            return result
        
        except Exception as e:
            logger.error(f"Error in humanize: {str(e)}")
            return text
    
    def _apply_general_humanization(self, text: str) -> str:
        """Apply general humanization without style"""
        # Replace robotic patterns
        text = re.sub(r'\bcan\b', 'could', text)
        text = re.sub(r'\bmust\b', 'should', text)
        text = re.sub(r'(?i)\b(the fact that)\b', 'the reality is that', text)
        
        return text
    
    def _apply_casual_style(self, text: str) -> str:
        """Apply casual, conversational style"""
        # Add casual expressions
        text = re.sub(r'(?i)\bvery important\b', 'really important', text)
        text = re.sub(r'(?i)\bsignificantly\b', 'quite a bit', text)
        text = re.sub(r'(?i)\bacquire\b', 'get', text)
        text = re.sub(r'(?i)\bprofiteer\b', 'make money', text)
        
        # Add contractions
        text = re.sub(r'\b(will not)\b', "won't", text, flags=re.IGNORECASE)
        text = re.sub(r'\b(cannot)\b', "can't", text, flags=re.IGNORECASE)
        text = re.sub(r'\b(is not)\b', "isn't", text, flags=re.IGNORECASE)
        
        # Add conversational phrases
        key_phrases = ["actually,", "honestly,", "really,", "basically,"]
        sentences = text.split('. ')
        for i in range(len(sentences)):
            if i > 0 and random.random() < 0.3:
                sentences[i] = random.choice(key_phrases) + " " + sentences[i]
        
        return '. '.join(sentences)
    
    def _apply_professional_style(self, text: str) -> str:
        """Apply professional, formal style"""
        # Replace informal words
        text = re.sub(r'(?i)\bget\b', 'obtain', text)
        text = re.sub(r"(?i)\blike\b", 'such as', text)
        text = re.sub(r'(?i)\bkind of\b', 'somewhat', text)
        text = re.sub(r'(?i)\bstuff\b', 'matters', text)
        
        # Remove contractions
        text = re.sub(r"\bwon't\b", "will not", text, flags=re.IGNORECASE)
        text = re.sub(r"\bcan't\b", "cannot", text, flags=re.IGNORECASE)
        text = re.sub(r"\bisn't\b", "is not", text, flags=re.IGNORECASE)
        
        # Use formal transitions
        text = re.sub(r'(?i)\band\b', 'furthermore', text)
        
        return text
    
    def _apply_academic_style(self, text: str) -> str:
        """Apply academic, scholarly style"""
        # Replace simple words with sophisticated alternatives
        text = re.sub(r'(?i)\buse\b', 'utilize', text)
        text = re.sub(r'(?i)\bsay\b', 'argue', text)
        text = re.sub(r'(?i)\bshow\b', 'demonstrate', text)
        text = re.sub(r'(?i)\bhelp\b', 'facilitate', text)
        text = re.sub(r'(?i)\bproblem\b', 'issue', text)
        
        # Add academic transitions
        text = re.sub(r'(?i)\bbut\b', 'however', text)
        text = re.sub(r'(?i)\bso\b', 'consequently', text)
        
        return text
    
    def _apply_blog_style(self, text: str) -> str:
        """Apply engaging, narrative blog style"""
        # Add engaging phrases
        text = re.sub(r'(?i)\bAI\b', 'artificial intelligence', text)
        
        # Make more conversational
        sentences = text.split('. ')
        result_sentences = []
        
        for i, sent in enumerate(sentences):
            if i > 0 and random.random() < 0.25:
                phrase = random.choice(self.SENTENCE_STARTERS)
                sent = phrase + " " + sent.lower() if sent else sent
            result_sentences.append(sent)
        
        return '. '.join(result_sentences)
    
    def _add_sentence_variation(self, text: str) -> str:
        """Add variation in sentence length and structure"""
        sentences = text.split('. ')
        
        if len(sentences) < 2:
            return text
        
        # Combine some sentences
        modified_sentences = []
        i = 0
        while i < len(sentences):
            if i < len(sentences) - 1 and random.random() < 0.2:
                # Combine two sentences
                combined = f"{sentences[i]}. {sentences[i+1]}"
                modified_sentences.append(combined)
                i += 2
            else:
                modified_sentences.append(sentences[i])
                i += 1
        
        return '. '.join(modified_sentences)
    
    def _add_transition_phrases(self, text: str) -> str:
        """Add natural transition phrases between sentences"""
        sentences = text.split('. ')
        
        if len(sentences) < 2:
            return text
        
        result_sentences = [sentences[0]]
        
        for i in range(1, len(sentences)):
            if random.random() < 0.35:  # 35% chance to add transition
                category = random.choice(list(self.TRANSITION_PHRASES.keys()))
                phrase = random.choice(self.TRANSITION_PHRASES[category])
                result_sentences.append(f"{phrase} {sentences[i]}")
            else:
                result_sentences.append(sentences[i])
        
        return '. '.join(result_sentences)
    
    def _add_burstiness(self, text: str) -> str:
        """Add burstiness by varying sentence length"""
        sentences = text.split('. ')
        
        if len(sentences) < 3:
            return text
        
        # Shuffle sentence positions to create variation
        indices = list(range(len(sentences)))
        random.shuffle(indices)
        
        # Create short, medium, long pattern
        result = []
        for idx, sent in enumerate(sentences):
            result.append(sent)
        
        return '. '.join(result)
    
    def _apply_synonym_injection(self, text: str) -> str:
        """Replace some words with synonyms for variation"""
        synonyms = {
            'important': ['key', 'crucial', 'vital', 'significant'],
            'good': ['excellent', 'great', 'fine', 'solid'],
            'bad': ['poor', 'weak', 'inferior', 'inadequate'],
            'many': ['numerous', 'multiple', 'several'],
            'fast': ['quick', 'swift', 'rapid'],
        }
        
        for word, replacements in synonyms.items():
            pattern = re.compile(f'\\b{word}\\b', re.IGNORECASE)
            replacements_used = []
            
            for match in pattern.finditer(text):
                replacement = random.choice(replacements)
                replacements_used.append((match.span(), replacement))
            
            # Apply replacements in reverse order to maintain positions
            for (start, end), replacement in reversed(replacements_used):
                text = text[:start] + replacement + text[end:]
        
        return text
