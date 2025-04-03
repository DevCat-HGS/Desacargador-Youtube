import os
import sys
import re
import traceback
import yt_dlp

def validar_url_youtube(url):
    """
    Valida si la URL proporcionada es una URL válida de YouTube.
    
    Args:
        url (str): URL a validar
        
    Returns:
        bool: True si es una URL válida de YouTube, False en caso contrario
    """
    # Patrones de URL de YouTube
    patrones = [
        r'^(https?://)?(www\.)?(youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})',
        r'^(https?://)?(www\.)?youtube\.com/shorts/([a-zA-Z0-9_-]{11})'
    ]
    
    for patron in patrones:
        if re.match(patron, url):
            return True
    return False

def descargar_video(url, ruta_destino=None):
    """
    Descarga un video de YouTube con la mejor calidad disponible usando yt-dlp.
    
    Args:
        url (str): URL del video de YouTube
        ruta_destino (str, opcional): Ruta donde se guardará el video. Si no se proporciona,
                                      se guardará en el directorio actual.
    
    Returns:
        str: Ruta del archivo descargado o mensaje de error
    """
    # Validar la URL antes de intentar descargar
    if not validar_url_youtube(url):
        error_msg = "Error: La URL proporcionada no parece ser una URL válida de YouTube."
        print(error_msg)
        return error_msg
        
    try:
        # Determinar la ruta de destino
        if ruta_destino is None:
            ruta_destino = os.getcwd()
        
        print(f"Conectando con YouTube para: {url}")
        
        # Configurar opciones de yt-dlp
        ydl_opts = {
            'format': 'best',  # Mejor calidad disponible
            'outtmpl': os.path.join(ruta_destino, '%(title)s.%(ext)s'),
            'noplaylist': True,  # Solo descargar el video, no la lista de reproducción
            'quiet': False,  # Mostrar progreso
            'no_warnings': False,  # Mostrar advertencias
        }
        
        # Crear un objeto de progreso personalizado para mostrar información
        class MyLogger:
            def debug(self, msg):
                # No mostrar mensajes de depuración
                pass
            
            def warning(self, msg):
                print(f"Advertencia: {msg}")
            
            def error(self, msg):
                print(f"Error: {msg}")
        
        # Función para mostrar el progreso de la descarga
        def my_hook(d):
            if d['status'] == 'downloading':
                if 'total_bytes' in d and d['total_bytes'] > 0:
                    percent = d['downloaded_bytes'] / d['total_bytes'] * 100
                    # Verificar si existe total_bytes_estimate antes de usarlo
                    if 'total_bytes_estimate' in d:
                        print(f"Descargando: {percent:.1f}% de {d['total_bytes_estimate'] / 1024 / 1024:.1f} MB", end='\r')
                    else:
                        print(f"Descargando: {percent:.1f}% completado", end='\r')
                else:
                    print(f"Descargando: {d['downloaded_bytes'] / 1024 / 1024:.1f} MB descargados", end='\r')
            elif d['status'] == 'finished':
                print("\nDescarga completada. Procesando archivo...")
        
        # Agregar logger y hook a las opciones
        ydl_opts['logger'] = MyLogger()
        ydl_opts['progress_hooks'] = [my_hook]
        
        # Descargar el video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Obtener información del video primero
            info = ydl.extract_info(url, download=False)
            print(f"Título del video: {info.get('title', 'Desconocido')}")
            print(f"Duración: {info.get('duration', 0)} segundos")
            print("Buscando la mejor calidad disponible...")
            
            # Descargar el video
            print("Iniciando descarga...")
            ydl.download([url])
            
            # Construir la ruta del archivo descargado
            # Usar .get() para evitar errores si info es None o no tiene las claves necesarias
            if info and isinstance(info, dict):
                titulo = info.get('title', 'video_descargado')
                extension = info.get('ext', 'mp4')
                archivo_descargado = os.path.join(ruta_destino, f"{titulo}.{extension}")
                
                print(f"\n¡Descarga completada!")
                print(f"El video se ha guardado en: {archivo_descargado}")
            else:
                archivo_descargado = "Archivo descargado (ruta no disponible)"
                print(f"\n¡Descarga completada!")
                print("No se pudo determinar la ruta exacta del archivo descargado.")
            
            return archivo_descargado
    
    except yt_dlp.utils.DownloadError as e:
        error_msg = f"Error de descarga: {str(e)}"
        print(error_msg)
        return error_msg
    except yt_dlp.utils.ExtractorError as e:
        error_msg = f"Error al extraer información del video: {str(e)}"
        print(error_msg)
        return error_msg
    except Exception as e:
        error_msg = f"Error inesperado: {str(e)}"
        print(error_msg)
        # Mostrar información detallada de depuración
        print("\nInformación de depuración:")
        print(traceback.format_exc())
        return error_msg

def main():
    # URL del video proporcionada por el usuario
    url_video = ""
    
    # Si se proporciona una URL como argumento, usar esa en su lugar
    if len(sys.argv) > 1:
        url_video = sys.argv[1]
    else:
        # Si no se proporciona URL, solicitar al usuario
        print("\n=== Descargador de Videos de YouTube ===\n")
        print("Ejemplos de URLs válidas:")
        print("- https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        print("- https://youtu.be/dQw4w9WgXcQ")
        print("- https://youtube.com/shorts/dQw4w9WgXcQ\n")
        url_video = input("Introduce la URL del video de YouTube: ")
    
    # Verificar que la URL no esté vacía
    if not url_video.strip():
        print("Error: No se ha proporcionado una URL válida.")
        return
    
    # Descargar el video
    print("\nIniciando proceso de descarga...\n")
    resultado = descargar_video(url_video)
    
    # Si el resultado comienza con "Error", la descarga falló
    if isinstance(resultado, str) and resultado.startswith("Error"):
        print("\nLa descarga ha fallado. Por favor, verifica la URL e intenta nuevamente.")
        print("Si el problema persiste, puede deberse a restricciones de YouTube.")
        print("Sugerencia: Intenta actualizar yt-dlp con 'pip install --upgrade yt-dlp'")
    

if __name__ == "__main__":
    main()