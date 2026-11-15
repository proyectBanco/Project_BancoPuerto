from models import Cliente
from logs import Log

log = Log()

def cargarCliente(tipo):
    while True:
        num = input("Introduce el número de cliente: ")

        if len(num) != 6 or not num.isdigit():
            print("El formato introducido no es correcto")
            continue

        if tipo == "movimientos":
            return leerFichero(num)

        elif tipo == "guardado":
            return cargarClienteGuardado(num)


def leerFichero(numCliente):

    # Añadido para Tarea 2: registrar el inicio de la carga
    log.escribir("INFO", f"INICIO CARGA DEL CLIENTE {numCliente}")

    cliente = Cliente(numCliente)

    try:
        with open(f"ficherosClientes/{numCliente}.txt", "r") as f:

            for numLinea, linea in enumerate(f, start=1):

                for grupo in linea.strip().split():

                    datos = grupo.split(";")

                    try:
                        cantidad = float(datos[0])
                        operacion = datos[1]
                        destino = datos[2]
                    except (ValueError, IndexError):
                        log.escribir(
                            "ERROR",
                            f"CLIENTE {numCliente}: LÍNEA {numLinea} INCORRECTA, "
                            f"SE IGNORA EL MOVIMIENTO -> '{grupo}'"
                        )
                        continue

                    if destino == "Cuenta" and operacion == "Ingreso":
                        cliente.cuenta.ingresar(cantidad)

                    elif destino == "Cuenta" and operacion == "Retirada":
                        cliente.cuenta.retirar(cantidad)

                    elif destino == "Deposito" and operacion == "Ingreso":
                        cliente.deposito.ingresar(cantidad)

                    elif destino == "Deposito" and operacion == "Retirada":
                        cliente.deposito.retirar(cantidad)

        cliente.guardar()

        print("Datos del cliente cargados correctamente")

        log.escribir("INFO", f"CLIENTE {numCliente} CARGADO CORRECTAMENTE")

        print(f"Cliente: {cliente.getNumero()}")
        print(f"Saldo cuenta: {cliente.getCuenta().getSaldo()} €")
        print(f"Saldo depósito: {cliente.getDeposito().getSaldo()} €")

        return cliente

    except FileNotFoundError:
        print("El usuario no tiene ninguna cuenta con el banco")
        log.escribir(
            "ERROR",
            f"NO EXISTE EL FICHERO DE MOVIMIENTOS DEL CLIENTE {numCliente}"
        )
        return None


def cargarClienteGuardado(numCliente):

    try:
        with open(f"datosClientes/{numCliente}.txt", "r") as f:

            datos = f.read().split(";")

            cliente = Cliente(datos[0])

            cliente.cuenta.saldo = float(datos[1])
            cliente.deposito.saldo = float(datos[2])

            return cliente

    except FileNotFoundError:
        print("Primero tienes que cargar los datos de este cliente")
        log.escribir(
            "ERROR",
            f"INTENTO DE CONSULTA DEL CLIENTE {numCliente} QUE NO HA SIDO CARGADO"
        )
        return None