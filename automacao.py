#1 - instalação do pyautogui
import pyautogui
#import de biblioteca de timer
import  time

pyautogui.PAUSE = 0.1

#Apertar tecla win
pyautogui.press("win")
#Escrever o nome do navegador/estoque
pyautogui.write("edge")
#Apertar enter
pyautogui.press("enter")
time.sleep(1.5)
#Escrever o link/credenciais do estoque
link="https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
#Apertar enter
pyautogui.press("enter")
time.sleep(3)
#Fazer login
  #cliclar na localização da forms
pyautogui.click(x=705, y=361)
#escrever credenciais
pyautogui.write("victorinotinho@gmail.com")
pyautogui.press("tab")
pyautogui.write("issoéumasenha")
pyautogui.press("tab")
pyautogui.press("enter")
# time.sleep()

#percorrer linhas da tabela
import pandas as pd
#para cada linha vamos cadastar um produto
tabela = pd.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:

  pyautogui.click(x=695, y=241)
  #codigo
  codigo = tabela.loc[linha, "codigo"]
  pyautogui.write(str(codigo))
  pyautogui.press("tab")
  #marca
  pyautogui.write(tabela.loc[linha, "marca"])
  pyautogui.press("tab")
  #tipo
  pyautogui.write(tabela.loc[linha, "tipo"])
  pyautogui.press("tab")
  #categoria
  pyautogui.write(str(tabela.loc[linha, "categoria"]))
  pyautogui.press("tab")
  #preco_unitario
  pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
  pyautogui.press("tab")
  #custo
  pyautogui.write(str(tabela.loc[linha, "custo"]))
  pyautogui.press("tab")
  #obs
  obs = tabela.loc[linha, "obs"]
  if not pd.isna(obs):
    pyautogui.write(obs)

  #enviar informacao para o estoque
  pyautogui.press("tab")
  pyautogui.press("enter")
  
  
  pyautogui.scroll(5000)