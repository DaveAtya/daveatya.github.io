with open("input.txt", "r") as file:
    lista = []
    for sor in file:
        sortomb = sor.strip().split('\t')
        lista.append(Adat(....)))
    return lista

count = 0
for row in file:
    if row[0] == "Mecsek" and row[2] == False:
        count += 1
print(count)

result = []
for row in file:
    if row[0] == "Mátra" and row[2] == True and row[5] < row[4]:
        result.append(row)
print(result)

has_offer = False
for row in file:
    if row[0] == "Hortobágy" and row[3] in ["Április", "Május", "Június"]:
        has_offer = True
        break
print(has_offer)

prices = [row[6] for row in file]
print(min(prices))

result = {}
for row in file:
    if row[1] in result:
        result[row[1]] += 1
    else:
        result[row[1]] = 1
print(result)

