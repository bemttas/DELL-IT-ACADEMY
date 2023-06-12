import csv #Adicionei para ler os ".csv"
import os #Utilizo para limpar a tela

with open('DNIT-Distancias.csv', newline='') as csvfile: #Abre o .csv das cidades/distancias
    dist_reader = csv.reader(csvfile, delimiter=';') #Separo cada cidade pelo caracter ';'
    cidades = next(dist_reader)  # Define que a primeira linha do arquivo sao as cidades

    distancias = [] # Cria uma matriz das distancias
    for linha in dist_reader: #Leio as distancias e armazeno em "distancias"
            distancias.append(linha)

with open('Caminhoes.csv', newline='') as csvfile: #Abre o .csv dos caminhoes
    dist_reader = csv.reader(csvfile, delimiter=',') #Dessa vez, separo cada informacao pelo caracter ';'
    caminhao = next(dist_reader) #Le a proxima linha e armazena na lista "caminhao"
    pesoC = next(dist_reader) #Le a proxima linha e armazena os pesos de cada na lista "pesoC"
    preco = next(dist_reader) #Le a proxima linha e armazena os preços na lista "preco"

with open('Itens.csv', newline='') as csvfile: #Abre o .csv dos itens
    dist_reader = csv.reader(csvfile, delimiter=',') #Separa cada informacao pelo caracter ','
    item = next(dist_reader) #Le a proxima linha e armazena os nomes dos itens em "item"
    peso = next(dist_reader) #Le a proxima linha e armazena os pesos dos respectivos itens na lista "peso"


rotas = [] #Inicia uma matriz das rotas que serao cadastradas

def menu1(): #opcao 1
    while True: #Inicia um loop para voltar, caso o usuario digite algo inválido
        print("")
        cidade1 = input(f"Digite o nome da primeira cidade: ").upper().strip() #Utilizo o "upper()" para digitar tudo em maiusculo, para facilitar a busca na lista
        if cidade1 in cidades: #Aqui ele verifica se a cidade1 existe na lista do .csv
            cidade2 = input(f"Digite o nome da segunda cidade: ").upper().strip() #Utilizo o "strip()" para descartar os espaços em branco
            while True:
                if cidade2 in cidades: #Aqui ele verifica se a cidade2 existe na lista do .csv
                    indice1 = cidades.index(cidade1) #Declaro os indices das 2 cidades na lista
                    indice2 = cidades.index(cidade2)
                    distancia = distancias[indice1][indice2] #E busco a distancia de acordo com os indices das cidades


                    while True: #Inicia um loop para voltar, caso o usuario digite uma opcao de transporte inválida
                        print("")
                        print("Selecione uma opção de transporte:")
                        print("")
                        print("1 - Caminhão de pequeno porte")
                        print("2 - Caminhão de médio porte")
                        print("3 - Caminhão de grande porte")
                        print("")


                        menu1 = int(input("Digite a opção desejada : ")) #Recebe a opcao desejada
                        os.system("clear") #Limpa a tela
                        print("")
                        if menu1 == 1: #Caso a opcao seja Caminhão de pequeno porte
                            valor = float(preco[0])*int(distancia) #Multiplica o preco(em float) com a distancia(devo transforma-la em int) com os seus index
                            print("De "+cidade1+ " para "+cidade2+", utilizando um "+caminhao[0]+", a distância é de "+distancia+"km e o custo será de R$"+str(valor))
                            print("") #Adiciono um espaço em branco
                            break
                        elif menu1 == 2: #Caso a opcao seja Caminhão de medio porte
                            valor = float(preco[1])*int(distancia)
                            print("De "+cidade1+ " para "+cidade2+", utilizando um "+caminhao[1]+", a distância é de "+distancia+"km e o custo será de R$"+str(valor))
                            print("")
                            break
                        elif menu1 == 3: #Caso a opcao seja Caminhão de grande porte
                            valor = float(preco[2])*int(distancia)
                            print("De "+cidade1+ " para "+cidade2+", utilizando um "+caminhao[2]+", a distância é de "+distancia+"km e o custo será de R$"+str(valor))
                            print("")
                            break
                        else:
                            print("Opção inválida.") #Caso nao for 1,2 ou 3 imprime:
                    break
                else:
                    print(f"Segunda cidade inválida.") #Caso digite uma cidade inválida
                    cidade2 = input(f"Digite o nome da segunda cidade: ") #Abre o imput para digitar novamente
            break
        else:
            print(f"Primeira cidade inválida") #Caso digite uma cidade inválida

