

num=int(input("Digite cuantos numeros desea registrar: "))

mul2=0
mul3=0

for i in range(n):
    v=int(input('Digite un numero a almacenar'))
    if v%2==0:
       mul2+=1
    elif v%3==0:
        mul3+=1;

print(f"La cantidad de multiplos de 2 es: {mul2} y de 3 es: {mul3}")