# Instrucțiuni Scrieți un program care adaugă cifrele într-un număr de 2 cifre.
# de exemplu. dacă intrarea a fost 35, atunci ieșirea ar trebui să fie 3 + 5 = 8
#
# Avertizare. Nu modificați codul de pe rândurile 1-3.
# Programul dvs. ar trebui să funcționeze pentru diferite intrări.
# de exemplu. orice număr din două cifre.
#
# Exemplu de intrare 39 Exemplu de ieșire 3 + 9 = 12

two_digit_number = input("Scrie un numar de 2 cifre: ")
suma = int(two_digit_number[0]) + int(two_digit_number[1])
print(suma)