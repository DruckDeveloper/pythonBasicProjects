frase = input("Escriba una frase: ")
letra = input("Escriba una letra: ")
counter=0
for x in frase:
    if(x == letra):
        counter+=1
print("La letra {} se menciona: {} veces".format(letra,counter))
