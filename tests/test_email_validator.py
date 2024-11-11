import unittest
from emails.validator import EmailValidator
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestEmailValidator(unittest.TestCase):
    def setUp(self):
        self.validator = EmailValidator()

    def test_email_valido(self): #Verificar que se devuelve true si los  correos cumplen el formato
        self.assertTrue(self.validator.validar("ejemplo.email@dominio.com"))
        self.assertTrue(self.validator.validar("nombre.apellido@subdominio.dominio.com"))

    def test_email_invalido(self): #Verificar que se devuelve false si los correos no cumplen el formato
        self.assertFalse(self.validator.validar("correo.sin.arroba"))
        self.assertFalse(self.validator.validar("incorrecto@.com"))
        self.assertFalse(self.validator.validar("incorrecto@dominio"))

    def test_email_none(self): #Probar el caso de que no se introduzca ningun valor
        self.assertFalse(self.validator.validar(None))

if __name__ == "__main__":
    unittest.main()
