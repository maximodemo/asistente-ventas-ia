# 🤖 Asistente de Ventas IA (Arquitectura RAG)

Un chatbot de atención al cliente inteligente y moderno, construido con Python, procesamiento de lenguaje natural (NLP) y la API de Google Gemini. 

Este proyecto implementa una arquitectura **RAG (Retrieval-Augmented Generation)** básica, asegurando que la IA responda de forma precisa basándose únicamente en la base de conocimientos del negocio, evitando "alucinaciones" (respuestas inventadas).

## 🚀 Características Principales

* **Búsqueda Inteligente (NLP):** Utiliza SpaCy para normalizar texto, lematizar palabras y eliminar tildes, logrando coincidencias exactas sin importar cómo escriba el usuario (ej. "envíos" = "envio").
* **Generación Aumentada (RAG):** El motor busca primero en una base de datos local (`JSON`) el contexto correcto y se lo inyecta a Google Gemini para formular la respuesta.
* **Interfaz Premium:** Frontend diseñado con HTML/CSS puro (Vanilla), aplicando conceptos modernos de UI/UX (Glassmorphism, animaciones suaves y estilo de burbujas redondeadas tipo iMessage).
* **API RESTful:** Comunicación fluida entre el frontend y el backend mediante rutas POST creadas con Flask.

## 🛠️ Tecnologías Utilizadas

* **Backend:** Python 3, Flask
* **Inteligencia Artificial:** API de Google Gemini (gemini-2.5-flash)
* **NLP (Lenguaje Natural):** SpaCy (`es_core_news_sm`), Unicodedata
* **Frontend:** HTML5, CSS3, JavaScript Vanilla
* **Almacenamiento:** Archivos JSON (Base de conocimientos local)

## ⚙️ ¿Cómo funciona?

1. **Interacción:** El usuario envía un mensaje a través de la interfaz web.
2. **Procesamiento NLP:** El backend recibe el mensaje, limpia caracteres especiales, elimina stopwords y extrae la "raíz" (lema) de las palabras clave usando SpaCy.
3. **Recuperación (Retrieval):** El motor compara las palabras clave del usuario con las etiquetas almacenadas en la base de datos (`knowledge_base.json`) para encontrar la información de la empresa más relevante.
4. **Generación (Generation):** Se envía el mensaje original del usuario junto con el contexto recuperado a la API de Gemini.
5. **Respuesta:** Gemini formula una respuesta natural, educada y basada 100% en las reglas del negocio, la cual se muestra en la interfaz con una animación fluida.

---
*Proyecto creado para demostrar habilidades en integración de LLMs, desarrollo backend con Python y diseño de interfaces web.*