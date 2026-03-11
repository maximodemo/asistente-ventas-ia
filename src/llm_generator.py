import os
import google.generativeai as genai
from dotenv import load_dotenv

class LLMGenerator:
    """
    Motor Generativo usando la API de Google Gemini.
    Toma la información seca de nuestra base de datos y redacta una respuesta natural.
    """
    
    def __init__(self):
        print("[LLMGenerator] Inicializando conexión con Gemini...")
        # 1. Cargamos los secretos
        load_dotenv()
        self.api_key = os.getenv("GEMINI_API_KEY")
        
        # Validación de seguridad:
        if not self.api_key:
            print("⚠️ [ERROR] No se pudo cargar GEMINI_API_KEY. Revisa las Environment Variables en Render.")
        
        # 2. Configuramos la librería
        genai.configure(api_key=self.api_key)
        
        # 3. Elegimos el modelo 2.5 flash
        self.model = genai.GenerativeModel('gemini-2.0-flash') 
        # NOTA: Aunque Google anunció la serie 2.5, en la librería de Python 
        # el ID del modelo suele ser 'gemini-2.0-flash' o el que te dieron en AI Studio.

    def generate_human_response(self, user_message: str, database_info: str) -> str:
        """
        Envía las instrucciones a la IA en la nube y devuelve el texto redactado.
        """
        # 4. El "Prompt" (Las instrucciones para la IA)
        prompt = f"""
        Eres un asistente virtual de atención al cliente de una tienda.
        El usuario te ha dicho exactamente esto: "{user_message}"
        
        Tu sistema interno buscó en la base de datos y encontró esto: "{database_info}"
        
        INSTRUCCIONES:
        - Redacta una respuesta amable, natural y conversacional para el usuario.
        - Usa ÚNICAMENTE la información de la base de datos para responder. No inventes precios ni productos.
        - Si la base de datos dice que "no hay información", discúlpate cordialmente y pregúntale si puedes ayudarle en algo más.
        """
        
        try:
            # 5. Hacemos la llamada a internet (a los servidores de Google)
            respuesta_ia = self.model.generate_content(prompt)
            return respuesta_ia.text
        except Exception as e:
            # Si falla el internet o la API, devolvemos un mensaje seguro
            print(f"[Error LLM] {e}")
            return "Disculpa, en este momento tengo problemas de conexión para redactar tu respuesta. Pero confirmo: " + database_info