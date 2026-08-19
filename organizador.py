import os
import shutil

Mapa_Carpetas = {
    "Documentos": [".pdf", ".txt", ".docx", ".xlsx"],
    "Imagenes": [".jpg", ".jpeg", ".png", ".gif"],
    "Instaladores": [".dmg", ".pkg", ".zip"]
}

Carpeta_A_Limpiar = "/Users/idarraganieves/Downloads"

def iniciar_organizador():
    if os.path.exists(Carpeta_A_Limpiar):
        print("¡Sí, la carpeta existe de verdad!\n")
        
        # Leemos los archivos sueltos
        mis_archivos = os.listdir(Carpeta_A_Limpiar)
        total = len(mis_archivos)
        print(f"Tienes {total} elementos en total dentro de Descargas.\n")

        # Creamos las carpetas si no existen
        for carpeta in Mapa_Carpetas:
            ruta_nueva_carpeta = f"{Carpeta_A_Limpiar}/{carpeta}"      
            os.makedirs(ruta_nueva_carpeta, exist_ok=True)

        # Recorremos y movemos cada archivo
        for archivo in mis_archivos:
            nombre, ext = os.path.splitext(archivo)
            ext = ext.lower() 

            for carpeta, extensiones_validas in Mapa_Carpetas.items():
                if ext in extensiones_validas:
                    
                    ruta_origen = f"{Carpeta_A_Limpiar}/{archivo}"
                    ruta_destino = f"{Carpeta_A_Limpiar}/{carpeta}/{archivo}"
                    
                    shutil.move(ruta_origen, ruta_destino)
                    print(f"📦 Movido con éxito: {archivo} -> Carpeta {carpeta}")

        print("\n🎉 ¡Organización completada con éxito!")

    else:
        print("❌ No, esa carpeta no existe o escribiste mal el nombre.")

iniciar_organizador()
