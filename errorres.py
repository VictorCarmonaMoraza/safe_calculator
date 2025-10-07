class CalculadoraError(Exception):
    """Clase base para excepciones de la calculadora."""
    pass


class DivisionPorCeroError(CalculadoraError):
    """Se lanza cuando se intenta dividir entre cero."""
    def __init__(self, mensaje="No se puede dividir entre cero"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


class EntradaInvalidaError(CalculadoraError):
    """Se lanza cuando el usuario introduce un valor no numérico."""
    def __init__(self, mensaje="Entrada no válida"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)