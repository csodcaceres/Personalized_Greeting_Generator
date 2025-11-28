def validate_input(text: str) -> bool:
    """
    Verifica que el texto recibido no esté vacío.
    """
    return bool(text and text.strip())


def format_text(text: str) -> str:
    """
    Limpia el texto: elimina espacios y coloca mayúscula inicial.
    """
    return text.strip().capitalize()