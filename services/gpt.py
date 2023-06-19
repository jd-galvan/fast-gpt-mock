import openai
from config.settings import settings
from util.constants import GPT_MODEL, GPT_TEMPERATURE, GPT_MAX_TOKENS, GPT_CONTEXT_FOR_MODEL

openai.api_key = settings.gpt_api_key


def get_response(prompt: str):
    response = openai.Completion.create(
        model=GPT_MODEL,
        prompt=f"{GPT_CONTEXT_FOR_MODEL} {prompt}",
        temperature=GPT_TEMPERATURE,
        max_tokens=GPT_MAX_TOKENS
    )
    result = dict(list(response["choices"])[0])["text"].strip()
    return result
