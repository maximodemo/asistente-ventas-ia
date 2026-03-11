# 🤖 Asistente de Ventas IA (Arquitectura RAG)

Este repositorio contiene un chatbot de atención al cliente desarrollado con Python, procesamiento de lenguaje natural (NLP) y la API de Google Gemini. 

El objetivo principal del proyecto es implementar una arquitectura **RAG (Retrieval-Augmented Generation)** funcional. El sistema está diseñado para que la IA responda basándose exclusivamente en una base de conocimientos local, garantizando que la información entregada al cliente sea siempre exacta, controlada y alineada con las reglas del negocio.

## 🚀 Características Principales

* **Procesamiento de Lenguaje Natural (NLP):** Utiliza `spaCy` para normalizar el texto, aplicar lematización y eliminar tildes. Esto previene errores de búsqueda causados por faltas de ortografía o variaciones gramaticales (ej. "envíos" = "envio").
* **Generación Aumentada (RAG):** El motor recupera primero el contexto adecuado desde una base de datos local y lo inyecta en un prompt estructurado para que la API de Gemini formule la respuesta.
* **API RESTful:** La comunicación entre la interfaz de usuario y el servidor se gestiona mediante rutas POST construidas con Flask.
* **Interfaz de Usuario:** Frontend desarrollado con HTML, CSS y JavaScript (Vanilla), aplicando diseño responsivo y una arquitectura visual conversacional orientada a la experiencia del usuario.

## 🛠️ Tecnologías Utilizadas

* **Backend:** Python 3, Flask
* **Inteligencia Artificial:** API de Google Gemini
* **NLP (Lenguaje Natural):** SpaCy (`es_core_news_sm`), Unicodedata
* **Frontend:** HTML5, CSS3, JavaScript Vanilla
* **Almacenamiento:** Archivos JSON (Base de conocimientos local)

## ⚙️ ¿Cómo funciona?

1. **Interacción:** El usuario envía su consulta a través de la interfaz web.
2. **Procesamiento NLP:** El backend recibe el mensaje y utiliza la librería `spaCy` para limpiar los caracteres especiales, filtrar stopwords y extraer los lemas (la raíz de las palabras clave).
3. **Recuperación (Retrieval):** El sistema busca coincidencias entre los lemas extraídos y las etiquetas almacenadas en la base de datos (`knowledge_base.json`) para recuperar el contexto específico.
4. **Generación (Generation):** Se envía el mensaje original del usuario junto con el contexto recuperado a la API de Gemini.
5. **Respuesta:** La IA redacta una respuesta coherente y natural basada *estrictamente* en el contexto proporcionado, la cual se renderiza de vuelta en el navegador del usuario.

---
*Desarrollé este proyecto para profundizar mis conocimientos en la integración de modelos de lenguaje (LLMs), manejo de APIs de terceros y desarrollo backend con Python.*