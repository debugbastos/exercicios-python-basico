a = float(input("numero 1: "))
b = float(input("numero 2: "))
op = input("Digite a operação (+, -, *, /): ")

if op == "+":
  print("A soma é:", a + b)
elif op == "-":
  print("A subtração é:", a - b)
elif op == "*":
  print("A multiplicação é:", a * b)
elif op == "/":
  if b != 0:
    print("A divisão é:", a / b)
  else:
    print("Erro: Divisão por zero não é permitida.")
else:  print("Operação inválida. Por favor, escolha entre +, -, *, /.") 

