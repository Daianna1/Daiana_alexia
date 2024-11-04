meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]  # coada FIFO
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]  # coada FIFO
tavi = ["tava"] * 7  # stiva LIFO
istoric_comenzi = []

cata_ceafa_era_la_inceput = meniu.count("ceafa")
cata_ceafa_s_a_comandat = comenzi.count("ceafa")
pret_ceafa = preturi [1][1]
castig_ceafa = cata_ceafa_s_a_comandat * pret_ceafa

print(cata_ceafa_era_la_inceput - cata_ceafa_s_a_comandat)
print(cata_ceafa_s_a_comandat * pret_ceafa)

student1 = student1.pop(0)
comanda1 = comenzi.pop(0)
print(f"Studentul (student1) a comandat (comanda1)")
istoric_comenzi.append([student1 , comanda1])
tavi.pop()

student2 = student1.pop()
comanda2 = comenzi.pop()
print(f"Studentul (student2) a comandat (comanda2)")
istoric_comenzi.append([student2, comanda2])
tavi.pop()

 Dictionar pentru prețurile produselor pentru calcul rapid
preturi_dict = {produs: pret for produs, pret in preturi}

# 1. Comenzi - simulăm servirea comenzilor pentru fiecare student
print("Simularea comenzilor:")
while studenti and comenzi and tavi:
    student = studenti.pop(0)  # extragem primul student
    comanda = comenzi.pop(0)  # extragem prima comandă
    tava = tavi.pop()  # extragem o tavă din stivă

    # Afisăm detalii despre comanda studentului
    print(f"{student} a comandat {comanda}.")

    # Actualizăm inventarul
    meniu.remove(comanda)
    istoric_comenzi.append(comanda)
    comenzi_efectuate[comanda] += 1
    total_incasari += preturi_dict[comanda]

print("\nInventar final:")

# 2. Inventar - afisăm statistici
print(
    f"S-au comandat {comenzi_efectuate['guias']} guias, {comenzi_efectuate['ceafa']} ceafa, {comenzi_efectuate['papanasi']} papanasi.")
print(f"Mai sunt {len(tavi)} tavi.")
print(f"Mai este ceafa: {'ceafa' in meniu}.")
print(f"Mai sunt papanasi: {'papanasi' in meniu}.")
print(f"Mai sunt guias: {'guias' in meniu}.")

print("\nFinanțe:")

# 3. Finanțe - calculăm veniturile și produsele sub 7 lei
print(f"Cantina a încasat: {total_incasari} lei.")
produse_sub_7_lei = [produs for produs in preturi if produs[1] <= 7]
print("Produse care costă cel mult 7 lei:", produse_sub_7_lei)

