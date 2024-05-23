usuarios = {
  "Nelson" : "1234",
  "Max" : "4321"
}
def verificar_credenciais(usuario, senha):
  print("Verifica se as credenciais são válidas")
  if usuario in usuarios and usuarios[usuario] == senha:
    return True
  else:
    raise ValueError("Nome de usuário e senha incorretos")

def login():
  while True:
    try:
      usuario = input("Digite seu nome de usuário (ou digite sair' para encerrar): ")
      if usuario == 'sair':
        print("Encerrando programa.")
        
        break
      senha = input("Digite sua senha: ")

      if verificar_credenciais(usuario,senha):
        print(f"Login bem sucedido. Bem-vindo, {usuario}")

        break
    except ValueError as e:
      print(e)
    else:
      print("Você está logado com sucesso.")
    finally:
      print("Tentativa de login finalizada")
login()