from generator import GreetingBuilder, validate_input, format_text

def main():
    print("=== Personalized Greeting Generator ===")

    # Inputs
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    color = input("Enter your favorite color: ")

    # Validaciones
    if not validate_input(name):
        print("Invalid name. Exiting program.")
        return

    if not validate_input(age):
        print("Invalid age. Exiting program.")
        return

    if not validate_input(color):
        print("Invalid color. Exiting program.")
        return

    # Formateo
    name = format_text(name)
    color = format_text(color)

    # Crear mensaje usando la clase OOP
    builder = GreetingBuilder(name, age, color)
    message = builder.build_message()

    print("\n---- Personalized Greeting Message -----")
    print(message)


if __name__ == "__main__":
    main()
