# COPIAR OS DADOS DOS CONTRIBUINTES DO ITR
# bibliotecas

import pyautogui
import time
import pyperclip
import pandas as pd
import clipboard 

# TRANSFORMAR COLUNAS EM LISTA      
# copiar dados do contribuinte (seleção por CIB)
tabela = pd.read_excel('Prop_falta5.xlsx')
   
## ACESSAR O PORTAL
# abrir navegador até digitar o CIB
time.sleep(3)
pyautogui.PAUSE = 0.5
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=735, y=611)
time.sleep(3)
pyautogui.write("https://portalitr.receita.fazenda.gov.br")
pyautogui.press("enter")
pyautogui.click(x=1799, y=482)
time.sleep(3)
pyautogui.click(x=1282, y=290)
time.sleep(3)
pyautogui.click(x=1578, y=422)
time.sleep(3)
pyautogui.write("senha")
pyautogui.click(x=951, y=573)
time.sleep(7)

# acesso no portal ITR
pyautogui.click(x=1151, y=256)
time.sleep(2)
pyautogui.click(x=1140, y=276)
time.sleep(2)
pyautogui.click(x=1365, y=274)
time.sleep(2)
pyautogui.click(x=1040, y=452)