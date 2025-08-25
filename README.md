# 🌤️ Weather Assistant

Asistente conversacional que responde preguntas sobre el **clima actual** y el **pronóstico del tiempo** en distintas ubicaciones.  
Está construido con **LangChain**, **LangGraph**, **OpenAI GPT** y la API de **WeatherAPI**.

---

## 🚀 Instalación

1. Clonar el repositorio:

   git clone https://github.com/CarOmodeo/weather-assistant.git
   cd weather-assistant

2. Crear y activar un entorno virtual:

   python -m venv venv
   source venv/bin/activate # En Linux/Mac
   venv\Scripts\activate # En Windows

3. Instalar dependencias:

   pip install -r requirements.txt

4. Crear un archivo `.env` en la raíz del proyecto con tus claves de API:

   OPENAI_API_KEY=tu_api_key_openai  
    WEATHERAPI_KEY=tu_api_key_weatherapi

   > 🔑 Puedes obtener una clave gratuita de [WeatherAPI](https://www.weatherapi.com/).

---

## ▶️ Uso

Ejecutar el asistente desde la terminal:

    python main.py

Ejemplo de interacción:

    🌤️ Welcome to the weather assistant.

    🧑 You: What’s the weather like in Madrid right now?
    🤖 Assistant: Currently in Madrid it’s 25°C with clear skies.

    🧑 You: What will the weather be like in New York for the next 3 days?
    🤖 Assistant: In New York, light rain is expected tomorrow, with temperatures ranging from 20-25°C over the next 3 days.

Para salir, escribir:

    exit

---

## 📂 Estructura del proyecto

    weather-assistant/
    │── main.py
    │── requirements.txt
    │── .env
    │── README.md
    │
    ├── graph/
    │   └── workflow.py
    │
    ├── model/
    │   └── llm_openai.py
    │
    ├── tools/
    │   └── weather.py

---

## 🛠️ Tecnologías utilizadas

- [LangChain](https://www.langchain.com/)
- [LangGraph](https://github.com/langchain-ai/langgraph)
- [OpenAI GPT](https://platform.openai.com/)
- [WeatherAPI](https://www.weatherapi.com/)
- [Python Dotenv](https://pypi.org/project/python-dotenv/)
- [Requests](https://pypi.org/project/requests/)

---

## 📌 Próximas mejoras

- Agregar más fuentes de datos meteorológicos.
- Soporte para más días en el pronóstico.
- Interfaz web sencilla para interactuar con el asistente.

---

## 💼 Contacto

- 🔗 [LinkedIn](https://www.linkedin.com/in/carolina-omodeo)

---

> 🌟 Gracias por visitar mi perfil. Estoy abierta a nuevas oportunidades y colaboraciones tech.
