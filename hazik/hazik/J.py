# A fájl beolvasása
diakok = []
with open('input.txt', 'r') as f:
    for sor in f:
        tanulo_kod, nev, math_info_csoport, angol_csoport, idegen_nyelv, neme, csalad_tagok, testverek = sor.strip().split(';')
        diakok.append({
            'tanulo_kod': int(tanulo_kod),
            'nev': nev,
            'math_info_csoport': math_info_csoport,
            'angol_csoport': angol_csoport,
            'idegen_nyelv': idegen_nyelv,
            'neme': neme,
            'csalad_tagok': int(csalad_tagok),
            'testverek': int(testverek),
        })

osszes_diak = len(diakok)
print('Az összes diák száma:', osszes_diak)

alfa_diakok = [diak for diak in diakok if diak['math_info_csoport'] == 'alfa']
print('Az alfa csoportban lévő diákok száma:', len(alfa_diakok))

nemet_diakok = [diak for diak in diakok if diak['idegen_nyelv'] == 'német']
print('Az német nyelvet választó diákok száma:', len(nemet_diakok))

lanyok = [diak for diak in diakok if diak['neme'] == 'L']
print('A lányok száma, akik a testnevelés szerint L bontásban vannak:', len(lanyok))

legalabb_ketto_testver = [diak for diak in diakok if diak['testverek'] >= 2]
print('Azoknak a száma, akiknek legalább 2 testvérük van:', len(legalabb_ketto_testver))

tobb_mint_ketto_testver = [diak for diak in diakok if diak['testverek'] > 2]
print('Hány olyan diák van, akiknek több mint 2 testvére van?:', len(tobb_mint_ketto_testver))

nev_tobb_mint_ketto_testver = [diak['nev'] for diak in diakok if diak['testverek'] > 2]
print('Azon diákok neve, akiknek több mint 2 testvérük van:', nev_tobb_mint_ketto_testver)

print('Hány olyan diák van, akik a 2. idegen nyelvként a németet tanulják?:', len(nemet_diakok))

nev_fiu_nemet = [diak['nev'] for diak in diakok if diak['neme'] == 'F' and diak['idegen_nyelv'] == 'német']
print('Azon fiú diákok neve, akik a 2. idegen nyelvként a németet tanulják:', nev_fiu_nemet)

egyes_angol_diakok = [diak for diak in diakok if diak['angol_csoport'] == '1']
print('Hány diák tanul az egyes angol csoportban:', len(egyes_angol_diakok))

kettes_angol_diakok = [diak for diak in diakok if diak['angol_csoport'] == '2']
print('Hány diák tanul a kettes angol csoportban:', len(kettes_angol_diakok))

print('Hány diák tanul az alfa matematika csoportban:', len(alfa_diakok))

beta_diakok = [diak for diak in diakok if diak['math_info_csoport'] == 'beta']
print('Hány diák tanul az beta matematika csoportban:', len(beta_diakok))

alfa_diakok = [diak for diak in diakok if diak['math_info_csoport'] == 'alfa']
lanyok_alfa = [diak for diak in alfa_diakok if diak['neme'] == 'L']
print('Hány lány tanul az alfa matematika csoportban?:', len(lanyok_alfa))

beta_diakok = [diak for diak in diakok if diak['math_info_csoport'] == 'beta']
lanyok_beta = [diak for diak in beta_diakok if diak['neme'] == 'L']
print('Hány lány tanul a beta matematika csoportban?:', len(lanyok_beta))

fiuk_alfa = [diak for diak in alfa_diakok if diak['neme'] == 'F']
print('Hány fiú tanul az alfa matematika csoportban?:', len(fiuk_alfa))

fiuk_beta = [diak for diak in beta_diakok if diak['neme'] == 'F']
print('Hány fiú tanul a beta matematika csoportban?:', len(fiuk_beta))

orosz_diakok = [diak for diak in diakok if diak['idegen_nyelv'] == 'orosz']
if len(orosz_diakok) > 0:
print("Van olyan diák, aki a 2. idegen nyelvként oroszt tanul")
else:
print("Nincs olyan diák, aki a 2. idegen nyelvként oroszt tanul")

olasz_diakok = [diak for diak in diakok if diak['idegen_nyelv'] == 'olasz']
if len(olasz_diakok) > 0:
print("Van olyan diák, aki a 2. idegen nyelvként olaszt tanul")
else:
print("Nincs olyan diák, aki a 2. idegen nyelvként olaszt tanul")

spanyol_diakok = [diak for diak in diakok if diak['idegen_nyelv'] == 'spanyol']
if len(spanyol_diakok) > 0:
print("Van olyan diák, aki a 2. idegen nyelvként spanyolt tanul.")
else:
print("Nincs olyan diák, aki a 2. idegen nyelvként spanyolt tanul.")

legnagyobb_csalad = max([diak['csalad_tagok'] for diak in diakok])
print("A legnagyobb család az osztályban:", legnagyobb_csalad, "fő")

legtobb_testver = max([diak['testverek'] for diak in diakok])
for diak in diakok:
if diak['testverek'] == legtobb_testver:
print("Az egyik diák, aki a legtöbb testvére van:", diak['nev'])

lany_angol_egyes_ketto = [diak['nev'] for diak in diakok if diak['neme'] == 'L' and (diak['angol_csoport'] == '1' or diak['angol_csoport'] == '2')]
print("Az egyes vagy kettes angol csoportban lévő lány diákok:", lany_angol_egyes_ketto)

fiu_angol_harom_negy = [diak['nev'] for diak in diakok if diak['neme'] == 'F' and (diak['angol_csoport'] == '3' or diak['angol_csoport'] == '4') and (diak['testverek'] == 0 or diak['testverek'] == 2)]
print("A hármas vagy négyes angol csoportban lévő és 0 vagy 2 testvérük van fiú diákok:", fiu_angol_harom_negy)

