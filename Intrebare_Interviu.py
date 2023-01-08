# #jocul FizzBuzz
# Instructiuni
# Vei scrie un numar care va da raspunsul automat la joaca FizzBuzz
#
# Programul trebuie sa functioneze pe un range de la 1 la 100 inclusiv
#
# Cand numarul este divizibil cu 3, in lod de numar, trebuie sa fie printat "Fizz"
#
# Cand numarul este divizibil cu 5, in loc de numar trebuie sa fie printat "Buzz"
#
# Si daca numarul este divizibil si cu 3 si cu 5, in loc de numar trebuie sa fie printat "FizzBuzz"

numar = 0

for numar in range(1, 100 + 1):
    if numar % 3 ==0 and numar % 5 ==0:
        print("FizzBuzz")
    elif numar % 5 ==0:
        print("Buzz")
    elif numar % 3 ==0:
        print("Fizz")
    else:
        print(numar)
