def cadastrardados():
# Cadastrando os dados do jogador.
    try: 
        with open('Aluno.txt','a') as arquivo:
            nome = input("Digite o nome do jogador: ")
            idade = input("Digite a idade do jogador: ")
            endereco = input("Digite o endereço do jogador: ")
            nome_responsavel = input("Digite o nome do responsável: ")
            cpf_responsavel = input("Digite o  cpf do responsável: ")
            pe_bom = input("Digite qual o pé bom do jogador: ")
            
            jogador = f"{nome},{idade},{endereco},{nome_responsavel},{cpf_responsavel},{pe_bom}\n"
            
            arquivo.write(jogador)
            
            print("Dados cadastrados com sucesso!")
            
    except Exception as erro:
        print("Oops! Ocorreu um erro ao cadastrar os dados!", str(erro))
        
def listardados():
# Mostrando os dados já cadastrados
    try:
        with open('Aluno.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
            
        if not linhas:   
            print("Não há nenhuma informação desse jogador cadastrado.")
        
        else:
            
            print("Essas são as informações do jogador: ")
            for l in linhas:
                informacoes = l.strip().split(',')
                print ("Nome: ", informacoes[0])
                print ("Idade: " , informacoes[1])
                print ("Endereço: ", informacoes[2])
                print("Nome do  resposável: ", informacoes[3])
                print("CPF do responsável:" , informacoes[4])
                print("Pé bom do jogador: ", informacoes[5])
    
    except Exception as erro:
        print("Oops! Ocorreu um erro ao listar os dados", str(erro))
    
    except FileExistsError:
        print("Erro, arquivo não encontrado.")

def alterardados():
    try:
        with open('Aluno.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
        
        if not linhas: 
            print("Não há nenhuma informação desse jogador cadastrado.")
            return # Para retornar o inicio da função.
        
        cpf = input("Digite o CPF do responsavel do aluno que deseja encontrar")
        findingcpf = False
        
        with open('Aluno.txt', 'w') as arquivo:
            for linha in linhas:
                informacoes = linha.strip().split(',')
                if informacoes[4] == cpf:
                    novo_nome = input("Digite o nome do jogador: ")
                    nova_idade = input("Digite a idade do jogador: ")
                    novo_endereco = input("Digite o endereço do jogador: ")
                    novo_nome_responsavel = input("Digite o nome do responsável: ")
                    novo_cpf_responsavel = input("Digite o  cpf do responsável: ")
                    novo_pe_bom = input("Digite qual o pé bom do jogador: ")

                    nova_linha = f"{novo_nome},{nova_idade},{novo_endereco},{novo_nome_responsavel},{novo_cpf_responsavel},{novo_pe_bom} \n"
                    arquivo.write(nova_linha)
                    findingcpf = True
                    print("Dados do jogador alterados com sucesso")
                else:
                    arquivo.write(linha)
            
            if not findingcpf:
                print("Não foi encontrado nenhum aluno cujo responsavel possua esse cpf.")
    
    except FileExistsError:
        print("Erro, arquivo não encontrado.")  
    except Exception as erro:
        print("Oops! Ocorreu um erro ao listar os dados", str(erro))  
        
def excluirdados():
    try:
        with open('Aluno.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
        
        if not linhas: 
            print("Não há nenhuma informação desse jogador cadastrado.")
            return
        
        cpf = input("Digite o CPF do responsavel do aluno que deseja excluir")
        findingcpf = False
        
        with open('Aluno.txt', 'w') as arquivo:
            for l in linhas:
                informacoes = l.strip().split(',')
            if informacoes[4] == cpf:
                findingcpf = True
                print("Informações excluidas com sucesso")
            else:
                arquivo.write(l)
            if not findingcpf:
                print("Nenhum aluno encontrado cujo cpf do responsável foi o digitado.")
    
    except FileExistsError:
        print("Oops! Ocorreu um erro, arquivo não encontrado")
    
    except Exception as erro:
        print("Oops! Ocorreu um erro ao listar os dados", str(erro)) 
    
    
def fazerbackup():
    try: 
        with open('Aluno.txt', 'r') as arquivo_raiz:
            with open('Aluno_BACKUP.txt', 'w') as arquivo_backup:
                content = arquivo_raiz.read() # LEITURA DO CONTEUDO DO ARQUIVO RAIZ E ARMAZENAMENTO DENTRO DA VARIAVEL CONTENT
                arquivo_backup.write(content) # GRAVANDO O CONTEUDO DA VARIAVEL CONTENT DENTRO DO ARQUIVO_BACKUP.TXT
        print("O Backup foi realizado com sucesso!")
    
    except FileExistsError:
        print("Oops! Ocorreu um erro, arquivo não encontrado")
    
    except Exception as erro:
        print("Oops! Ocorreu um erro ao listar os dados", str(erro)) 