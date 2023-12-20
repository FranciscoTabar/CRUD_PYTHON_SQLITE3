import sqlite3

conn = sqlite3.connect( "databse.db")
cursor = conn.cursor()

cursor.execute(
    """
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT,
                    email TEXT
                )
                """
)
conn.commit()

######### Crear registro -> C
def crear_usuario(nombre:str, email:str) -> str:
    cursor.execute("INSERT INTO usuarios (nombre , email) VALUES(?,?)", (nombre, email))
    conn.commit()
    return" usuario agregado"

######### Obtener registro -> R
def obtener_registros():
    cursor.execute("SELECT id, nombre, email FROM usuarios")
    lista_usuarios= cursor.fetchall()
    print("{:<5} {:<15}{:<30}".format("ID", "Nombre","Email"))
    print("-"*55)
    for usuario in lista_usuarios:
        print("{:<5} {:<15} {:<30}".format(usuario[0], usuario[1], usuario[2]))
    

######## Obtener usuario -> U
def actualizar_usuario(id:int, nombre:str, email:str)-> str:
    cursor.execute(
        "UPDATE usuarios SET nombre=?, email=?,WHERE id=?",(nombre, email,id)
        )
    conn.commit()
    return"usuario actualizado"

######## Eliminar usuario -> D
def eliminar(id):
    cursor.execute("DELETE FROM usuarios WHERE id = ? ", (id,))
    conn.commit()
    return"usuario eliminado"

def obtener_usuarios(id:int)->list:
    cursor.execute("SELECT id, nombre, email FROM usuarios WHERE id = ? ", (id,))
    usuario = cursor.fetchone()
    if usuario:
        return usuario
    return"usuario no encontrado"


while True:
    print("\n>>>>>>>>>>>> MENU DE INICIO <<<<<<<<<<<<<<<<")
    print("\n1. Guardar un nuevo usuario")
    print("2. Ver registros de usuarios")
    print("3. Salir")

    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == "1":
        # Solicitar al usuario que ingrese nombre y correo electrónico
        nombre = input("Ingrese el nombre: ")
        email = input("Ingrese el correo electrónico: ")

        # Llamar a la función para crear un nuevo usuario
        print(crear_usuario(nombre, email))

    elif opcion == "2":
        # Llamar a la función para obtener registros
        print("\nRegistros en la base de datos:")
        obtener_registros()

    elif opcion == "3":
        print("Saliendo del programa. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Por favor, ingrese un número válido.")
