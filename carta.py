def val_idade(idade):
    if idade <18:
        print('Desculpe você não tem idade para dirigir ',nome)
        return False
    elif idade >= 18 :
        print('Vamos começar')
        return True 
    #Verifica se o usuário tem idade para dirigir 

def escolher_carta():
    print('escolha uma das opções a seguir')
    print('1- Carro, 2- Moto ou 3-Carro e moto')
    return int(input())
# verifica se o usuário prefere carro, moto ou ambos para a compra

def calcular_preco(escolha):
    carro = 15000
    moto = 8000
    

    if escolha == 1:
        return carro
    elif escolha == 2:
        return moto
    else:
        return carro + moto
    #calcula o preço de acordo com a escolha do usuário
    
def desconto(valor):
    return valor - (valor *0.10)
#Calcula o desconto

nome = input('Qual é o seu nome ?')
idade = int(input('Quantos anos você tem ?'))
#definindo as variáveis para a primeira função

if val_idade(idade):
    escolha = escolher_carta()
    print('Ok, vou calcular o preço')
    valor = calcular_preco(escolha)
    print(nome,' ficou ', valor,' reais, mas vou ver se consigo um desconto pra você ')
    valor = desconto(valor)
    print('Eba, consigui um desconto, ficando um total de ',valor,' reais')
    print('Tem interesse ? 1-sim   2-não')
    interesse = int(input())
    if interesse == 1:
        print('Que bom começaremos amanhã!')
    else:
        print('Que pena, volte sempre')