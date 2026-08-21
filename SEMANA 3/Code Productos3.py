def merge(tab, p, q, r):
    L = tab[p:q+1]
    R = tab[q+1:r+1]
    
    i = 0
    j = 0
    for k in range(p, r + 1):
        if i < len(L) and (j >= len(R) or L[i] <= R[j]):
            tab[k] = L[i]
            i = i + 1
        else:
            tab[k] = R[j]
            j = j + 1
 
 
def merge_sort(tab, p, r):
    if p < r:
        q = (p + r) // 2
 
        merge_sort(tab, p, q)
        merge_sort(tab, q + 1, r)
        merge(tab, p, q, r)

def binary_search_desc(tab, x):
    lo, hi = 0, len(tab) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if tab[mid] == x:
            return mid
        elif tab[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return None
 
 
def main():
    n = int(input("Cantidad de productos (Valor NUMERICO entero): "))
 
    if n < 0:
        print("Valor no Valido")
    else:
        print("Valor valido, Valor guardado")
    tab = []
    for i in range(n):
        cod = int(input("Valor producto: "))
        tab.append(cod)
    merge_sort(tab, 0, len(tab) - 1)
 
    print("Lista ordenada de menor a mayor:")
    print(tab)
    x = int(input("Ingrese el valor a buscar: "))
    res = binary_search_desc(tab, x)
    print(f"El codigo del producto se encuentra en la posicion {res} de la lista")
 
 
main()
