import pyautogui
import time
import pandas as pd

# Tempo de esperar da execução de cada linha de codigo

pyautogui.PAUSE = 0.5

# Entrar no navegador

pyautogui.press("win")
pyautogui.write("Firefox")
pyautogui.press("enter")

# LInk do sistema

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# Fazer login no sistema

time.sleep(3)

pyautogui.click(x=313, y=396)
pyautogui.write("pedrinhoAraujo@acad.ifma.edu.br")

# Primeira opção 

# pyautogui.click(x=254, y=489)
# pyautogui.write("Pisantino")

# Segunda opção
pyautogui.press("tab")
pyautogui.write("Pisantino")

pyautogui.click(x=483, y=557)

#Importar base de dados dos produtos

table = pd.read_csv("./Powerup/produtos.csv")

print(table)

time.sleep(2)

# cadastrar um produto


for linha in table.index:
    pyautogui.click(x=403, y=278)

    # Codigo
    codigo = table.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab") 

    # Marca 
    marca = table.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab") 

    # Tipo
    tipo = table.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab") 

    # Categoria
    categoria = table.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab") 

    # Preço Unitário
    preco_unitario = table.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab") 

    # Custo
    custo = table.loc[linha, "custo"] 
    pyautogui.write(str(custo))
    pyautogui.press("tab") 

    # OBS
    obs = table.loc[linha, "obs"]
    if not pd.isna(obs): 
        pyautogui.write(obs)
    pyautogui.press("tab") 

    pyautogui.press("enter")

    pyautogui.scroll(1000)

