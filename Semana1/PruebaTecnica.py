def valores(n):
    
    if n>>0:
        print ("Valor positivo: ",n)
    elif n<0:
        print ("Valor negativo: ",n)
    else:
        print ("Valor Cero:" ,n)

def pares(n):
    if n%2==0:
        print("Par")
    elif  n%2!=0:
        print("Impar")


def primo(n):
    cont=0
    for i in range(2,n):
        if n%i==0:
               cont+=1
    if cont==1:
        print("Primo")
    else:
        print("No es Primo")

def fibonacci(n):
    a=0
    b=1

    while a!=n:
        c=a+b
        a=b
        b=c
    if a==n:
        print (n,"Pertenece a Fibonacci")
    else:
        print (n,"NO pertenece a Fibonacci")
     
def intermedios(a,b):
    suma=0
    for i in range(a+1,b):
          suma+=i       
    return suma

def elevaciones(n):
    if n%2==0:
        print(n**2)
    else:
        print(n**3)
     
def main():
       


    print("-----------------Eleccion-----------------")
    c=int(input("Escoja el punto a revisar Forma numerica: "))

    if c != 5 and c != 8 and c != 9 and c != 10:
        n=int(input("Ingrese un UNICO valor NUMERICO: "))
        
        if c==1:
            print(valores(n))
            
        elif c==2:
            print(pares(n))
        elif c==3:
            print(fibonacci(n))
            
        elif c==4:
            print(primo(n))

        elif c==6:
            print(elevaciones(n))

        elif c==7:
            (valores(n))
            (pares(n))
            (primo(n))
            (fibonacci(n))
            (elevaciones(n))
           

   

    elif c==5:
        a=int(input("Ingrese un primer valor NUMERICO: "))
        b=int(input("Ingrese un segundo valor NUMERICO: "))
        suma=intermedios(a,b)
        print(suma)
        
    elif c==8 or c==9 or c==10 :
        f=input("Ingrese su fecha de nacimiento con su codifo, EJEMPLO:2-diciembre20000016784:  ")
        pal=""
        for i in f:
            if i.isalpha():
                pal+=i
        print("Mes de nacimiento: ",pal)
        vocales=["a", "e", "i", "o", "u"]

        abe = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "ñ", "o", "p", "q","r", "s", "t", "u", "v", "w", "x", "y", "z"]

        exi=[]
        cons=[]
        for i in pal:
            if i in vocales:
                 exi.append(i)
            else:
                cons.append(i)
        pocisiones=[]
        mes=[]
        for i in pal:
            for j in range(len(abe)):
                if i== abe[j]:
                    pocisiones.append(j+1)
                    mes.append(i)

        print(pocisiones) 
        print(mes)         
        print("VOCALES: ",exi)
        print("CONSONANTES",cons)
main()
