from helpers.consts import PASSWORDS_PATH
import json
import os


def load_passwords():
    if not os.path.exists(PASSWORDS_PATH):
        return {"passwords": []}

    with open(PASSWORDS_PATH, "r") as f:
        return json.load(f)


def save_passwords(data):
    with open(PASSWORDS_PATH, "w") as f:
        json.dump(data, f, indent=4)


if __name__ == "__main__":
    data = load_passwords()

    new_password = input("Ingrese una contraseña inicial: ").strip()

    if not new_password:
        print("La contraseña no puede estar vacía")
        exit()

    if new_password in data["passwords"]:
        print("Esa contraseña ya existe")
    else:
        data["passwords"].append(new_password)
        save_passwords(data)
        print("Contraseña agregada correctamente")