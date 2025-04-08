#Archivo: tres_valores.py
#Fecha: 08/04/2025
#Proy: estudio de algoritmos

#Ordenar crecientemente una lista de tres valores
#Existe un error, ya que según los valores,puede cambiar
#Dos de entre ellos había quecambiar, pero genera mal orden
#En los posteriores

n = [252, 14, 58] 

#Bucle para tomar datos del teclado y guardarlos en la variable n de tipo lista
def swap(j):
  a = n[j] 
  n[j]= n[j + 1]
  n[j+1] = a



for i  in range(len(n)-2):    
    for j in range(len(n)-1):
        if n[j] > n[j + 1]:
            swap(j)

print(n)