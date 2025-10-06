'''try:
    num = int(input("Enter a number: "))
    resultado = 10 / num
    print(resultado)
except ZeroDivisionError:
    print("Error: No se permiten las divisiones por cero")
except ValueError:
    print("Error: Invalid input. Please enter a valid number")'''

# 🧠 Ejemplo completo de manejo de excepciones en Python
# Incluye los bloques: try, except, else y finally
# -----------------------------------------------------

## Parte 2
try:
    # 1️⃣ Solicitamos al usuario que introduzca un número
    # La función input() devuelve una cadena (string),
    # por eso usamos int() para convertirla a número entero.
    # Si el usuario introduce algo no numérico, se generará un ValueError.
    num = int(input("Introduce un numero: "))

    # 2️⃣ Intentamos realizar una operación que puede fallar:
    # dividir 10 entre el número introducido.
    # Si el número es 0, se lanzará una excepción de tipo ZeroDivisionError.
    result = 10 / num

    # 3️⃣ Si no se produce ninguna excepción, se muestra el resultado.
    print("Resultado: ", result)

# ⚠️ 4️⃣ Bloque except
# Este bloque captura un error específico: ZeroDivisionError.
# Es decir, si el usuario introduce 0, no se detendrá el programa,
# sino que mostrará el mensaje personalizado de error.
except ZeroDivisionError:
    print("Error: Division por cero no esta permitido. ")

# ✅ 5️⃣ Bloque else
# Este bloque se ejecuta únicamente si NO ocurre ninguna excepción en el try.
# Es útil para confirmar que todo ha salido correctamente.
else:
    print("No ocurrio ninguna excepcion.  Resultado: ", result)

# 🔚 6️⃣ Bloque finally
# Este bloque se ejecuta SIEMPRE, ocurra o no una excepción.
# Se suele usar para cerrar archivos, liberar recursos o mostrar un mensaje final.
finally:
    print("Bloque ejecutado. Programa terminado")

