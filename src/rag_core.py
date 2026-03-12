import json
import os
from typing import List, Dict, Tuple
import unicodedata # Añade esto al inicio del archivo si no está

class KnowledgeRetriever:
    """
    Motor de Búsqueda (Retrieval).
    Se encarga de buscar en nuestra base de conocimientos la mejor respuesta
    basada en las palabras clave extraídas por el motor NLP.
    """
    
    def __init__(self, knowledge_file: str = "data/knowledge_base.json"):
        self.knowledge_file = knowledge_file
        # Al inicializar, cargamos el JSON en memoria una sola vez
        self.knowledge_base = self._load_knowledge()

    def _load_knowledge(self) -> Dict:
        """Método privado para leer el archivo JSON."""
        if not os.path.exists(self.knowledge_file):
            print(f"[Error] No se encontró el archivo: {self.knowledge_file}")
            return {}
        
        with open(self.knowledge_file, 'r', encoding='utf-8') as file:
            print("[KnowledgeRetriever] Base de conocimientos cargada.")
            return json.load(file)

    def search_best_match(self, user_keywords: List[str]) -> Tuple[str, float]:
       
        
        def limpiar_tildes(texto):
            return ''.join((c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn'))

        if not user_keywords or not self.knowledge_base:
            return "No entendí tu pregunta o no tengo información.", 0.0

        user_set = set(user_keywords)
        best_response = "Lo siento, aún no tengo información sobre ese tema específico."
        max_score = 0.0

        for category, items in self.knowledge_base.items():
            for item in items:
                # Limpiamos las tildes de las etiquetas del JSON para que coincidan con SpaCy
                etiquetas_limpias = [limpiar_tildes(etiqueta.lower()) for etiqueta in item["etiquetas"]]
                item_set = set(etiquetas_limpias)
                
                common_words = user_set.intersection(item_set)
                score = len(common_words)

                if score > max_score:
                    max_score = score
                    best_response = item["respuesta"]

        return best_response, float(max_score)