def menu2(): #opçao 2
    while True:
        print("Por favor, digite a cidade de origem seguida das paradas do transporte, separadas por vírgula.")
        print("")
        transporte = input()
        listatransporte = [transporte.strip().upper() for transporte in transporte.split(",")] #Aqui ele recebe as cidades separadas por vírgula, usando o strip() para descartar os espaços em braco e o split(","")

        for cidade in listatransporte:
            if cidade not in cidades: #Se qualquer uma cidade nao existir, ele nao avança
                print("")
                print("Uma ou mais das cidades não existe(m)")
                print("")
                break
            elif len(listatransporte)<2:  #Se digitar apenas uma cidade, ele nao avança
                print("")
                print("Digite no mínimo duas cidades")
                print("")
                break
            else:
                while True:        
                    print("Quais itens você deseja transportar?, para multiplas escolhas, digite separando por virgulas")
                    print("")
                    print("-------------------------------------")
                    print("1 - Celular")
                    print("2 - Geladeira")
                    print("3 - Freezer")
                    print("4 - Cadeira")
                    print("5 - Luminária")
                    print("6 - Lavadora de roupa")
                    print("-------------------------------------")
                    print("")

                    itens = input()
                    listaitens = [int(itens.strip()) for itens in itens.split(",")] #permite 
                    os.system("clear")


                    print("Indique a quantidade dos itens que deseja transportar: ")
                    print("")

                    qtdTotal = []  #Cria uma lista que irá receber as quantidades dos respectivos itens
                    for i in range(len(listaitens)):
                        qtdTotal.append(int(input(item[listaitens[i]-1]+ ":")))

                    qtdtemp = [] #Cria uma lista temporária que irá diminuir as quantidades dos itens que ja foram entregues
                    for i in range(len(qtdTotal)):
                        qtdtemp.append(qtdTotal[i])

                    qtdparadas = [] #Cria uma matriz dos valores de cada parada

                    for i in range(len(listatransporte)-1):
                        print("De " + listatransporte[i] + " até " + listatransporte[i+1]+ " Quantos itens você quer levar?")
                        print("")

                        qtd = [] #Cria uma lista vazia para receber os valores de cada parada
                        for i in range(len(listaitens)): #Percorre a lista de itens
                            while True:
                                valor = int(input(item[listaitens[i]-1]+ ":")) 
                                if (valor <= qtdtemp[i]): #Se o valor for menor ou igual ao total
                                    qtd.append(valor) #Adiciona o valor na lista da parada
                                    qtdtemp[i] = qtdtemp[i]-valor #Entao, sempre quando ele receber um valor, sera decrementado no item no qtdtotal
                                    break

                                else: #Se o valor digitado for maior que a quantidade total, da erro
                                    print("Limite ultrapassado! Digite outro valor")
                                    print("")
                        qtdparadas.append(qtd) #Adicionou a lista de itens na parada no qtdparadas
                    
                    distanciatotal = []  #Cria uma lista de distancias para depois, somar todos os elementos
                    pesototal = []   #Cria uma lista de pesos para depois, somar todos os elementos
                    os.system("clear")

                    print("Transporte cadastrado!")
                    print("")
                    #Imprime todas as paradas e a quantidade de itens que serao entregues nelas
                    for i in range(len(listatransporte)-1):
                        distanciat= int(distancias[cidades.index(listatransporte[i])][cidades.index(listatransporte[i+1])]) #Calcula a distancia de cada parada
                        distanciatotal.append(distanciat) #Adiciona na lista a distancia de todas as paradas
                        print("-------------------------------------")
                        print("De " + listatransporte[i] + " até " + listatransporte[i+1]+ " a distância é de "+ str(distanciat)+"km")
                        print("")
                        print("Para o transporte dos produtos: ")
                        for j in range(len(qtdparadas[i])): #Calcula o peso total de todos os itens
                            print(item[listaitens[j]-1]+" x"+str(qtdparadas[i][j])) 
                            pesot = float(peso[listaitens[j]-1])*qtdparadas[i][j]
                            pesototal.append(pesot)




                    distanciasoma = sum(distanciatotal) #Calcula a soma das distancias
                    pesosoma = sum(pesototal)  #Calcula a soma dos pesos
                    

                    print("Com o peso: "+ str(pesosoma)+"kg")

                    
                    caminhoesn = [0,0,0] #Cria uma lista 
                    for i in range(len(pesoC)): #For com a quantidade de tipos de pesos
                        while pesosoma >= float(pesoC[i]): #Se for maior ou igual ao peso do index ele incrementa em caminhoesn
                            caminhoesn[i] = caminhoesn[i]+1
                            pesosoma = pesosoma -float(pesoC[i]) #Diminiu o valor do peso total

                    if pesosoma < float(pesoC[2]) and pesosoma!=0: #Aqui ele pega o resto, se tiver um valor menor que 1000, ele incrementa 1
                        caminhoesn[i] = caminhoesn[i]+1
                        pesosoma = pesosoma -float(pesoC[i])

                    valorT=[] #Para calcular o valor total de toda a viagem
                    for i in range (len(caminhoesn)): #Percorre a lista dos caminhoes necessários
                        valor = caminhoesn[i]*distanciasoma*float(preco[i]) #E multiplica pelo preço do caminhao e a distancia total
                        valorT.append(valor) #Adiciona o valor na lista valotT

                    unit = float(sum(valorT)/sum(qtdTotal)) #Calcula o preco unitario medio

                    custokm = sum(valorT)/distanciasoma #Custo por km

                    print("")
                    print("Para transportar tudo, a distancia total é de "+str(distanciasoma)+"km")
                    print("")
                    print("Será necessario utilizar: ")
                    print("-------------------------------------") 
                    for i in range (len(caminhoesn)):  #Aqui ele le os caminhoes necessario para o transporte
                        if caminhoesn[i] >=1 :
                            if i == 0:
                                print(caminhao[2]+"  x"+str(caminhoesn[i]))
                            elif i == 2:
                                print(caminhao[0]+"  x"+str(caminhoesn[i]))
                            else:
                                print(caminhao[1]+"  x"+str(caminhoesn[i]))
                    print("-------------------------------------")
                    print("Com o valor total de: R$"+str(sum(valorT)))
                    print("Com o valor unitário médio: R$"+ str(unit))
                    print("-------------------------------------")

                    rota = {'cidades': listatransporte, 'itens': listaitens, 'qtdTotal': qtdTotal, 'valorT': sum(valorT), 'unit': unit, 'custokm': custokm, 'caminhoesn': caminhoesn}
                    rotas.append(rota)
                    
                    break
            break
        break         
    

