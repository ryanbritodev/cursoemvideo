print(""" ____                                     /\/|       
|  _ \ _ __ ___   __ _ _ __ ___  ___ ___ |/\/_  ___  
| |_) | '__/ _ \ / _` | '__/ _ \/ __/ __|/ _` |/ _ \ 
|  __/| | | (_) | (_| | | |  __/\__ \__ \ (_| | (_) |
|_| _ |_|  \___/_\__, |_|  \___||___/___/\__,_|\___/ 
   / \   _ __(_) |___/__ ___   /_/| |_(_) ___ __ _   
  / _ \ | '__| | __| '_ ` _ \ / _ \ __| |/ __/ _` |  
 / ___ \| |  | | |_| | | | | |  __/ |_| | (_| (_| |  
/_/   \_\_|  |_|\__|_| |_| |_|\___|\__|_|\___\__,_|  """)

termo = int(input("\nQual o 1° TERMO da sua PA? "))
razao = int(input("Qual a RAZÃO da sua PA? "))
inicio = 1

print("\n10 PRIMEIROS TERMOS DA PA:")
while inicio <= 10:
    print(termo, "→ ", end="")
    termo += razao
    inicio += 1
print("FIM!")
