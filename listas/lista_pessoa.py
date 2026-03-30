pessoa = ["bia", "gabriel", "william"]
resultado = [f"{i+1}-{nome.upper()}" for i, nome in enumerate(pessoa) if len(nome) > 3]
print(resultado)