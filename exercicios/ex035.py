print("----- CONDIÇÃO DE EXISTÊNCIA DE UM TRIÂNGULO -----")

lado1 = float(input("Digite o tamanho do 1° lado: "))
lado2 = float(input("Digite o tamanho do 2° lado: "))
lado3 = float(input("Digite o tamanho do 3° lado: "))

if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado3 + lado1 > lado2:
    print("O triângulo pode existir!")
else:
    print("O triângulo não pode existir!")
