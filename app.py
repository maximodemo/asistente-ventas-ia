from flask import Flask, request, jsonify, render_template
from src.bot import HybridChatbot

# 1. Inicializamos la aplicación web de Flask
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# 2. Encendemos nuestro bot (Solo se enciende una vez cuando arranca el servidor)
mi_bot = HybridChatbot(name="IngenieroBot")

# 3. Creamos un "Endpoint" (Una ruta o puerta de entrada en internet)
# El decorador @app.route le dice a Flask: "Cuando alguien entre a /api/chat usando el método POST, ejecuta esta función".
@app.route('/api/chat', methods=['POST'])
def chat_endpoint():
    try:
        # Obtenemos los datos que nos envía el usuario en formato JSON
        datos_usuario = request.get_json()
        
        # Verificamos que el usuario realmente haya enviado un "mensaje"
        if not datos_usuario or 'mensaje' not in datos_usuario:
            return jsonify({"error": "Falta el campo 'mensaje' en la petición"}), 400
        
        mensaje = datos_usuario['mensaje']
        
        # ¡Aquí conectamos la web con nuestro motor!
        # Le pasamos el mensaje a tu clase HybridChatbot
        resultado = mi_bot.process_message(mensaje)
        
        # Devolvemos la respuesta al usuario en formato JSON (estándar web)
        return jsonify(resultado), 200

    except Exception as e:
        # Buena práctica: Siempre manejar errores (try/except) para que el servidor no se caiga
        return jsonify({"error": str(e)}), 500

# 4. Bloque para arrancar el servidor
if __name__ == '__main__':
    print("\n" + "="*50)
    print("🚀 Servidor API iniciando en http://127.0.0.1:5000")
    print("="*50 + "\n")
    # debug=True permite que el servidor se reinicie solo si hacemos cambios en el código
    app.run(debug=True, port=5000)