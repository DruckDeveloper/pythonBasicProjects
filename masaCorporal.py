print("El siguiente programa calculara tu indice de masa corporal (imc)")
peso = float(input("ingresa tu peso en KG? ")) 
altura = float(input("ingresa tu estatura en metros "))

altura2 = altura * altura
imc = peso / altura2
print("Tu indice de masa corporal es de: " ,imc)
