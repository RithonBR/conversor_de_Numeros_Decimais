def escolhaDeConversao() :
    print("-" * 29)
    print("Conversor de Numeros Decimais")
    print("-" * 29)
    print("1. Sistema Hexadecimal.")
    print("2. Sistema Octadecimal.")
    print("3. Sistema Binario.")
    print("-" * 29)

def umaLinha():
    print("-" * 29)

def escolhaValida(esc , m) :
    if esc == 1 :
        print("Sua Escolha Foi o Sistema Hexadecimal.")
        umaLinha()
        hexadecimal(m)
    elif esc == 2:
        print("Sua Escolha Foi o Sistema Octadecimal.")
        umaLinha()
        octadecimal(m)
    elif esc == 3:
        print("Sua Escolha Foi o Sistema Binario.")
        umaLinha()
        binario(m)
    else :
        print("Escolha invalida")
        umaLinha()

def hexadecimal(num) :
    num = int(input("Qual numero deseja Converter : "))
    print('passou aqui')

def octadecimal(num) :
    num = int(input("Qual numero deseja Converter : "))

    print('passou aqui')

def binario(num) :
    num = int(input("Qual numero deseja Converter : "))

    print('passou aqui')


m = 0
cnt = 's'
while cnt == 's' :

    escolhaDeConversao()
    escolha = int(input("Escolha de Sistema : "))
    umaLinha()
    escolhaValida(escolha , m)






    cnt = input("Deseja Continuar(S/N) : ").lower()