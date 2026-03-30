nomes = ["ana","carlos","bia","roberto","joao"]
resultado = [nome.upper() for nome in nomes if len(nome) > 4]
print(resultado)