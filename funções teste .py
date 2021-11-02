def l (x):
    tamanho = len(x)
    print("A sua string tem o tamanho de {} letras".format(tamanho))
    return

def espaço (e):
    r = len(e) - e.count(' ')
    print("O seu nome sem os espaços é de {} letras".format(r))
    return

def analisadorcompleto (x , y):
    print ("É {} que a sua variavel está em minusculas".format(x.islower()))
    print ("É {} que está em maiusculas ".format (x.isupper()))
    print ("A letra que você digitou está na posição {}".format(x.find(y)))
    print ("Esta letra aparece {} vezes".format(x.count(y)))
    print ("Você digitou a letra {}".format(y))
    print ("Sua string em maiusculas é {}".format(x.upper()))
    return


nome = str(input("Digite a string que vc deseja que seja analisada."))
letra = str(input("Digite a letra que você quer que seja analisada"))
analisadorcompleto(nome, letra)
