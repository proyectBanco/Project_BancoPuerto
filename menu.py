from cliente import cargarCliente, listarClientes

from cliente import cargarCliente
from logs import Log

log = Log()


def menu():

    while True:

        print("1) Cargar Datos Cliente")
        print("2) Consultar cuenta Deposito")
        print("3) Listar clientes cargados")
        print("4) Salir")

        opt = input("Introduce la opción deseada: ")

        if opt == "1":
            cargarCliente("movimientos")

        elif opt == "2":
            cliente = cargarCliente("guardado")
            if cliente is not None:
                log.escribir(
                    "INFO", f"CONSULTA DATOS CLIENTE CON NÚMERO: {cliente.numero}"
                )
                print(f"Cliente: {cliente.numero}")
                print(f"Saldo cuenta: {cliente.cuenta.saldo} €")
                print(f"Saldo depósito: {cliente.deposito.saldo} €")
                print(f"Saldo total: {cliente.getSaldoTotal()} €")
            else:
                print("No se puede mostrar la consulta de ese cliente")

        elif opt == "3":
            clientes = listarClientes()
            if clientes:
                print("Clientes cargados:\n")
                for numero in clientes:
                    print(f"- {numero}")
            else:
                print("No hay clientes cargados")
            log.escribir("INFO", f"LISTADO DE CLIENTES CARGADOS: {len(clientes)}")

        elif opt == "4":
            log.escribir("INFO", "FIN EJECUCIÓN")
            print("Hasta pronto")
            break

        else:
            log.escribir(
                "WARNING", "SE HA INTRODUCIDO UNA OPCION EN EL MENÚ NO RECONOCIDA"
            )
            print("No se ha seleccionado ninguna opción correcta")
