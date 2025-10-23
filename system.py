while True:
    print("=====MENU DE OPÇÕES=====")
    print("[1] Validar informações pessoais")
    print("[2] Comparar dois números")
    print("[3] Verificar se o valor é positivo")
    print("[0] Sair")
    opcao = input("Escolha uma opção:")

    if opcao == "1":

        nome = input("Digite seu nome: ")
        while len(nome) <= 3:
            print ("Nome deve ter mais de 3 caracteres")
            print("Tente Novamente")
            nome = input("Digite seu nome: ")


        idade = int(input("Digite sua idade: "))
        while idade <0 or idade>150:
            print("Idade inválida!")
            print("Tente Novamente")
            idade = int(input("Digite sua idade: "))

        salario = float(input("Digite seu salário: "))
        while salario <= 0:
            print("[ERRO] Você deve digitar um valor")
            salario = float(input("Digite seu salário: "))


        genero = input("Digite seu genero ( [F] - [M] - [Outros]): ").lower()
        while genero not in ["f", "m", "outros"]:
            print("[ERRO] Você deve informar seu genero")
            genero = input("Digite seu genero ( [F] - [M] - [Outros]): ").lower()


        estado_civil = input("Digite seu estado civil ([S] - [C] - [D] - [V]: ").lower()
        while estado_civil not in ["s", "c", "d", "v"]:
            print("[ERRO] Você deve informar seu estado civil")
            estado_civil = input("Digite seu estado civil ([S] - [C] - [D] - [V]: ").lower()


        print("\n Dados Validados com sucesso!!")
        print(f"Nome: {nome}")
        print(f"Idade: {idade}Anos")
        print(f"Salário: R${salario:.2f}")
        print(f"Genero: {genero}")
        print(f"Estado Civil: {estado_civil}")
        print(f"Seja bem-vindo, {nome}")



    elif opcao == "2":
        num1 = int(input("Digite sua primeiro numero: "))
        num2 = int(input("Digite sua segundo numero: "))
        if num1 > num2:
            print(f"O maior numéro é: {num1}")
        elif num1 < num2:
            print(f"O maior numéro é: {num2}")
        else:
            print("Os dois números são iguais")


    elif opcao == "3":
        valor = float(input("Digite sua valor: "))
        if valor > 0:
            print("O valor é positivo")
        elif valor < 0:
            print("O valor é negativo")
        else:
            print("O valor é zero")

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("[ERRO] VocÊ deve informar uma opção")

