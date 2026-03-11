import spacy
import unicodedata
from typing import List

class NLPEngine:
    """
    Motor de Procesamiento de Lenguaje Natural (NLP).
    """
    
    def __init__(self):
        print("[NLPEngine] Cargando modelo de lenguaje en español...")
        self.nlp = spacy.load("es_core_news_sm")
        print("[NLPEngine] Modelo cargado exitosamente.")

    def _limpiar_tildes(self, texto: str) -> str:
        """Elimina las tildes de un texto para búsquedas exactas."""
        return ''.join((c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn'))

    def extract_keywords(self, text: str) -> List[str]:
        """
        Analiza el texto y devuelve una lista con las palabras clave (lemas) SIN TILDES.
        """
        doc = self.nlp(text.lower())
        keywords = []
        
        for token in doc:
            if not token.is_punct and not token.is_space and not token.is_stop:
                # Extraemos el lema
                lema = token.lemma_.lower()
                # Le quitamos las tildes
                lema_limpio = self._limpiar_tildes(lema)
                keywords.append(lema_limpio)
                
        return keywords