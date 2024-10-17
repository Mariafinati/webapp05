import streamlit as st
from PIL import Image
from Massaki01 import *

def main():
   Configurar_Pagina("WebApp01 - TESTE", "amplo", "auto", "https://docs.streamlit.io", "mailto:prof.massaki@gmail.com", "#### Aplicativo Teste", "©️")
   Titulo("MEU PRIMEIRO APLICATIVO WEB")
   st.header("Desenvolvido por Massaki de O. Igarashi")
   
   MKD(Versao(), 'left', 18, 'blue')
      
   MKD('⬜ Massaki01 - Biblioteca teste', 'left', 48, 'darkblue')
      
   Escrever('Hehehehe! Agora todos poderão fazer seu site e programar facilmente!', 'subcabecalho')
   Escrever(' ')
   Escrever('Observação: Em desenvolvimento!', 'subcabecalho')
   image = Image.open('desenvolvimento.jpg')
   st.sidebar.image(image, width=300)
	
   CONTAINER = Container(True)
   with CONTAINER: 
      MKD('Biblioteca teste para facilitar o desenvolvimento de sites a qualquer pessoa leiga na Programação.', "justified", 20, "black")
    
   Barra_Lateral_Texto("Desenvolvido por Massaki Igarashi")

   colunas = Colunas(4)       
    
   with colunas[0]:
   	BTN1 = Botao_M("✔️ Botão 1")
   with colunas[1]:
        BTN2 = Botao_C("✔️ Botão 2", "gray")
   with colunas[2]:
        BTN3 = Botao_M("Botão 3")
   with colunas[3]:   
        BTN4 = Botao_C("✔️ Botão 4")
       
   if BTN1:
        Escrever("Você clicou no Botão 1")
   if BTN2:
        Escrever("Você clicou no Botão 2")
   if BTN3:
        Escrever("Você clicou no Botão 3")       
   if BTN4:
        Escrever("Você clicou no Botão 4") 
if __name__ == '__main__':
	main()
