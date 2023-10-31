nomes,idades,sexos=[],[],[]
for pessoas in range(4):
    pessoas = {
        "nome": str(input("nome: ")),
        "idade": int(input("idade: ")),
        "sexo": str(input("masculino: m, feminino: f: ")).lower()
    }
    nomes.append(pessoas["nome"]),idades.append(pessoas["idade"]),sexos.append(pessoas["sexo"]),
print(f"{(sum(idades))/4}")
maiori=max(idades)
indicem=idades.index(maiori)
homen = nomes[indicem]
print(f"{homen}")
mulheres20=0
for mulheres in range(4):
    if sexos[mulheres] == "f" and idades[mulheres] > 20:
        mulheres20+=1 
print(f" mulheres com mais de vinte anos {mulheres20}")