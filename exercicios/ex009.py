print(""" _____  _    ____  _   _   _    ____    _    
|_   _|/ \  | __ )| | | | / \  |  _ \  / \   
  | | / _ \ |  _ \| | | |/ _ \ | | | |/ _ \  
  | |/ ___ \| |_) | |_| / ___ \| |_| / ___ \ 
  |_/_/   \_\____/ \___/_/   \_\____/_/   \_|""")

numero = int(input("\nDigite um número para ver sua tabuada: "))

titulo = "TABUADA DO {}".format(numero)

print("-" * 12)
print(titulo)
print("{} x {:2} = {}".format(numero, "1", numero * 1))
print("{} x {:2} = {}".format(numero, "2", numero * 2))
print("{} x {:2} = {}".format(numero, "3", numero * 3))
print("{} x {:2} = {}".format(numero, "4", numero * 4))
print("{} x {:2} = {}".format(numero, "5", numero * 5))
print("{} x {:2} = {}".format(numero, "6", numero * 6))
print("{} x {:2} = {}".format(numero, "7", numero * 7))
print("{} x {:2} = {}".format(numero, "8", numero * 8))
print("{} x {:2} = {}".format(numero, "9", numero * 9))
print("{} x {:2} = {}".format(numero, "10", numero * 10))
print("-" * 12)
