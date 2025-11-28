class GreetingBuilder:
    """
    Clase encargada de crear mensajes personalizados para el usuario.
    """

    def __init__(self, name: str, age: str, color: str):
        self.name = name
        self.age = age
        self.color = color

    def build_message(self) -> str:
        """
        Retorna un mensaje personalizado utilizando los datos del usuario.
        """
        return (
            f"Hello {self.name}!\n"
            f"You are {self.age} years old.\n"
            f"Your favorite color is {self.color}.\n"
            "You're now ready to start your Python adventure!"
        )
