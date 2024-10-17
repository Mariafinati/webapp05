import streamlit as st
from PIL import Image
from ACTlib01 import *

def main():
   Configurar_Pagina("WebApp01 - TESTE", "amplo", "auto", "https://docs.streamlit.io", "mailto:prof.massaki@gmail.com", "#### Aplicativo Teste", "©️")
   Titulo("MEU PRIMEIRO APLICATIVO WEB")
   st.header("Desenvolvido por Massaki de O. Igarashi") 
   Escrever('Hehehehe! Agora todos poderão fazer seu site e programar facilmente!', 'subcabecalho')
   Escrever(' ')
   Escrever('Observação: Em desenvolvimento!', 'subcabecalho')
   image = Image.open('desenvolvimento.jpg')
   st.sidebar.image(image, width=300)

if __name__ == '__main__':
	main()
