# This Python file uses the following encoding: utf-8
import os, sys

from ..sample import uno, zero, saludar

# Ejemplo de fichero de pruebas pytest
# Autor: José Gaspar Sánchez García

def test_uno():
    assert uno() == 1

def test_zero():
    assert zero() == 0
def test_saludar():
    assert saludar() == "Hola mundo"