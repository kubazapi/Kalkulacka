while True:
  print("Vítej v kalkulačce")
  cislo1 = float(input("Zadej číslo: "))
  cislo2 = float(input("Zadej číslo: "))
  operace = input("Zadej operaci: ")
  if operace == "+":
    print(cislo1 + cislo2)
  elif operace == "-":
    print(cislo1 - cislo2)
  elif operace == "*":
    print(cislo1 * cislo2)
  elif cislo2 == 0 and operace == "/":
    print("Nulou nelze dělit")
  elif operace == "/":
    print(cislo1 / cislo2)
  elif operace == "**":
    print(cislo1 ** cislo2)
  elif operace == "//":
    print(cislo1 // cislo2)
  else:
    print("Zadaná hodnota je nesprávná")
  pokracovat = input("Chceš pokračovat? (ano/ne): ")
  if pokracovat == "ne":
    print("Děkuji za použití kalkulačky")
    break