nem_harom_a_kulonbseg = [diak for diak in diakok if abs(diak['csalad_tagok'] - diak['testverek']) != 3]
print('Azon családok száma, ahol az együttlakók száma és a testvérek száma között nem három a különbség:', len(nem_harom_a_kulonbseg))

dari_dora_angol_csoport = [diak for diak in diakok if diak['nev'] == 'Dári Dóra'][0]['angol_csoport']
dari_dora_angol_tarsak = [diak['nev'] for diak in diakok if diak['angol_csoport'] == dari_dora_angol_csoport and diak['nev'] != 'Dári Dóra']
print('Dári Dóra hiányzott a legutóbbi angol órán, szeretné bepótolni a hiányzást. Adja meg azon tanulók nevét, akik vele azonos angol csoportba járnak:', dari_dora_angol_tarsak)

avon_mor_angol_csoport = [diak for diak in diakok if diak['nev'] == 'Avon Mór'][0]['angol_csoport']
avon_mor_angol_tarsak = [diak['nev'] for diak in diakok if diak['angol_csoport'] == avon_mor_angol_csoport and diak['nev'] != 'Avon Mór']
print('Avon Mór hiányzott a legutóbbi angol órán, szeretné bepótolni a hiányzást. Adja meg azon tanulók nevét, akik vele azonos angol csoportba járnak:', avon_mor_angol_tarsak)

zuz_angol_csoport = [diak['nev'] for diak in diakok if diak['angol_csoport'] == 'Zúz Mara']
print('Zúz Mara angol csoportjába tartozó diákok:', zuz_angol_csoport)

print('Citad Ella angol csoportjába tartozó diákok:', citad_angol_csoport)

hat_angol_csoport = [diak['nev'] for diak in diakok if diak['angol_csoport'] == 'Hát Izsák']
print('Hát Izsák angol csoportjába tartozó diákok:', hat_angol_csoport)

spanyol_diakok = [diak for diak in diakok if diak['idegen_nyelv'] == 'spanyol']
nemet_diakok = [diak for diak in diakok if diak['idegen_nyelv'] == 'német']

if len(spanyol_diakok) > len(nemet_diakok):
print('Több diák tanul spanyol nyelvet.')
elif len(spanyol_diakok) < len(nemet_diakok):
print('Több diák tanul német nyelvet.')
else:
print('Ugyanannyian tanulják a spanyol és a német nyelvet.')

nyelv = input("Kérem adja meg azt a nyelvet, amelyiket tanuló diákjaik névsorát szeretné látni: ")
nyelv_diakok = [diak for diak in diakok if diak['idegen_nyelv'] == nyelv]
print("Az adott nyelvet tanuló diákjaik névsorát:")
for diak in nyelv_diakok:
print(diak['nev'])

osszes_idegen_nyelv = set([diak['idegen_nyelv'] for diak in diakok])
print("Az összes különböző második idegen nyelv száma:", len(osszes_idegen_nyelv))

osszes_matematika_info_csoport = set([diak['math_info_csoport'] for diak in diakok])
print("Az összes különböző matematika/informatika szerinti csoportbontás nevei:")
for csoport in osszes_matematika_info_csoport:
print(csoport)

angol_csoportok = set([diak['angol_csoport'] for diak in diakok])
print("Az angol nyelvi csoportokban járó diákok száma:")
for angol_csoport in angol_csoportok:
csoport_diakok = [diak for diak in diakok if diak['angol_csoport'] == angol_csoport]
print(f"{angol_csoport}: {len(csoport_diakok)}")

math_info_csoportok = set([diak['math_info_csoport'] for diak in diakok])
print('A matematika/informatika csoportbontások:', ', '.join(math_info_csoportok))

testverek = [diak['testverek'] for diak in diakok]
leggyakoribb_testver_szam = max(set(testverek), key=testverek.count)
print('A leggyakrabban előforduló testvérszám:', leggyakoribb_testver_szam)

angol_csoportok = set([diak['angol_csoport'] for diak in diakok])
angol_csoport_testverek = {angol_csoport: 0 for angol_csoport in angol_csoportok}
for diak in diakok:
angol_csoport_testverek[diak['angol_csoport']] += diak['testverek']

for angol_csoport, testver_szam in angol_csoport_testverek.items():
print(f'Az "{angol_csoport}" angol csoportban összesen {testver_szam} testvér van.')

idegen_nyelvek = set([diak['idegen_nyelv'] for diak in diakok])
idegen_nyelv_csoport_testverek = {idegen_nyelv: [] for idegen_nyelv in idegen_nyelvek}
for diak in diakok:
idegen_nyelv_csoport_testverek[diak['idegen_nyelv']].append(diak['testverek'])

for idegen_nyelv, testver_szamok in idegen_nyelv_csoport_testverek.items():
atlagos_testver_szam = sum(testver_szamok) / len(testver_szamok)
print(f'A(z) "{idegen_nyelv}" nyelv csoportban átlagosan {atlagos_testver_szam} testvér van.')

angolcsoportok = {}
for diak in diakok:
angol_csoport = diak['angol_csoport']
if angol_csoport not in angolcsoportok:
angolcsoportok[angol_csoport] = []
angolcsoportok[angol_csoport].append(diak['nev'])
for angol_csoport, nevek in angolcsoportok.items():
elso_nev = nevek[0]
utolso_nev = nevek[-1]
print(f"Angolcsoport: {angol_csoport}, Első diák neve: {elso_nev}, Utolsó diák neve: {utolso_nev}")
