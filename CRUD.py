import mysql.connector

conexao = mysql.connector.connect(
    host ='localhost',
    user='root',
    password='Wes170702',
    database='cadastro_cliente',
)

cursor = conexao.cursor()

nome = input("digite seu nome: ")
email =input("digite seu email: ")
idade = int(input("digite sua idade: "))
senha =int(input("digite sua senha: "))

comando = f'INSERT INTO clientes(nome, email, idade, senha) VALUES ("{nome}", "{email}", {idade}, {senha})'
cursor.execute(comando)
conexao.commit()

valor = input("senhor precisa editar os dados ? sim / nao: ")
if valor == "sim":
    print("ok")
    dados = input("digite seu email aqui:")
    if dados == email:
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


cursor.close()
conexao.close()