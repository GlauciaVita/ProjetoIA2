import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

CHAVE_API_GOOGLE = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=CHAVE_API_GOOGLE)

MODELO = "gemini-1.5-flash"

prompt = "Liste apenas os nomes dos produtos e ofereça uma breve descrição"
config_modelo = {
    "temperature" : 0.1,
    "response_mime_type" : "text/plain"
}

lln = genai.GenerativeModel(
    model_name=MODELO,
    system_instruction=prompt,
    generation_config=config_modelo,
)

pergunta = "Liste tres produtos de moda para ir ao shopping"

resposta = lln.generate_content(pergunta)

print(f"Resposta: {resposta.text}")