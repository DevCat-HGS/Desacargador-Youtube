import os
import sys
from pytube import YouTube

def descargar_video(url, ruta_destino=None):
    """
    Descarga un video de YouTube con la mejor calidad disponible.
    
    Args:
        url (str): URL del video de YouTube
        ruta_destino (str, opcional): Ruta donde se guardará el video. Si no se proporciona,
                                      se guardará en el directorio actual.
    
    Returns:
        str: Ruta del archivo descargado o mensaje de error
    """
    try:
        # Crear objeto YouTube
        print(f"Conectando con YouTube para: {url}")
        yt = YouTube(url, on_progress_callback=lambda stream, chunk, bytes_remaining: None)
        
        # Obtener el stream con la mejor resolución
        print(f"Título del video: {yt.title}")
        print("Buscando la mejor calidad disponible...")
        
        # Obtener el stream con la mejor resolución con audio y video juntos
        video_stream = yt.streams.get_highest_resolution()
        
        # Verificar si se encontró un stream válido
        if video_stream is None:
            return "Error: No se pudo encontrar un stream de video adecuado para descargar."
        
        # Determinar la ruta de destino
        if ruta_destino is None:
            ruta_destino = os.getcwd()
        
        # Descargar el video
        print(f"Descargando video en calidad: {video_stream.resolution if video_stream else 'desconocida'}")
        archivo_descargado = video_stream.download(output_path=ruta_destino)
        
        print(f"\n¡Descarga completada!")
        print(f"El video se ha guardado en: {archivo_descargado}")
        
        return archivo_descargado
    
    except Exception as e:
        error_msg = f"Error al descargar el video: {str(e)}"
        print(error_msg)
        return error_msg

def main():
    # URL del video proporcionada por el usuario
    url_video = "https://youtu.be/Z2XzaUM1JiM?si=S5HC5oSUVWkcpL4Y"
    
    # Si se proporciona una URL como argumento, usar esa en su lugar
    if len(sys.argv) > 1:
        url_video = sys.argv[1]
    
    # Descargar el video
    descargar_video(url_video)

if __name__ == "__main__":
    main()