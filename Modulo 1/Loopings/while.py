opçao = 90
while opçao != 3:
    opçao =  int(input("digite:\n 1 - cadastrar \n 2 - logar \n 3 - sair")) 
    if opçao == 2:
        nome_cadastro = input("digite seu nome de usuario:")
        senha_cadastro = input("digite sua senha:")
        print("cadastro criado com sucesso !!")
    elif opçao == 2:
        nome_digitado = input("digite seu usuario:")    
        senha_digitado = input ("digite seu usuario:")
        if nome_cadastro == nome_digitado and senha_cadastro == senha_digitado:
            print("logado com sucesso !!!")
        else:
            print("usuario e senha estao incorretos !!") 
    else:
        print("saiu do sistema")
