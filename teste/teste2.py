def login(usuario, senha):
    if usuario == "admin" and senha == "1234":
        return "Acesso permitido"
    else:
        return "Acesso negado"
    
print(login("ad13in", "1234"))  

       
