import functions as f

# APRENDER SOBRE KIVY
palavra = f.escolha()
jogadas = 0
while jogadas < 5:
    tentativa = f.tentativa()
    print(f.gabarito(palavra, tentativa))
    if tentativa == palavra:
        print(f'Parabéns!')
        break
    jogadas += 1
print(f'obrigado por jogar! A palavra era {palavra}!')
