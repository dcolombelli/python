print("=========== \n1 - Gravar \n2 - Ler \n===========")
op = int(input("Escolha uma das opções acima: "))
if op==1:
    nome = str(input('nome do arquivo: '))

    texto = input('digite o texto a ser escrito: ')
    m = open(nome+'.txt',"w")
    m.write(texto)
    m.close()
elif op == 2:
    nome = str(input('nome do arquivo: '))
    m = open(nome+'.txt', "r")
    print(m.read())
    m.close()
else:
    print('Opçao não encontrada.\nReinicie o programa.')