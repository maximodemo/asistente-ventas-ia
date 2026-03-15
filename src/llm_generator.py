import os
from google import genai
from dotenv import load_dotenv

class LLMGenerator:
    """
    Motor Generativo usando la NUEVA SDK de Google GenAI (2026).
    Toma la información seca de nuestra base de datos y redacta una respuesta natural.
    """
    
    def __init__(self):
        print("[LLMGenerator] Inicializando conexión con el nuevo cliente de Gemini...")
        # 1. Cargamos los secretos
        load_dotenv()
        self.api_key = os.getenv("GEMINI_API_KEY")
        
        # Validación de seguridad:
        if not self.api_key:
            print("⚠️ [ERROR] No se pudo cargar GEMINI_API_KEY. Revisa tu archivo .env")
            return

        # 2. Configuramos el nuevo Cliente (SDK Moderna)
        try:
            self.client = genai.Client(api_key=self.api_key)
            # Usamos 1.5-flash que es el más estable para el plan gratuito
            self.model_id = "gemini-2.5-flash"
            print(f"[LLMGenerator] Cliente conectado exitosamente. Modelo: {self.model_id}")
        except Exception as e:
            print(f"⚠️ [ERROR] Error al configurar el cliente de Google GenAI: {e}")

    def generate_human_response(self, user_message: str, database_info: str) -> str:
        """
        Envía las instrucciones a la IA usando el nuevo método de generación.
        """
        # 3. El "Prompt" (Las instrucciones para la IA)
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
            # 4. Nueva forma de llamar a la API (generative_ai -> genai)
            response = self.client.models.generate_content(
                model=self.model_id,
                contents=prompt
            )
            
            # Verificamos que la respuesta tenga texto
            if response.text:
                return response.text
            else:
                return "Disculpa, no pude procesar la respuesta. Pero confirmo: " + database_info

        except Exception as e:
            # Capturamos errores de cuota o conexión
            print(f"[Error con la nueva API]: {e}")
            return "Disculpa, en este momento tengo problemas de conexión para redactar tu respuesta. Pero confirmo: " + database_info