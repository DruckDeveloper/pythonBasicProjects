asignaturas=[]
asig=str(input("escribe una asignatura (no para finalizar):")) 
while asig !="no": 
    asignaturas.append(asig)
    asig=str(input("escribe una asignatura (no para finalizar):"))

notas=[]
valor=int(input("Ingresa tu nota (-1 para finalizar):"))
while valor!=-1:
    notas.append(valor)
    valor=int(input("Ingresar valor (-1 para finalizar):"))

print("tus asgnaturas son: ", asignaturas, "tus notas son: ", notas) 
