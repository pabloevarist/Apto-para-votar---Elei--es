idade_usuario = int(input('Digite a sua idade: '))

while idade_usuario < 16:
    print('Você não tem idade para votar, complete 16 anos e tire seu titulo de eleitor. ')
    idade_usuario = int(input('Digite a sua idade: '))

titulo_eleitor = ''

while titulo_eleitor != "sim" and titulo_eleitor != "não" and titulo_eleitor != "NÃO" and titulo_eleitor != "SIM" and titulo_eleitor != "Sim" and titulo_eleitor != "Não":
    titulo_eleitor = str(input("Possui título de eleitor? Favor digite apenas sim ou não: "))
    if titulo_eleitor == "sim":
        print('Você já tem idade para votar, seja consciente, faço seu voto valer a pena.')
    elif titulo_eleitor == "Sim":
        print('Você já tem idade para votar, seja consciente, faço seu voto valer a pena.')
    if titulo_eleitor == "SIM":
        print('Você já tem idade para votar, seja consciente, faço seu voto valer a pena.')
    elif titulo_eleitor == "não":
        print('Você já tem idade para votar, mas precisa fazer seu título de eleitor, procure o cartório do seu bairro!')
    if titulo_eleitor == "Não":
        print('Você já tem idade para votar, mas precisa fazer seu título de eleitor, procure o cartório do seu bairro!')
    if titulo_eleitor == "NÃO":
        print('Você já tem idade para votar, mas precisa fazer seu título de eleitor, procure o cartório do seu bairro!')

print('Uma eleição é feita para corrigir o erro da eleição anterior, mesmo que o agrave.')