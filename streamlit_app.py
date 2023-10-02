import streamlit as st
import openai

# Configurar la clave de la API de OpenAI
api_key = st.sidebar.text_input("Enter your OpenAI API key", type="password")

if not api_key:
    st.warning("Please enter a valid API key to continue.")
else:
    openai.api_key = api_key
    # Continuar con el resto del código que utiliza la clave de API

# Título de la aplicación
st.title("ChatGPT")

# Campo de entrada de texto
user_input = st.text_input("Usuario:", "")

# Conversación inicial
conversation = []

# Función para generar una respuesta de ChatGPT
def generar_respuesta(input_text, conversation):
    # Agregar la entrada del usuario a la conversación
    conversation.append({"role": "user", "content": input_text})
    
    # Generar una respuesta de ChatGPT
    respuesta = openai.Completion.create(
        engine="text-davinci-003",
        prompt=conversation,
        temperature=0.7,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7
    )
    
    # Agregar la respuesta de ChatGPT a la conversación
    conversation.append({"role": "assistant", "content": respuesta.choices[0].text.strip()})
    
    return respuesta.choices[0].text.strip()

# Botón para enviar la entrada del usuario y generar una respuesta
if st.button("Enviar"):
    if user_input:
        respuesta = generar_respuesta(user_input, conversation)
        st.text_area("ChatGPT:", value=respuesta, height=200, max_chars=None, key=None)
    else:
        st.warning("Por favor, ingresa un mensaje.")
