# Configuramos los datos iniciales de la cuenta
clave_correcta = "2011"
saldo = 75000 # Empezamos con 75000 mil pesos en saldo
historial_movimientos = ["saldo inicial: 75000"]
print("=== BIENVENIDA/O A TU BANCO DIGITAL ===")
# Paso 1: Validación de Seguridad
intentos_clave = 0
bloqueado = False
while intentos_clave < 3:
    clave_ingresada = input("Introduce tu clave secreta de 4 digitos: ")
    if clave_ingresada == clave_correcta:
        print("¡Clave correcta! Accediendo a tu cuenta...\n")
        break
    else:
        intentos_clave = intentos_clave + 1
        print(f"Clave incorrecta. Te quedan {3 - intentos_clave} intentos.")
        if intentos_clave == 3:
            bloqueado = True
# Si falló 3 veces, el programa termina aquí
if bloqueado:
    print("Tarjeta bloqueada por seguridad. Acércate a una sucursal")
    exit()
    # Paso 2 Menú de operaciones Bancarias
while True:
     print("--- MENÚ DE OPERACIONES ---")
     print("1. Consultar saldo")
     print("2. Depositar dinero")
     print("3. Retirar dinero")
     print("4. Ver historial de movimientos")
     print("5. Salir")
     opcion = input("Elige un número (1-5): ")
     if opcion == "1":
         print(f"\nTu saldo actual es de: ${saldo}\n")
     elif opcion == "2":
         monto_deposito = int(input("¿Cuánto dinero deseas depositar?: $"))
         saldo = saldo + monto_deposito
         historial_movimientos.append(f"Deposito de: +${monto_deposito}")
         print(f"¡Deposito exitoso! Nuevo saldo: ${saldo}\n")
     elif opcion == "3":
         monto_retiro = int(input(f"¿Cuánto dinero desea retirar?: $"))
         if monto_retiro > saldo:
             print("Error: Fondos insuficientes.\n")
         else:
             saldo = saldo - monto_retiro
             historial_movimientos.append(f"Retiro de: -${monto_retiro}")
             print(f"¡Retiro exitoso! Retira tu dinero. Nuevo saldo: ${saldo}\n")
     elif opcion == "4":
         print("\n--- HISTORIAL DE MOVIMIENTOS ---")
         for movimientos in historial_movimientos:
             print(f"- {movimientos}")
         print("---------------------------------\n")
     elif opcion == "5":
         print("Gracias por elegir usar nuestro banco. ¡Que tengas un buen día!")
         break
     else:
         print("Opción no válida. Intenta otra vez.\n")