from typing import Dict, Any
from src.nlp_engine import NLPEngine
from src.rag_core import KnowledgeRetriever
# 1. IMPORTACIÓN: Traemos a nuestro nuevo redactor con IA
from src.llm_generator import LLMGenerator 

class HybridChatbot:
    """
    Orquestador principal. Ahora coordina el flujo RAG completo:
    1. NLP (Entiende) -> 2. Retriever (Busca) -> 3. LLM (Redacta con IA)
    """

    def __init__(self, name: str = "IngenieroBot"):
        self.name = name
        print(f"[{self.name}] Inicializando sistemas base...")
        
        self.nlp = NLPEngine()
        self.retriever = KnowledgeRetriever()
        
        # 2. INICIALIZACIÓN: Encendemos la conexión con Google Gemini
        # Esto leerá tu .env y preparará el modelo flash
        self.generator = LLMGenerator()

    def process_message(self, user_message: str) -> Dict[str, Any]:
        """Coordina el flujo RAG: Retrieval-Augmented Generation"""
        
        # Paso A: Entender (Extraer lemas con SpaCy)
        keywords = self.nlp.extract_keywords(user_message)

        # Paso B: Buscar (El Retriever busca coincidencias en el JSON)
        # best_answer aquí es el texto duro de la base de datos (ej: "Zapatos rojos a $85")
        best_answer, confidence_score = self.retriever.search_best_match(keywords)

        # Paso C: Generar (LA MAGIA DE LA IA)
        # Lógica: En lugar de devolver 'best_answer' crudo, se lo pasamos a Gemini
        # junto con lo que dijo el usuario, para que redacte algo natural.
        if confidence_score > 0:
            final_response = self.generator.generate_human_response(
                user_message=user_message,
                database_info=best_answer # Le pasamos los datos reales encontrados
            )
        else:
            # Lógica de Fallback: Si el JSON no tiene la respuesta, le decimos a Gemini
            # que improvise una disculpa basándose en la falta de datos.
            final_response = self.generator.generate_human_response(
                user_message=user_message,
                database_info="No se encontró información en la base de datos sobre esto."
            )

        # Retornamos el paquete armado al servidor web
        return {
            "bot_name": self.name,
            "original_message": user_message,
            "keywords_extracted": keywords,
            "confidence_score": confidence_score,
            "response": final_response, # ¡Ahora esta es la respuesta redactada por Gemini!
            "status": "success"
        }