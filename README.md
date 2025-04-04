# Desacargador-Youtube

## Descripción

Desacargador-Youtube es una herramienta de línea de comandos desarrollada en Python que permite descargar videos de YouTube con la mejor calidad disponible. Utiliza la biblioteca `yt-dlp` para gestionar las descargas de manera eficiente, mostrando información detallada sobre el progreso y manejando diferentes tipos de URLs de YouTube (videos estándar y shorts).

## Características

- Descarga videos de YouTube con la mejor calidad disponible
- Soporta URLs de videos estándar y shorts de YouTube
- Muestra información detallada del progreso de descarga
- Validación de URLs para asegurar que sean enlaces válidos de YouTube
- Manejo de errores robusto con mensajes informativos
- Interfaz de línea de comandos simple e intuitiva
- Opción de especificar la ruta de destino para guardar los videos

## Requisitos

Para utilizar esta herramienta, necesitas tener instalado:

- Python 3.6 o superior
- Las siguientes bibliotecas de Python (incluidas en `requirements.txt`):
  - yt-dlp

## Instalación

1. Clona o descarga este repositorio:

```bash
git clone https://github.com/tu-usuario/DescargadorYoutubeMP4.git
cd DescargadorYoutubeMP4
```

2. Instala las dependencias necesarias:

```bash
pip install -r requirements.txt
```

## Uso

### Método 1: Ejecución interactiva

Ejecuta el script sin argumentos para iniciar el modo interactivo:

```bash
python youtube_downloader.py
```

El programa te solicitará que ingreses la URL del video de YouTube que deseas descargar.

### Método 2: Línea de comandos con URL

Puedes proporcionar la URL directamente como argumento:

```bash
python youtube_downloader.py https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

### Formatos de URL soportados

El programa acepta los siguientes formatos de URL:

- Videos estándar: `https://www.youtube.com/watch?v=ID_DEL_VIDEO`
- Videos acortados: `https://youtu.be/ID_DEL_VIDEO`
- Shorts: `https://youtube.com/shorts/ID_DEL_VIDEO`

## Estructura del código

El programa está organizado en tres funciones principales:

1. `validar_url_youtube(url)`: Valida si la URL proporcionada corresponde a un video de YouTube utilizando expresiones regulares.

2. `descargar_video(url, ruta_destino=None)`: Función principal que gestiona la descarga del video, muestra el progreso y maneja los posibles errores.

3. `main()`: Punto de entrada del programa que gestiona la interfaz de usuario y llama a las funciones anteriores.

## Solución de problemas

### URLs no válidas

Si recibes el mensaje "La URL proporcionada no parece ser una URL válida de YouTube", asegúrate de que:

- La URL sea correcta y esté completa
- El formato de la URL sea uno de los soportados (ver sección "Formatos de URL soportados")

### Errores de descarga

Si la descarga falla con un mensaje de error, puede deberse a:

1. Restricciones del video (edad, geográficas, etc.)
2. Cambios en la API de YouTube
3. Versión desactualizada de yt-dlp

Solución recomendada: Actualiza yt-dlp a la última versión:

```bash
pip install --upgrade yt-dlp
```

## Consideraciones legales

Esta herramienta está diseñada para uso personal y educativo. Al utilizarla, debes respetar:

- Los términos de servicio de YouTube
- Las leyes de derechos de autor aplicables en tu país
- No utilizar los videos descargados con fines comerciales sin autorización

## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar esta herramienta, puedes:

1. Hacer un fork del repositorio
2. Crear una rama para tu funcionalidad (`git checkout -b nueva-funcionalidad`)
3. Hacer commit de tus cambios (`git commit -am 'Añadir nueva funcionalidad'`)
4. Hacer push a la rama (`git push origin nueva-funcionalidad`)
5. Crear un Pull Request

## Licencia

Este proyecto está licenciado bajo [incluir licencia aquí, por ejemplo MIT o GPL].
