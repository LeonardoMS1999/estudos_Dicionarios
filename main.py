filmes = []

def coletarDados():
    entradaTitulo = input("Digite o título:")
    entradaGenero = input("Digite o genero:")
    entradaAno = int(input("Digite o anoo:"))
    return {"titulo": entradaTitulo, "genero": entradaGenero, "ano": entradaAno}
        
for n in range(3):
    filme = coletarDados()
    filmes.append(filme)
               
for filme in filmes:
    print(f'O filme {filme["titulo"]} é do gênero {filme["genero"]} e foi lançado em {filme["ano"]}.')
