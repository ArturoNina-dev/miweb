# ==========================================
# Evaluación Continua HITO 3 - Programación POO
# Sistema de Validación de Datos de Usuario
# ==========================================

import re

# Clase base (Superclase)
class ValidadorDato:
    def __init__(self, valor):
        self.valor = valor

    def es_valido(self):
        # Método que será sobrescrito por las clases hijas
        pass


# Clase para validar el formato de correo electrónico
class ValidadorEmail(ValidadorDato):
    def es_valido(self):
        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(patron, self.valor):
            return True
        return False


# Clase para validar la edad del usuario
class ValidadorEdad(ValidadorDato):
    def es_valido(self):
        try:
            edad = int(self.valor)
            if 0 < edad < 120:
                return True
            return False
        except ValueError:
            return False


# Clase para validar la seguridad de la contraseña
class ValidadorPassword(ValidadorDato):
    def es_valido(self):
        # Debe tener al menos 6 caracteres y combinar letras con números
        if len(self.valor) >= 6 and any(c.isdigit() for c in self.valor):
            return True
        return False


# --- Programa Principal ---
if __name__ == "__main__":
    print("=== SISTEMA DE REGISTRO Y VALIDACIÓN DE DATOS ===")
    
    # Entrada de datos
    correo = input("Ingresa tu correo electrónico: ")
    edad = input("Ingresa tu edad: ")
    password = input("Ingresa tu contraseña: ")

    # Instancia de objetos
    val_email = ValidadorEmail(correo)
    val_edad = ValidadorEdad(edad)
    val_pass = ValidadorPassword(password)

    print("\nProcesando validación...")

    # Verificación de los datos
    if not val_email.es_valido():
        print("[Error]: El correo electrónico no tiene un formato válido.")
    elif not val_edad.es_valido():
        print("[Error]: La edad ingresada debe ser un número válido entre 1 y 119.")
    elif not val_pass.es_valido():
        print("[Error]: La contraseña debe tener al menos 6 caracteres y al menos un número.")
    else:
        print("\n¡Registro completado exitosamente! Todos los datos son válidos.")