def menu3():
    if len(rotas)>=1:
        for i, rota in enumerate(rotas):
            print(f"Rota {i+1}: {' --> '.join(rota['cidades'])}") #Concatena as cidades registradas na rota
            print(f"Itens transportados: {', '.join([item[k-1] for k in rota['itens']])}")
            print(f"Quantidades transportadas, respectivamente: {', '.join([str(qtd) for qtd in rota['qtdTotal']])}") #Percorre a lista das quantidades de itens
            print(f"Valor total R${', '.join([str(rota['valorT'])])}")

            print("Veiculos necessarios: ")
            print("-------------------------------------")
            for j in range (len(rota['caminhoesn'])):  #Aqui ele le os caminhoes necessario para o transporte
                if rota['caminhoesn'][j] >=1 :
                    if j == 0:
                        print(caminhao[2]+"  x"+str(rota['caminhoesn'][j]))
                    elif j == 2:
                        print(caminhao[0]+"  x"+str(rota['caminhoesn'][j]))
                    else:
                        print(caminhao[1]+"  x"+str(rota['caminhoesn'][j]))
            print("-------------------------------------")

            print(f"Valor unitário R${', '.join([str(rota['unit'])])}")
            print(f"Custo por Km R${', '.join([str(rota['custokm'])])}") #Imprime o custo por km



            for j in range(len(rota['cidades'])-1): #Aqui ele mostra o custo de cada parada
                print("-------------------------------------")
                distanciat = int(distancias[cidades.index(rota['cidades'][j])][cidades.index(rota['cidades'][j+1])])
                custo_parada = distanciat * rota['custokm']
                print(f"Custo da parada de {rota['cidades'][j]} até {rota['cidades'][j+1]}: R${custo_parada}")
            print("-------------------------------------")
            print("")



    else:
        print("Nenhum transporte foi cadastrado")
        

while True:

    print("")
    print("-------------------------------------")
    print("1 - Consultar trechos x modalidade")
    print("2 - Cadastrar transporte")
    print("3 - Dados estatísticos")
    print("0 - Sair")
    print("-------------------------------------")
    print("")

    menu = int(input(f"Digite a opção desejada: "))
    os.system("clear")
    if menu == 1:
        menu1()
    elif menu == 2:
        menu2()
    elif menu == 3:
        menu3()
    elif menu == 0:
        break
    else:
        print("Opção inválida.")
