import random

# 1. Lista de cuvinte și alegerea cuvântului la întâmplare
cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progres = ["_" for _ in cuvant_de_ghicit]

# 2. Inițializarea numărului de încercări
incercari_ramase = 6
litere_incercate = []

# Afișarea șablonului inițial
print("Bun venit la jocul Spânzurătoarea!")
print("Cuvântul de ghicit este:", " ".join(progres))
print(f"Încercări rămase: {incercari_ramase}\n")

# Buclă principală de joc
while "_" in progres and incercari_ramase > 0:
    # Cererea unei litere
    litera = input("Introdu o literă: ").lower()

    # Verificarea validității
    if len(litera) != 1 or not litera.isalpha():
        print("Te rog să introduci o singură literă validă.")
        continue

    if litera in litere_incercate:
        print("Ai mai încercat această literă. Te rog să încerci alta.")
        continue

    litere_incercate.append(litera)

    # Verificarea literei în cuvânt
    if litera in cuvant_de_ghicit:
        for idx, char in enumerate(cuvant_de_ghicit):
            if char == litera:
                progres[idx] = litera
        print("Bravo! Ai găsit o literă!")
    else:
        incercari_ramase -= 1
        print("Din păcate, litera nu se află în cuvânt.")

    # Afișarea progresului și încercărilor rămase
    print("Cuvântul de ghicit este:", " ".join(progres))
    print(f"Încercări rămase: {incercari_ramase}\n")

# Încheierea jocului
if "_" not in progres:
    print(f"Felicitări! Ai ghicit cuvântul: {cuvant_de_ghicit}!")
else:
    print(f"Ai pierdut! Cuvântul era: {cuvant_de_ghicit}.")
