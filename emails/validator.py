import logging
import re
import os

# Configuración global del logger
logger = logging.getLogger(__name__)  # Se crea un logger con el nombre del módulo actual
logger.setLevel(logging.INFO)  # Se establece el nivel de log a INFO

# Configuración del manejador de archivos para el log
file_handler = logging.FileHandler('logs/validadoremails.log')  # Se define un manejador para guardar los logs en un archivo
file_handler.setLevel(logging.INFO)

# Formato del log
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')  # Se define el formato de los mensajes del log
file_handler.setFormatter(formatter)  # Se aplica el formato al manejador

# Se añade el manejador al logger
logger.addHandler(file_handler)

class EmailValidator:
    def __init__(self):
        # Expresión regular para validar el formato de un correo electrónico
        self.regex = re.compile(r'([A-Za-z]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

    def validar(self, correo: str):
        try:
            # Comprobación inicial: verificar que el correo es una cadena de texto
            if not isinstance(correo, str):
                logger.error("El correo debe ser una cadena de caracteres.")  # Log de error si el correo no es cadena
                raise ValueError("El correo debe ser una cadena de caracteres.")  # Excepción por tipo inválido
            
            # Comprobar si el correo cumple con la expresión regular
            es_valido = re.fullmatch(self.regex, correo) is not None  # Devuelve True si cumple, False en caso contrario
            
            if es_valido:
                logger.info(f"El correo '{correo}' que introdujo es válido.")  # Log informativo de éxito
            else:
                logger.warning(f"El correo '{correo}' que introdujo es inválido.")  # Log de advertencia de fallo
            
            return es_valido  # Devuelve True si es válido, False si no lo es
        
        except Exception as e:
            # Captura cualquier excepción durante el proceso de validación
            logger.error(f"Error al validar el correo introducido: {e}")  # Log del error específico
            return False  # Devuelve False en caso de error
