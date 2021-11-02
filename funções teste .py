def l (x):
    tamanho = len(x)
    print("O teu nome tem o tamanho de {} letras".format(tamanho))
    return

def espaço (e):
    r = len(e) - e.count(' ')
    print("O seu nome sem os espaços é de {} letras".format(r))
    return

def analisadorcompleto (x , y):
    print ("É {} que a sua variavel é uma string".format(x.isalpha()))
    print ("É {} que a sua varivel está em minusculas".format(x.islower()))
    print ("Esta em maiusculas? {} ".format (x.isupper()))
    print ("A letra que você digitou está na posição {}".format(x.find(y)))
    return


nome = str(input("Digite a string que vc deseja que seja analisada.")).upper()
print ("Digite a letra que deseja saber onde está na palavra")
letra = str(input()).upper()
print (input(" \nO caractere {} se encontra nessa string por {} vezes \n Tecle algo para continuar essa analise".format(letra, nome.count(letra))))
l(nome)
espaço(nome)
analisadorcompleto(nome, letra)
