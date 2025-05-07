# Please install OpenAI SDK first: `pip3 install openai`

from openai import OpenAI

client = OpenAI(api_key="sk-583761f02276480ea686a639e51d7312", base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "Tú eres un Santa costeño, en el Chocó, Colombia, y hablas con los modismos y palabras de la región. La respuesta no debe ser mayor a 50 palabras, no incluir emojis ni caracteres especiales"},
        {"role": "user", "content": "Hola ¿Cómo estás?"},
    ],
    stream=False
)

print(response.choices[0].message.content)