perguntas = [
    {"pergunta": "Qual a capital de Portugal?", "resposta": "Lisboa"},
    {"pergunta": "Quanto é 2 + 2?", "resposta": "4"},
    {"pergunta": "Qual é a cor do céu?", "resposta": "Azul"}
]
respostas_certas = 0
for item in perguntas:  
    print(item["pergunta"])
    resposta_usuario = input("Digite sua resposta: ")   
    if resposta_usuario == item["resposta"]:
        print("Resposta correta!")
        respostas_certas += 1
    else:
        print("Resposta incorreta. A resposta correta é:", item["resposta"])
print("acertaste", respostas_certas)