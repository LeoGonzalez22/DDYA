def vueltas_monedas(monedas, vueltas):
    if vueltas == 0:
        return 0
    q = float('inf')
    for moneda in monedas:
        if moneda <= vueltas:
            q = min(q, 1 + vueltas_monedas(monedas, vueltas - moneda))
    return q
def memoized_vueltas(monedas, vueltas):
    r = [float('inf')] * (vueltas + 1)
    r[0] = 0
    for cantidad in range(1, vueltas + 1):
        for moneda in monedas:
            if moneda <= cantidad:
                r[cantidad] = min(r[cantidad], 1 + r[cantidad - moneda])
    return r[vueltas]
monedas = [50, 100, 200, 500, 1000]
try:
    cambio = int(input("Ingrese el valor numérico del cambio: "))
    if cambio <= 0:
        print("Por favor ingrese un valor positivo.")
    else:
        print("El cambio es:", cambio)
        cantidad = memoized_vueltas(monedas, cambio)
        if cantidad == float('inf'):
            print("No es posible entregar el cambio exacto.")
            print("Por favor ingrese otro valor.")
        else:
            print("Cantidad mínima de monedas:", cantidad)
except ValueError:
    print("Por favor ingrese un valor numérico.")
