from google import genai
from google.genai.types import Content

API_KEY = "Sua chave - API"


cliente = genai.Client(api_key=API_KEY)

model_name = "gemini-2.5-flash"

print("Tentando inicializar o chat...")

SYSTEM_INSTRUCTION_TEXT = "Você deve dar respostas bem humoradas e sucintas, com uma linguagem de rua sobre o imc peça o peso e a altura e faça a sua analise."

initial_history = [
    Content(
        role="model",
        parts=[{"text": SYSTEM_INSTRUCTION_TEXT}]
    )
]

try:
    chat = cliente.chats.create(
        model=model_name,
        history=initial_history
    )

    print("Chatbot do Senac")
    print("Inicializando Chatbot Senac (digite 'sair' para encerrar)")

    while True:
        user_input = input("Você: ")

        if user_input.lower() == "sair":
            print("Chatbot Senac encerrado.")
            break

        response = chat.send_message(user_input)
        print(f"Chatbot senaczinho: {response.text}")

except Exception as e:
    print(f"Ocorreu um erro na inicialização: {e}")
