import mysql.connector

conexao = mysql.connector.connect(
    host ='localhost',
    user='root',
    password='Wes170702',
    database='cadastro_cliente',
)

cursor = conexao.cursor()

escolha = input("voce gostaria de deletar algum dado? digite: s /n: ")
if escolha == "s":
    cadastro = input("nos informe seu email cadastrado: ")
    comando = f'DELETE FROM clientes WHERE email = "{cadastro}"'
    
    cursor.execute(comando)
    conexao.commit()

    print("seu email foi deletado com sucesso")

else:
    escolha = "n"
    print("ok tenha um bom dia")



nome = input("digite seu nome: ")
email = input("digite seu email: ")
idade = int(input("digite sua idade: "))
senha = int(input("digite sua senha: "))

comando = f'INSERT INTO clientes(nome, email, idade, senha) VALUES ("{nome}", "{email}", {idade}, {senha})'
cursor.execute(comando)
conexao.commit()

valor = input("senhor precisa editar os dados ? s / n: ")
if valor == "s":
    print("ok")
    print("\nO que você deseja editar?")
    print("1. Nome")
    print("2. Email")
    print("3. Idade")
    print("4. Senha")

    opcao = input("Escolha uma opção (1/2/3/4): ")

    if opcao == "1":
        novo_nome = input("digite seu novo nome: ")
        comando = f'UPDATE clientes SET nome = "{novo_nome}" where nome = "{nome}"'
        cursor.execute(comando)
        conexao.commit()

        print(f"seu nome foi trocado para {novo_nome}")

    elif opcao == "2":
        novo_email = input("digite seu novo email: ")
        comando = f'UPDATE clientes SET email = "{novo_email}" where email = "{email}"'
        cursor.execute(comando)
        conexao.commit()

        print(f"seu novo email é {novo_email}")

    elif opcao == "3":
        nova_idade = input("digite sua nova idade: ")
        comando = f'UPDATE clientes SET idade = {nova_idade} where idade = "{idade}"'
        cursor.execute(comando)
        conexao.commit()

        print(f"sua nova idade é {nova_idade}")

    elif opcao == "4":
        nova_senha = input("digite sua nova senha: ")
        comando = f'UPDATE clientes SET senha = {nova_senha} where senha = "{senha}"'
        cursor.execute(comando)
        conexao.commit()

        print(f"sua nova idade é {nova_senha}")

else:
    valor == "n"
    print(f"ok senhor/a {nome} seu cadastro foi concluido ")


cursor.close()
conexao.close()