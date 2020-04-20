from typing import List, Any


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
    '''

    Ter que pegar o numero dividir por 16 , pegar os restos ate
     o cosciente for indivisivel e inverter a lista , fazendo com que os numeros maiores que 9
      dentro de uma lista vire letras(na minha cabeca faz sentido)

    '''
    num = float(input("Qual numero deseja Converter : "))
    lst = ()

    cocien_num = 1
    id = 0
    while cocien_num != 0 :
        lst = num % 16
        cocien_num = (lst(id)) // 16
        id += 1
        print(lst)

    lst = lst.sort(reverse=True)


def octadecimal(num) :
    num = int(input("Qual numero deseja Converter : "))

    print('passou aqui')

def binario(num) :
    num = int(input("Qual numero deseja Converter : "))

    print('passou aqui')

def main() :

    m = 0
    cnt = 's'
    while cnt == 's' :

        escolhaDeConversao()
        escolha = int(input("Escolha de Sistema : "))
        umaLinha()
        escolhaValida(escolha , m)
        cnt = input("Deseja Continuar(S/N) : ").lower()

main()



