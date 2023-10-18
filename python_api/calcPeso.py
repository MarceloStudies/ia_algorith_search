def calcular_peso(dificuldade, tempo, peso_dificuldade=5.0, peso_tempo=5.0):
    if 1.0 <= dificuldade <= 20.0 and 1 <= tempo <= 1000:
        escala_dificuldade = (peso_dificuldade * dificuldade) / 20.0
        escala_tempo = (peso_tempo * tempo) / 1000.0
        peso_total = (escala_dificuldade * escala_tempo) * 10.0
        return peso_total
    else:
        return "Valores de dificuldade e tempo devem estar dentro dos limites permitidos."

dificuldade = 11.0
tempo = 500
peso_questao = calcular_peso(dificuldade, tempo)
print(f"Peso da questão: {peso_questao}")
