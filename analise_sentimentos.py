import os
import google.generativeai as genai
from google.api_core.exceptions import NotFound, GoogleAPIError, ServerError
from dotenv import load_dotenv

load_dotenv()

CHAVE_API_GOOGLE = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=CHAVE_API_GOOGLE)

modelo = "gemini-1.5-pro"

def carrega(nome_do_arquivo):
  try:
    with open(nome_do_arquivo, "r") as arquivo:
      dados = arquivo.read()
      return dados
  except IOError as e:
    print(f"Erro: {e}")
    
def salva(nome_do_arquivo, conteudo):
    try:
        with open(nome_do_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(conteudo)
    except IOError as e:
        print(f"Erro ao carregar o arquivo: {e}")
        

def analisador(nome):
    prompt_sistema = f"""
            Você é um analisador de sentimentos de avaliações de produtos.
            Escreva um parágrafo com até 50 palavras resumindo as avaliações e
            depois atribua qual o sentimento geral para o produto.
            Identifique também 3 pontos fortes e 3 pontos fracos identificados a partir das avaliações.

            # Formato de Saída

            Nome do Produto:
            Resumo das Avaliações:
            Sentimento Geral: [utilize aqui apenas Positivo, Negativo ou Neutro]
            Ponto fortes: lista com três bullets
            Pontos fracos: lista com três bullets
        """
        
    prompt_usuario = carrega(f"dados/avaliacoes-{nome}.txt")

    print(f"Iniciando a análise de sentimentos do produto: {nome}")

    try:
        llm = genai.GenerativeModel(
                model_name=modelo,
                system_instruction=prompt_sistema
        )
    except NotFound as e:
        print(f"Erro no modelo: {e}")    

    try: 
        resposta = llm.generate_content(prompt_usuario)
        texto_resposta = resposta.text

        salva(f"dados/resposta-{nome}", texto_resposta)
    except Exception as e:
        print(f"Erro ao realizar a análise de sentimentos: {e}")
    except GoogleAPIError as e:
        print(f"Erro na API: {e}")
    except ServerError as e:
        print(f"Erro no servidor: {e}")
    
    
def main():
    lista = ["Camisetas de algodão orgânico", "Jeans feitos com materiais reciclados", "Maquiagem mineral", "Papel higienico"]   
    
    for produto in lista:
         analisador(produto)
         
if __name__ == "__main__":
    main()         

    