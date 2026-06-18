##Definir variaveis

produtos=[
    [1,"Volante",3,"Prateleira 01"],
    [2,"Pedal",50,"Prateleira 02"],

]
##Definir funções
def Alterar(): 
    
    global produtos
    linhaprocurada =-1
    alter=input("Qual nome do produto que deseja alterar a quantidade? ").capitalize()
    for i in range(len(produtos)):##Varre linha a linha da matriz
        if(produtos[i][1]==alter):
            linhaprocurada = i
    if (linhaprocurada==-1):
        print("Produto não eiste.")
    else:
        print(f"{produtos[linhaprocurada]}")
        novaQuantidade= int(input(f"Qual a nova quantidade do produto?: "))
        produtos[linhaprocurada][2] = novaQuantidade ## Muda a quantidade do produto desejado
        print("Nova quantidade atualizada com sucesso!")
        print(f"{produtos[linhaprocurada]}")
    travarmenu()


def dados():
    print(produtos)
    for i in range(len(produtos)):##Varre linha a linha da matriz
        if(produtos[i][2]<5): ##Verifica se a quantidade do item é menor ou maior que 5
            print(f"\nCuidado , os produtos {produtos[i]} estão quase sem estoque.")
            print("Hora de repor 🚚")
    travarmenu() ## Com ajuda do caio

def BuscaProd():
    linhaprocurada =-1
    ID = int(input("Qual ID do produto que deseja procurar? "))
    for i in range(len(produtos)):##Varre linha a linha da matriz
        if(produtos[i][0]==ID): ##Verifica se a posição do nome é igual ao nome procurado
            linhaprocurada = i
    if (linhaprocurada==-1):
        print("Produto não eiste.")
    else:
        print(f"O Produto procurado é {produtos[linhaprocurada]}")
    travarmenu()


def remProd():##Remover Produtos
    if (len(produtos)==0):
        print("Não ha produtos. Adicione")
    else:
        ID = int(input("Qual ID do produto que deseja remover? "))
        for i in range(len(produtos)):##Varre linha a linha da matriz
            if(produtos[i][0]==ID): ##Verifica se a posição do nome é igual ao nome procurado
                linhaprocurada = i
        if (linhaprocurada==-1):
            print("Produto não eiste.")
        else:
            print(f"{produtos[linhaprocurada]}")
            Apagar=input("Você quer excluir esse produto? Sim/Não ").capitalize()
            if (Apagar=="Sim"):
                produtos.pop(linhaprocurada)
                print("Produto excluido com sucesso 🗑️")
            else:
                print("Cancelado !!")
    travarmenu() ## Com ajuda do Caio
      
                    
def resProd():##Add Produtos
    novoIDProduto = int(input("Qual ID do novo produto ? "))
    novoNMProduto = input("Qual nome do novo produto ? ")
    novoQTProduto = int(input("Qual a Quantidade do novo produto ? "))
    novoLCProduto = input("Qual a localização do novo produto ? ")
    produtos.append([novoIDProduto,novoNMProduto,novoQTProduto,novoLCProduto]) ## inserimos
    print("Produto inserido com sucesso!")
    travarmenu()



def travarmenu():
    #Nosso código vai aqui
    input("\nPrecione <ENTER> para continuar......")


##Menu 

print("\nBem vindo ao menu interativo do estoque. Por favor selecione uma opção:")
while True : #Roda para sempre
    print("\n1- Buscar produtos | 2- Alterar qauntidades | 3- Status do estoque | 4- Novo produto | 5-Remover produto | 6-Sair")
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
        print("Sistema finalizado !")
        break
