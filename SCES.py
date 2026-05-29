##Definir variaveis
combustivel=100
produtos=[]
##Definir funções
def viajar(): ##Gastar combustivel
    
    global combustivel
    if (combustivel>=30):
        combustivel= combustivel- 30
        print("A nave viajou com sucesso 🚀🚀")
    else:
        print("Voce está sem combustivel suficiente. Abasteça!")


def abastecer():
    print("-----------------------------------")
    global combustivel
    combustivel=100
    print("Tanque cheio! ⛽")

def stNave():
    print("----------STATUS DA NAVE-----------")
    print(f"A nave esta com {combustivel}L de combustivel")
    print(f"Os produtos são:{produtos}")
    print("-----------------------------------")


def resTrip():##Add tripulantes
    novoProduto = input("Qual nome do novo produto ? ")
    produtos.append(novoProduto) ## inserimos
    print("Produto inserido com sucesso!")

##Menu 

print("\nBem vindo ao menu interativo da nave. Por favor selecione uma opção:")
while True : #Roda para sempre
    print("\n1- Mostrar status da nave| 2- Viajar| 3- Abastecer| 4- Novo produto |5-Sair")
    opcao=input("Escolha: ")
    if (opcao=="1"):
        stNave()
    elif (opcao=="2"):
        viajar()
    elif (opcao=="3"):
        abastecer()
    elif (opcao=="4"):
        resTrip()
    elif (opcao=="5"):
        print("Viagem encerrada!")
        break
