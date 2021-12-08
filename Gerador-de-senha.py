from random import randint
def adivinhar():
    lista = ['q','a','z','w',1,'s','x','e','d',1,'c','r','f','v','t',3,'g','b','y','h','n','u','j',4,'m','i','k','o','l',5,'p','ç','Q','A','Z',6,'W','S','X','E','D','C',7,'R','F','V','T',8,'G','B','Y','H','N','U','J','M','I','K','O','L',9,'P','Ç','!','@','#','$','%','&','*','(',')','-','_','+','=','?']
    x = int(input("Quantos caracteres: "))
    cont = 0
    senha = []
    while cont < x:
        senha.append(lista[randint(0, 61)])
        cont = cont + 1

    senha = "".join([str(_) for _ in senha])
    print (senha)
adivinhar()