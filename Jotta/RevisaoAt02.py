n1 = float(input("NOTA 1: "))
n2 = float(input("NOTA 2: "))
n3 = float(input("NOTA 3: "))

media = (n1 + n2 + n3) / 3
print("A média é:", media)

if media >= 6:
    print("O aluno foi aprovado.")
else:
    print("O aluno foi reprovado.")