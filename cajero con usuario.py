def bdp_cajero():
    # Base de datos simulada de usuarios (ID: PIN, Saldo)
    usuarios_registrados = {
        "1020": {"pin": "1234", "saldo": 1000.0},
        "5060": {"pin": "4321", "saldo": 2500.0}
    }
    intentos = 3

    print("=== BIENVENIDO AL CAJERO AUTOMÁTICO ===")
    
    # 1. Validación de Identificación de Usuario
    while True:
        id_usuario = input("Ingrese su identificación de usuario (4 dígitos): ")
        
        # Validar longitud y que sean solo números
        if len(id_usuario) == 4 and id_usuario.isdigit():
            if id_usuario in usuarios_registrados:
                break
            else:
                print("Usuario no encontrado. Intente de nuevo.\n")
        else:
            print("Error: La identificación debe ser exactamente de 4 números.\n")

    # Guardar datos del usuario activo
    datos_usuario = usuarios_registrados[id_usuario]
    pin_correcto = datos_usuario["pin"]
    saldo = datos_usuario["saldo"]

    # 2. Sistema de autenticación por PIN
    while intentos > 0:
        pin_ingresado = input(f"Usuario {id_usuario}, ingrese su PIN: ")
        
        if pin_ingresado == pin_correcto:
            print("\nAcceso concedido.")
            break
        else:
            intentos -= 1
            print(f"PIN incorrecto. Intentos restantes: {intentos}")
            if intentos == 0:
                print("Tarjeta bloqueada por seguridad. Contacte a su banco.")
                return

    # 3. Bucle principal de operaciones
    while True:
        print(f"\n--- MENÚ (Usuario: {id_usuario}) ---")
        print("1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            print(f"\nSu saldo actual es: ${saldo:.2f}")
            
        elif opcion == "2":
            try:
                deposito = float(input("\nIngrese la cantidad a depositar: $"))
                if deposito > 0:
                    saldo += deposito
                    print(f"Depósito exitoso. Nuevo saldo: ${saldo:.2f}")
                else:
                    print("Error: El monto debe ser mayor a cero.")
            except ValueError:
                print("Error: Ingrese un número válido.")
                
        elif opcion == "3":
            try:
                retiro = float(input("\nIngrese la cantidad a retirar: $"))
                if retiro > saldo:
                    print("Error: Fondos insuficientes.")
                elif retiro <= 0:
                    print("Error: El monto debe ser mayor a cero.")
                else:
                    saldo -= retiro
                    print(f"Retiro exitoso. Nuevo saldo: ${saldo:.2f}")
            except ValueError:
                print("Error: Ingrese un número válido.")
                
        elif opcion == "4":
            print("\nGracias por utilizar nuestros servicios. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    bdp_cajero()