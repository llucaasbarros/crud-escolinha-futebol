from funcoes import * 
import sys
print("*"*40)
print("Lucas Pereira de Barros e Juan Lovera")
print("*"*40)


print("ESCOLINHA DE FUTEBOL DO CLUBE DE REGATAS FLAMENGO")
print("*"*40)

while True:
   
    print("1. Cadastrar informações do jogador")
    print("2. Listar informações do jogador")
    print("3. Alterar informações do jogador")
    print("4. Excluir informações do jogador")
    print("5. Realizar backup do cadastro do jogador")
    print("0 . Sair")
    
    opcao = int(input("Escolha a opção desejada: "))
    
    if opcao == 1:
        cadastrardados()
    elif opcao == 2:
        listardados()
    elif opcao == 3:
        alterardados()
    elif opcao == 4:
        excluirdados()
    elif opcao == 5:
        fazerbackup()
    elif opcao == 0:
        print("Saindo do programa...")
        break
