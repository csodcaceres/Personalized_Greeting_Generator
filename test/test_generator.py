import pytest
from generator import greet  # o del módulo donde esté tu código

def test_greet_basic():
    assert greet("Juan") == "Hola, Juan! Bienvenido."

def test_greet_empty():
    assert greet("") == "Hola! Bienvenido."  # o como quieras manejarlo
