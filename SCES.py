##Definir variaveis

produtos=[
    [1,"Volante",3,"Prateleira 01"],
    [2,"pedal",50,"Prateleira 02"]
]
##Definir funções
def Alterar(): 
    
    global produtos
    alter=input("Qual produto deseja alterar a quantidade? com ID ")
    if (alter==produtos):
        alter.append(alter)
        print("Produto alterado")
    travarmenu()

def dados():
    print("-----------------------------------")
    print(produtos)
    travarmenu()  


def BuscaProd():
    linhaprocurada =-1
    ID = int(input("Qual ID do produto que deseja procurar? "))
    for i in range(len(produtos)):##Varre linha a linha da matriz
        if(produtos[i][0]==ID): ##Verifica se a posição do nome é igual ao nome procurado
            linhaprocurada = i
    print(f"O Produto procurado é {}")
    

def remProd():##Remover Produtos
    if (len(produtos)==0):
        print("Não ha produtos. Adicione")
    else:
    
        produtos.pop(produtos)
        print("Produto removido.")
        print(produtos)
    travarmenu()


def resProd():##Add Produtos
    novoProduto = input("Qual ID e nome do novo , quantidade e localização do produto ? ")
    produtos.append(novoProduto) ## inserimos
    print("Produto inserido com sucesso!")
    travarmenu()

def travarmenu():
    #Nosso código vai aqui
    input("\nPrecione <ENTER> para continuar......")


##Menu 

print("\nBem vindo ao menu interativo do estoque. Por favor selecione uma opção:")
while True : #Roda para sempre
    print("\n1- Buscar produtos | 2- Alterar| 3- Produtos| 4- Novo produto | 5-Remover produto | 6-Sair")
    opcao=input("Escolha: ")
    if (opcao=="1"):
        BuscaProd()
    elif (opcao=="2"):
        Alterar()
    elif (opcao=="3"):
        dados()
    elif (opcao=="4"):
        resProd()
    elif (opcao=="5"):
        remProd()    
    elif (opcao=="6"):
        print("Viagem encerrada!")
        break
