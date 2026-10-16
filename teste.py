alunos = [
    {"nome": "Ana", "nota": 8.5},
    {"nome": "Bruno", "nota": 6.0}
]

aluna = alunos [1]["nota"]

if aluna  >= 6:
    print(alunos [1]["nome"], "foi aprovado")
else:
    print(alunos [1]["nome"], "foi reprovado")


for aluno in alunos:
    if aluno ["nota"] >=6:
        print(aluno ["nome"], " aprovado")