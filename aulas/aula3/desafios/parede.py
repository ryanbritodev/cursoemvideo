largura = float(input("Digite a largura da sua parede em metros: "))
altura = float(input("Digite a altura da sua parede em metros: "))

area = altura * largura
tinta = area / 2

print("A área da sua parede é de {}m² e serão necessários {}L de tinta para realizar a pintura!".format(area, tinta))
2