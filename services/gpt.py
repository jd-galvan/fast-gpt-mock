import openai
from config.settings import settings
from util.constants import GPT_MODEL

openai.api_key = settings.gpt_api_key


def get_response(prompt: str):
    response = openai.Completion.create(
        model=GPT_MODEL,
        prompt=f"Quiero que me respondas con objetos JSON y si es mas de una respuesta, lo respondas en un arreglo. {prompt}",
        temperature=0.4,
        max_tokens=500
    )
    return response.choices[0].text.strip()
