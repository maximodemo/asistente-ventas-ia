from src.bot import HybridChatbot

mi_bot = HybridChatbot(name="DevBot")

# Lista de preguntas de prueba
preguntas = [
    "¡Hola! Estoy buscando unos zapatos rojos para correr rápidamente, ¿tienen disponibles?",
    "Me gustaría saber a qué hora abren y cierran el local",
    "Quiero comprar una computadora gamer" # Esta no está en el JSON, debería fallar elegantemente
]

print("-" * 50)
for pregunta in preguntas:
    print(f"Usuario: '{pregunta}'")
    resultado = mi_bot.process_message(pregunta)
    print(f"Bot (Score: {resultado['confidence_score']}): {resultado['response']}")
    print("-" * 50)