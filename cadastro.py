clientes = []
def menu(): 
  print("MENU")
  print("1- Cadastrar clientes")
  print("2- Listar clientes")
  print("0- Sair")
while True: 
  menu()
  opcao = input("Escolha uma opção: ")
  if opcao == "1":
    nome = input(" Digite o nome do cliente: ")
    clientes.append(nome)
    print ("Cliente cadastrado com sucesso")
  elif opcao == "2":
    print ("Clientes cadastrados:")
    for cliente in clientes: 
     print (cliente) 
  elif Opcao == "0":
    print ("Saindo do sistema")
    break 
else:
    print("Opção invalida")

