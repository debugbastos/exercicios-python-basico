import os

MEDIA_APROVACAO = 6.0
MEDIA_RECUPERACAO = 4.0  # abaixo disso reprova direto

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def ler_float(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if 0 <= valor <= 10:
                return valor
            else:
                print("A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

def ler_notas():
    notas = []
    print("\nDigite as notas (digite 'fim' para encerrar):")
    
    while True:
        entrada = input(f"Nota {len(notas)+1}: ").strip().lower()
        
        if entrada == "fim":
            if not notas:
                print("Digite pelo menos uma nota.")
                continue
            break
        
        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Entrada inválida.")
    
    return notas

def calcular_media(notas):
    return sum(notas) / len(notas)

def classificar(media):
    if media >= MEDIA_APROVACAO:
        return "Aprovado"
    elif media >= MEDIA_RECUPERACAO:
        return "Recuperação"
    else:
        return "Reprovado"

def main():
    limpar_tela()
    print("========== SISTEMA DE MÉDIA ==========")

    notas = ler_notas()
    media = calcular_media(notas)
    status = classificar(media)

    print("\n----------- RESULTADO -----------")
    print(f"Notas: {', '.join(f'{n:.2f}' for n in notas)}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {status}")
    print("--------------------------------")

if __name__ == "__main__":
    main()
