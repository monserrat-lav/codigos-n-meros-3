simulador de cajero digital

Este es un sistema bancario interactivo por consola que desarrollé en mi segundo día aprendiendo a programar en Python a los 15 años. El proyecto combina lógica de seguridad, control de flujos y gestión de datos en tiempo real.

Características del Programa

-Validación de Seguridad: El sistema solicita una clave secreta de 4 dígitos (2011) y cuenta con un límite de 3 intentos. Si se falla tres veces, la tarjeta se bloquea por seguridad y el programa se detiene.
-Menú Interactivo: Un bucle continuo que permite al usuario elegir entre 5 opciones diferentes sin que el programa se cierre automáticamente.
-Consulta de Saldo: Muestra los fondos disponibles en la cuenta en cualquier momento.
-Depósitos: Permite ingresar dinero, actualiza el saldo de forma matemática e imprime una confirmación.
-Retiros con Validación: Permite retirar fondos, verifica si hay dinero suficiente para evitar saldos negativos y actualiza la cuenta.

 Cómo Probar el Código

1. Descarga o clona este repositorio.
2. Ejecuta el archivo desde tu terminal:
   ```bash
   python cajero.py
   ```
3. Introduce la clave por defecto: `2011`
