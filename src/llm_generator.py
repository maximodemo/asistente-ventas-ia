import os
import google.generativeai as genai
from dotenv import load_dotenv

# Cargamos al principio por si acaso, pero fuera de la clase
load_dotenv()

class LLMGenerator:
    def __init__(self):
        print("[LLMGenerator] Conectando con Gemini 1.5 Flash...")
        
        # Prioridad absoluta a la variable de Render
        self.api_key = os.getenv("GEMINI_API_KEY")
        
        if not self.api_key:
            print("❌ ERROR crítico: No se detecta GEMINI_API_KEY")
        
        genai.configure(api_key=self.api_key)
        
        # Usamos la versión 1.5 que es la más compatible con la librería actual
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def generate_human_response(self, user_message, database_info):
        try:
            prompt = f"""
            Eres un asistente de ventas amable. 
            Basándote en esta info: {database_info}
            Responde a: {user_message}
            """
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"❌ Error en Gemini: {e}")
            return f"Disculpa, en este momento tengo problemas de conexión. Pero confirmo: {database_info}"