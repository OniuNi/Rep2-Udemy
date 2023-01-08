print("Bine ai venit pe Insula Comorilor!")
print("Misiunea ta este sa gasesti cufarul care contine comoara.")

# 'You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.'
# "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?"
# "It's a room full of fire. Game Over."
# "You found the treasure! You Win!"
# "You enter a room of beasts. Game Over."
# "You chose a door that doesn't exist. Game Over."
# "You get attacked by an angry trout. Game Over."
# "You fell into a hole. Game Over."

print("Te afli la o intersectie. In ce directie vrei sa o iei? Alege intre stanga si dreapta.")

directie_intersectie = input("Directia aleasa de tine: ")

if(directie_intersectie == "stanga"):
  print("Ai ajuns la lac. Exista o insula in mijlocul lacului. Daca vrei sa astepti o barca, tasteaza \"asteapta\". Daca vrei sa pornesti inotand catre insula, tasteaza 'inoata'.")
  alegere_lac = input("Alegerea ta este: ")
  if(alegere_lac == "asteapta"):
    print("Ai ajuns pe insula. Aici se afla o casa cu trei usi. O usa este rosie, una este galbena, iar cealalta este albastra. Ce culoare alegi?")
    culoare_usa = input("Culoarea usii tale este (albastra/ rosie/ galbena): ")
    if(culoare_usa == 'albastra'):
      print("Ai fost mancat de un leu. Game over!")
    elif(culoare_usa == 'galbena'):
      print("Ai castigat! Ai gasit cufarul!")
    elif(culoare_usa == 'rosie'):
      print("Ai nimerit in camera de foc. Game over!")
    else:
      print("Game over!")
  else:
    print("Ai fost atacat. Game over!")
else:
  print("Ai cazut intr-o groapa. Game over!")