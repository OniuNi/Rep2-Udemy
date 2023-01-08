# Se citesc două numere naturale n1 şi n2.
# Se cere să se calculeze câtul şi restul împărţirii întregi ale celor două numere, fără a utiliza operatori de împărţire. Indicație.
# Aşa cum înmulţirea se poate face prin adunare repetată, tot aşa împărţirea se poate face prin scădere repetată...
nr1 = int(input("primul numar este:"))
nr2 = int(input("al doilea numar este:"))
conditie = True
cat = 0
rest = 0
while conditie:
    if nr1 - nr2 >= 0:
        cat += 1
        nr1 -= nr2
    else:
        rest = nr1
        conditie = False
print (cat, rest)