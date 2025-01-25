import google.generativeai as genai

MODELO_FLASH = "gemini-1.5-flash"
MODELO_PRO = "gemini-1.5-pro"

CUSTO_ENTRADA_FLASH = 0.075
CUSTO_SAIDA_FLASH = 0.30

CUSTO_ENTRADA_PRO = 3.5
CUSTO_SAIDA_PRO = 10.50

model_flash = genai.get_model(f"models/{MODELO_FLASH}")
limites_flash = {
    "tokens_entrada" : model_flash.input_token_limit,
    "tokens_saida" : model_flash.output_token_limit
}

print(f"limites modelo flash: {limites_flash}")

print("\n")

model_pro = genai.get_model(f"models/{MODELO_PRO}")
limites_pro = {
    "tokens_entrada" : model_pro.input_token_limit,
    "tokens_saida" : model_pro.output_token_limit
}

print(f"limites modelo pro: {limites_pro}")

lln_flash = genai.GenerativeModel(
    f"models/{MODELO_FLASH}"
)

qtd_tokens = lln_flash.count_tokens("O que é uma calça de alfaiataria")
print(f"qtd tokens: {qtd_tokens}")
