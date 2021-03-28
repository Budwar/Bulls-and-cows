# Tvým úkolem bude vytvořit program, který by simuloval hru Bulls and Cows.
# Po vypsání úvodního textu uživateli, může hádání tajného čtyřciferného čísla začít.
#
# Program bude obsahovat:
# Program pozdraví užitele a vypíše úvodní text
# Program dále vytvoří tajné 4místné číslo (číslice musí být unikátní a nesmí začínat 0)
# Hráč hádá číslo. Program jej upozorní, pokud zadá číslo kratší nebo delší než 4 čísla,
# pokud bude obsahovat duplicity, začínat nulou, příp. obsahovat nečíselné znaky
# Program vyhodnotí tip uživatele
# Program dále vypíše počet bull/ bulls (pokud uživatel uhodne jak číslo, tak jeho umístění),
# # příp. cows/ cows (pokud uživatel uhodne pouze číslo, ale ne jeho umístění).
# # Vrácené ohodnocení musí brát ohled na jednotné a množné číslo ve výstupu. Tedy 1 bull a 2 bulls (stejně pro cow/cows).


import random

#vytvoření funkce hádání
#Program uživatele upozorní, pokud zadá číslo kratší nebo delší než 4 čísla,
# pokud bude obsahovat duplicity, začínat nulou, příp. obsahovat nečíselné znaky
def hadani(cislo):
    bulls = 0
    cows = 0
    if len(cislo) != 4 or str(cislo)[0] == "0" or not cislo.isdigit() or len(set(cislo)) != 4:
      return "Číslo musí obsahovat přesně 4 číslice, nesmí začínat nulou a obsahovat nečíselne znaky a duplicity."

    else:
        for i,znak in enumerate(cislo):
            if znak in tajne_cislo:
                if i == tajne_cislo.index(znak):
                    bulls += 1
                else:
                    cows += 1

        return "{} {}".format(bulls, "bull" if bulls == 1 else "bulls") + ", {} {}".format(cows, "cow" if cows == 1 else "cows")



#Program pozdraví užitele a vypíše úvodní text
oddelovac = 47 * "-"
print(f"Hi there!"
      f"\n{oddelovac}"
      f"\nI´ve generated a random 4 digit number for you."
      f"\nLet´s play Bulls and Cows game!"
      f"\n{oddelovac}")

#Program vytvoří tajné 4místné číslo (číslice musí být unikátní a nesmí začínat 0)
tajne_cislo = ""
while len(tajne_cislo) != 4:
    nahodne_cislo = str(random.randint(0,9))
    if nahodne_cislo in tajne_cislo or (nahodne_cislo == "0" and len(tajne_cislo) == 0):
        continue
    tajne_cislo += nahodne_cislo



#Hráč hádá číslo
#i - počítání pokusů

uzivatel_cislo = input("Enter a number: ")
i = 1
while tajne_cislo != uzivatel_cislo:
    i += 1
    print(oddelovac)
    print(hadani(uzivatel_cislo))
    uzivatel_cislo = input()

print("Correct, you've guessed the right number\nin {} {}!".format(i, "guess" if i == 1 else "guesses"))


if i <= 4:
    print("That´s amazing!")
elif i > 4 and i <= 8:
    print("That´s avarage.")
elif i > 8 and i <= 16:
    print("That´s not so good.")
else:
    print("That´s horrible")