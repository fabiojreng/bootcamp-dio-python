contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}


resultado = contatos.get("chave")
print(resultado)

resultado = contatos.get("chave", {})
print(resultado)

resultado = contatos.get("guilherme@gmail.com", {})
print(resultado)
