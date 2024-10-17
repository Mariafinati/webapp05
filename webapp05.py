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
   url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQtWlwpc4_SPunNRbY9MWEsLemJ4-kr7JK1OE8avUWMU7BULFMQNt6-bFkIsJ-_7nOvH3sFOSyOFkeb/pub?gid=1851101266&single=true&output=csv"
   db = Ler_GooglePlanilha(url, coluna_indice = None)
   Escrever(db.columns())
   Escrever(db)

if __name__ == '__main__':
	main()
