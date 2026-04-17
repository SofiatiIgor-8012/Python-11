# Lendo a idade
nota = float(input("Digite a nota do alunos (0 a 10):"))

# Verificando varias condicoes
if nota >= 9:
    print("Conceito: A")
elif nota >=7 <9:
    print("Conceito: B")
elif nota >=5 <7:
    print("Conceito: C")
else:
    print("Conceito: D")