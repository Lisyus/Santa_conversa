# Please install OpenAI SDK first: `pip3 install openai`

import os
from dotenv import load_dotenv
from openai import OpenAI

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener la clave API desde la variable de entorno
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("La clave API 'OPENAI_API_KEY' no está configurada en el archivo .env.")

client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "Tú eres un Santa costeño, en el Chocó, Colombia, y hablas con los modismos y palabras de la región. La respuesta no debe ser mayor a 50 palabras, no incluir emojis ni caracteres especiales"},
        {"role": "user", "content": "Hola ¿Cómo estás?"},
    ],
    stream=False
)

print(response.choices[0].message.content)