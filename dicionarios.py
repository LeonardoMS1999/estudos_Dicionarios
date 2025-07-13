entrada1 = input("Digite o Título : ...")
entrada2 = input("Digite o Genero : ...")
entrada3= int(input("Digite o Lancamento : ..."))
entrada4 = input("Digite o Diretor : ...")

filme = {
    "titulo":entrada1,
    "genero":entrada2,
    "lancamento":entrada3,
    "diretor":entrada4
}

entrada5 = input(" Voce quer atribuir uma nota a esse filme SIM ou NAO ?")
if  entrada5 == "sim" or entrada5 == "SIM":
    nota = float(input("Digite a nota : "))
    filme["nota"] = nota
    print(f'...TITULO... {filme["titulo"]}')
    print(f'...GENERO... {filme["genero"]}')
    print(f'...ANO.LANC...{filme["lancamento"]}')
    print(f'...DIRETOR...{filme["diretor"]}')
    print(f'...NOTA...{filme["nota"]}')
else:
    print(f'...TITULO... {filme["titulo"]}')
    print(f'...GENERO... {filme["genero"]}')
    print(f'...ANO.LANC...{filme["lancamento"]}')
    print(f'...DIRETOR...{filme["diretor"]}')
        





