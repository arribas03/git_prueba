import os

def crear_archivo(ruta, contenido):
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(contenido)

def setup():
    base = "Laberinto_Terminal"
    
    # 1. Crear estructura base
    os.makedirs(base, exist_ok=True)
    
    # Nivel 1
    os.makedirs(f"{base}/Sala_Principal", exist_ok=True)
    os.makedirs(f"{base}/Sotano_Oscuro", exist_ok=True)
    os.makedirs(f"{base}/Torre_Alta", exist_ok=True)
    
    # Nivel 2 (Profundidad)
    os.makedirs(f"{base}/Sotano_Oscuro/Caja_Fuerte", exist_ok=True)
    os.makedirs(f"{base}/Torre_Alta/Biblioteca", exist_ok=True)
    
    # Archivos "Basura" (para que usen ls y los ignoren)
    crear_archivo(f"{base}/leeme.txt", "Tu misión: Encuentra el script 'tesoro.py' y ejecútalo.\nPara ello, busca las pistas en las carpetas.")
    crear_archivo(f"{base}/Sala_Principal/polvo.txt", "Nada interesante por aquí.")
    crear_archivo(f"{base}/Sala_Principal/silla_rota.log", "Log de silla: Se rompió.")
    
    # Archivos Pista
    crear_archivo(f"{base}/Sala_Principal/PISTA_1.txt", "La siguiente pista está donde hace mucho frío y oscuridad.\n(Ve al Sotano_Oscuro)")
    crear_archivo(f"{base}/Sotano_Oscuro/PISTA_2.txt", "Parece que la puerta está cerrada. La llave está en lo más alto del castillo.\n(Ve a Torre_Alta/Biblioteca)")
    
    # El Tesoro (Script final)
    codigo_tesoro = """
printWithSmile = print
printWithSmile("-" * 40)
printWithSmile("¡FELICIDADES! HAS ENCONTRADO EL TESORO")
printWithSmile("-" * 40)
printWithSmile("       ___________      ")
printWithSmile("      '._==_==_=_.'     ")
printWithSmile("      .-\\:      /-.    ")
printWithSmile("     | (|:.     |) |    ")
printWithSmile("      '-|:.     |-'     ")
printWithSmile("        \\::.    /      ")
printWithSmile("         '::. .'        ")
printWithSmile("           ) (          ")
printWithSmile("         _.' '._        ")
printWithSmile("        `-------`       ")
printWithSmile("-" * 40)
printWithSmile("Ya dominas la terminal. ¡Buen trabajo!")
"""
    crear_archivo(f"{base}/Torre_Alta/Biblioteca/tesoro.py", codigo_tesoro)

    print(f"¡Juego configurado! Se ha creado la carpeta '{base}'.")

if __name__ == "__main__":
    setup()