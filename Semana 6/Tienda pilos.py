def cantidad(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Valor no valido, intentelo de nuevo.")


def mostrar_clientes(clientes):
    if len(clientes) == 0:
        print("No hay clientes esperando.")
    else:
        print("Clientes esperando:", " -> ".join(clientes))


def agr_cliente(clientes):
    nuevo = input("Ingrese el nuevo cliente: ")
    clientes.append(nuevo)
    print("Cliente agregado.")
    mostrar_clientes(clientes)


def atend_cliente(clientes, atendidos):
    if len(clientes) == 0:
        print("No hay clientes esperando.")
    else:
        cliente = clientes.pop(0)      # dequeue
        atendidos.append(cliente)      # push

        print("Atendiendo a:", cliente)
        mostrar_clientes(clientes)


def mostrar_ultimo_atendido(atendidos):
    if len(atendidos) == 0:
        print("No hay clientes atendidos.")
    else:
        print("Ultimo cliente atendido:", atendidos[-1])   # peek


def eliminar_at(clientes, atendidos):
    if len(atendidos) == 0:
        print("No hay atenciones para deshacer.")
    else:
        ultimo = atendidos.pop()       # pop
        clientes.insert(0, ultimo)

        print("Se deshizo la atencion de:", ultimo)
        print("Pila de atendidos:", atendidos)
        mostrar_clientes(clientes)


def agregar_producto(productos):
    codigo = cantidad("Ingrese el codigo: ")

    for i in range(len(productos)):
        if productos[i][0] == codigo:
            print("Ya existe un producto con ese codigo.")
            return

    nombre = input("Ingrese el nombre: ")
    precio = cantidad("Ingrese el precio: ")

    producto = [codigo, nombre, precio]
    productos.append(producto)

    print("Producto agregado.")


def mostrar_productos_normal(productos):
    if len(productos) == 0:
        print("No hay productos.")
    else:
        print("Productos del primero al ultimo:")

        for i in range(len(productos)):
            print(productos[i][0], "-", productos[i][1], "- $", productos[i][2])


def mostrar_productos_reves(productos):
    if len(productos) == 0:
        print("No hay productos.")
    else:
        print("Productos del ultimo al primero:")

        for i in range(len(productos) - 1, -1, -1):
            print(productos[i][0], "-", productos[i][1], "- $", productos[i][2])


def buscar_producto(productos):
    codigo = cantidad("Ingrese el codigo que desea buscar: ")
    encontrado = False

    for i in range(len(productos)):
        if productos[i][0] == codigo:
            print("Producto encontrado:")
            print(productos[i][0], "-", productos[i][1], "- $", productos[i][2])
            encontrado = True
            break

    if encontrado == False:
        print("Producto no encontrado.")


def eliminar_producto(productos):
    codigo = cantidad("Ingrese el codigo que desea eliminar: ")
    encontrado = False

    for i in range(len(productos)):
        if productos[i][0] == codigo:
            productos.pop(i)
            encontrado = True
            print("Producto eliminado.")
            break

    if encontrado == False:
        print("Producto no encontrado.")


clientes = []
atendidos = []
productos = []

n = cantidad("Numero de clientes: ")

for i in range(n):
    c = input("Ingrese el nombre del cliente: ")
    clientes.append(c)


while True:
    print("\nMENU")
    print("1. Agregar cliente")
    print("2. Atender cliente")
    print("3. Mostrar clientes esperando")
    print("4. Mostrar ultimo cliente atendido")
    print("5. Deshacer ultima atencion")
    print("6. Agregar producto")
    print("7. Mostrar productos del primero al ultimo")
    print("8. Mostrar productos del ultimo al primero")
    print("9. Buscar producto")
    print("10. Eliminar producto")
    print("0. Salir")

    opcion = cantidad("Seleccione una opcion: ")

    if opcion == 1:
        agr_cliente(clientes)

    elif opcion == 2:
        atend_cliente(clientes, atendidos)

    elif opcion == 3:
        mostrar_clientes(clientes)

    elif opcion == 4:
        mostrar_ultimo_atendido(atendidos)

    elif opcion == 5:
        eliminar_at(clientes, atendidos)

    elif opcion == 6:
        agregar_producto(productos)

    elif opcion == 7:
        mostrar_productos_normal(productos)

    elif opcion == 8:
        mostrar_productos_reves(productos)

    elif opcion == 9:
        buscar_producto(productos)

    elif opcion == 10:
        eliminar_producto(productos)

    elif opcion == 0:
        print("Programa finalizado.")
        break

    else:
        print("Opcion no valida.")