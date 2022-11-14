nome = []
cpf = []
anonascimento = []
idade = []
filiado = []

i = 0
while i != "5":
    print("SISTEMA DE CADASTRO")
    print('-1- Inserir Dados de Pessoa Fisica')
    print('-2- Visualizar Dados')
    print('-3- Deletar Dados')
    print('-4- Atualizar Dados')
    print('-5- Finalizar')
    i = input("Digite o codigo da opção que você deseja: ")
        
    if i == "1":
        variavel = int(input("Digite a quantidade de cadastros gostaria de inserir: "))
        cont = 0
        while cont<variavel:
            cont+=1
            print("\n-Inserir dados de Pessoa Fisica - ID", cont)
            nome.append(input("Nome Completo: "))
            cpf.append(input("CPF: "))
            anonascimento.append(input("anonascimento De nasciemento: "))
            idade.append(input("Idade: "))
            filiado.append(input("Filiado: "))
            print("\n-CONFERIR DADOS INSERIDOS-")
            print("1- Nome Compelto: ", nome)
            print("2- CPF: ", cpf)
            print("3- Ano de Nascimento: ", anonascimento)
            print("4- Idade Atual: ", idade)
            print("5- Filiado: ", filiado)
            print("6- Inserir dados novamente")
            i2 = input("Clique enter para confirmar que seus dados estão corretos \nou\nForneça o codigo da opção que deseja: ")
            if i2 == "1":
                nome.append(input("Nome Completo: "))
            if i2 == "2":
                cpf.append(input("CPF: "))
            if i2 == "3":
                anonascimento.append(input("Ano de Nascimento: "))
            if i2 == "4":
                idade.append(input("Idade: "))
            if i2 == "5":
                filiado.append(input("Filiado: "))
            if i2 == "6":
                nome.append(input("Nome Completo: "))
                cpf.append(input("cpf: "))
                anonascimento.append(input("Ano de Nascimento: "))
                idade.append(input("Idade: "))
                filiado.append(input("Filiado: "))
            print("\nDados da pessoa cadastrada: \n\n")
        #i=i-1
    if i == "2":
        if nome == "Não cadastrado" and cpf == "Não cadastrado" and anonascimento == "Não cadastrado" and idade == "Não cadastrado" and filiado == "Não cadastrado":
            print("Nenhum dado foi cadastrado")
        else:
            print("\nCONSULTAR CADASTRO")
            print("Nome Completo: ", nome)
            print("CPF: ", cpf)
            print("Ano de Nascimento: ", anonascimento)
            print("Idade: ", idade)
            print("Filiado: ", filiado)
            i2 = input("Clique enter para retornar ao INICIO")
    if i == "3":
        print("\nDELETAR DADOS")
        print("1- Nome Completo: ", nome)
        print("2- CPF: ", cpf)
        print("3- Ano De nascimento: ", anonascimento)
        print("4- Idade: ", idade)
        print("5- Filiado: ", filiado)
        print("6- Deletar todos os dados")
        i2 = input("Opção: ")
        if i2 == "1":
            nome = "Não cadastrado"
            print("O Nome Digitado Anteriormente Foi Deletado")
        elif i2 == "2":
            cpf = "Não cadastrado"
            print("O CPF Digitado Anteriormente Foi Deletado")
        elif i2 == "3":
            anonascimento = "Não cadastrado"
            print("O Ano de Nascimento Digitado Anteriormente Foi Deletado")
        elif i2 == "4":
            idade = "Não cadastrado"
            print("A Idade Digitada Anteriormente Foi Deletada")
        elif i2 == "5":
            filiado = "Não cadastrado"
            print("O Filiado Digitado Anteriormente Foi Deletado")
        elif i2 == "6":
            nome = "Não cadastrado"
            cpf = "Não cadastrado"
            anonascimento = "Não cadastrado"
            idade = "Não cadastrado"
            filiado = "Não cadastrado"
            print("Todos os dados foram deletados!")
        else:
            print("Opção inválida")
    if i =="4":
        if nome == "Não cadastrado" and cpf == "Não cadastrado" and anonascimento == "Não cadastrado" and idade == "Não cadastrado" and filiado == "Não cadastrado":
            print("Nenhum dado foi cadastrado")
        else:
            print("\nATUALIZAR DADOS")
            print("1- Nome Completo: ", nome)
            print("2- CPF: ", cpf)
            print("3- Ano de Nascimento: ", anonascimento)
            print("4- Idade Atual: ", idade)
            print("5- Filiado: ", filiado)
            print("6- Atualizar dados novamente")
            i2 = input("Opção: ")
            if i2 == "1":
                print("Opção inválida")
                nome.append(input("Nome Completo: "))
                print("\nNome atualizado com sucesso\n\n")
            elif i2 == "2":
                cpf.append(input("cpf: "))
                print("\nCPF atualizado com sucesso\n\n")
            elif i2 == "3":
                anonascimento.append( input("anonascimento: "))
                print("\nAno de Nascimento Atualizado com sucesso\n\n")
            elif i2 == "4":
                idade.append(input("idade: "))
                print("\nIdade atualizadA com sucesso\n\n")
            elif i2 == "5":
                filiado.append(input("filiado: "))
                print("\nFiliado atualizado com sucesso\n\n")
            elif i2 == "6":
                nome.append(input("Nome Completo: "))
                cpf.append(input("CPF: "))
                anonascimento.append(input("Ano de Nascimento: "))
                idade.append(input("Idade: "))
                filiado.append(input("Filiado: "))
                print("\nDados de Pessoa Fisica Atualizados com Sucesso!\n\n")
            else:
                print("Opção inválida")
    if i =="5":
       print("Processo Encerrado")
       #NÃO CONSEGUIMOS IMPLEMENTAR A ESCOLHA DE CONFIRMAÇÃO
