revision = 1

while revision < 6:
    hay_combustible = input("¿Hay combustible?: ").lower()
    if hay_combustible == "si":
        print("Todo correcto!")
    elif hay_combustible == "no":
        print("Cuidaaadoooooooo! Llena tanque combustible")
    revision = revision + 1

