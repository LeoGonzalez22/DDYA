red = {
    "Ana": ["Carlos", "Laura"], "Carlos": ["Ana", "Mateo", "Sofia"],"Laura": ["Ana", "Daniel"],}

red2 = {"Ana": ["Carlos", "Laura"], "Carlos": ["Ana", "Mateo", "Sofia"], "Laura": ["Ana", "Daniel"], 
        "Mateo": ["Carlos"],"Sofia": ["Carlos", "Valentina"],"Daniel": ["Laura", "Valentina"],"Valentina": ["Sofia", "Daniel"],}


def mostrar(red):
    for usu in red:
        print(usu, ":", ", ".join(red[usu]))


def bfs(red, ini):
    cola = [(ini, 0)]
    visitadas = []

    while cola:
        usu, nivel = cola.pop(0)

        if usu not in visitadas:
            visitadas.append(usu)
            print(usu, "nivel:", nivel)

            for amistad in red[usu]:
                if amistad not in visitadas:
                    cola.append((amistad, nivel + 1))


def dfs(red, usu, visitadas):
    visitadas.append(usu)
    print(usu, end="")

    for amistad in red[usu]:
        if amistad not in visitadas:
            print(" -> ", end="")
            dfs(red, amistad, visitadas)


def busconex(red, ini, fin):
    cola = [[ini]]
    visitadas = [ini]

    while cola:
        ruta = cola.pop(0)
        usu = ruta[-1]

        if usu == fin:
            return ruta

        for amistad in red[usu]:
            if amistad not in visitadas:
                visitadas.append(amistad)
                cola.append(ruta + [amistad])

    return None


def agregar_usuario(red, nueva, conexiones):
    if not nueva:
        print("Tiene que haber nombre")
        return False

    if nueva in red:
        print("Este usuario ya existe")
        return False

    if len(conexiones) < 2:
        print("Debes conectarlo con al menos dos usuarios")
        return False

    for conexion in conexiones:
        if conexion not in red:
            print("El usuario", conexion, "no existe en la red")
            return False

    red[nueva] = []
    for conexion in conexiones:
        if conexion not in red[nueva]:
            red[nueva].append(conexion)
        if nueva not in red[conexion]:
            red[conexion].append(nueva)

    return True


def leer_usu(mensaje, red):
    while True:
        usu = input(mensaje).strip().title()
        if usu in red:
            return usu
        print("El usuario no existe, intentelo de nuevo")


def main():
    while True:
        print("------------------------------- ELECCION -------------------------------")
        print("1) Visualizacion lista de adyacencia")
        print("2) Visualizacion BFS desde Ana")
        print("3) Visualizacion DFS desde Ana")
        print("4) Elegir usuario de ini para BFS y DFS")
        print("5) Buscar la ruta mas corta entre dos usuarios")
        print("6) Agregar una usuario nueva")

        try:
            eleccion = int(input("Ingrese el numero correspondiente a su eleccion: "))
        except ValueError:
            print("Debe ingresar un numero entero del 1 al 6")
            continue

        if eleccion == 1:
            mostrar(red2)

        elif eleccion == 2:
            bfs(red2, "Ana")

        elif eleccion == 3:
            dfs(red2, "Ana", [])
            print()

        elif eleccion == 4:
            ini = leer_usu("Ingrese el usuario inicial: ", red2)
            print("Recorrido BFS desde", ini, ":")
            bfs(red2, ini)
            print("-----------------------------------------------------------------------")
            print("Recorrido DFS desde", ini, ":")
            dfs(red2, ini, [])
            print()

        elif eleccion == 5:
            ini = leer_usu(" Usuario de inicio: ", red2)
            fin = leer_usu(" Usuario de destino: ", red2)
            ruta = busconex(red2, ini, fin)

            if ruta is not None:
                print("Ruta encontrada:")
                print(" -> ".join(ruta))
                print("Cantidad de conexiones:", len(ruta) - 1)
            else:
                print("No existe.")

        elif eleccion == 6:
            nueva = input("Nuevo usuario: ").strip().title()
            conexiones = []

            while len(conexiones) < 2:
                conexion = leer_usu("Conectar con una usuario existente: ", red2)
                if conexion in conexiones:
                    print("Ya ingresaste esa conexion, escoja otra")
                else:
                    conexiones.append(conexion)

            if agregar_usuario(red2, nueva, conexiones):
                print("Usuario agregado. red actualizada:")
                mostrar(red2)

                print("BFS desde Ana:")
                bfs(red2, "Ana")

                print("DFS desde Ana:")
                dfs(red2, "Ana", [])
                print()

                ini = leer_usu(" Usuario de inicio para buscar una ruta: ", red2)
                fin = leer_usu(" Usuario de destino: ", red2)
                ruta = busconex(red2, ini, fin)

                if ruta is not None:
                    print("Ruta encontrada:")
                    print(" -> ".join(ruta))
                    print("Cantidad de conexiones:", len(ruta) - 1)
                else:
                    print("No existe una ruta entre esos usuarios")

        else:
            print("Opcion no valida. Elija un numero del 1 al 6")

main()
