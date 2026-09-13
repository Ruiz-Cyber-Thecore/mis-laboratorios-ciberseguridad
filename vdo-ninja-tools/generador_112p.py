# generador_112p.py
import os
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

# 1. ARQUITECTURA MAESTRA FIJA: MODO SÚPER NITIDEZ (112p)
# Esta configuración garantiza la densidad óptima de bits sin asfixiar el Wi-Fi.
CONFIG_RESILIENCIA_112P = {
    'whipoutvideobitrate': '35',
    'whipoutaudiobitrate': '27',
    'framerate': '5',
    'width': '200',
    'height': '112',
    'buffer': '7500',
    'latency': '7500',
    'pacing': '3',
    'videocodec': 'h264'
}

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def procesar_enlace_vdo():
    limpiar_pantalla()
    print("=" * 65)
    print("   AUTOMATIZACIÓN VDO.ninja - MODO SUPER NITIDEZ 112p (62 kbps)   ")
    print("=" * 65)
    
    # Captura interactiva de la URL dinámica
    url_input = input("\n🔗 Pega la URL original o las nuevas credenciales de VDO.ninja:\n> ").strip()
    
    if not url_input:
        print("\n❌ Error: No ingresaste ninguna URL.")
        return

    try:
        # Analizar la estructura de la URL provista
        parsed_url = urlparse(url_input)
        params_originales = parse_qs(parsed_url.query)

        # Extraer credenciales dinámicas esenciales de la plataforma
        push = params_originales.get('push', [None])[0]
        whippush = params_originales.get('whippush', [None])[0]
        whippushtoken = params_originales.get('whippushtoken', [None])[0]

        # Validación estricta de componentes de transmisión
        if not all([push, whippush, whippushtoken]):
            print("\n❌ ERROR CRÍTICO: El enlace no es válido.")
            print("Asegúrate de que la URL contenga los parámetros: push, whippush y whippushtoken.")
            return

        # Fusión matemática: Combinamos la plantilla fija de 112p con los tokens extraídos
        nuevos_parametros = {
            **CONFIG_RESILIENCIA_112P, 
            'push': push, 
            'whippush': whippush, 
            'whippushtoken': whippushtoken
        }
        
        # Codificar de manera segura para evitar roturas de caracteres en la red
        query_string_nueva = urlencode(nuevos_parametros)

        # Reconstrucción del enlace final apuntando al dominio limpio de VDO.ninja
        url_final = urlunparse((
            parsed_url.scheme if parsed_url.scheme else 'https',
            parsed_url.netloc if parsed_url.netloc else 'vdo.ninja',
            parsed_url.path if parsed_url.path else '/',
            '',
            query_string_nueva,
            ''
        ))

        # Despliegue del resultado listo para copiar
        print("\n" + "✓" * 65)
        print("🚀 ¡ENLACE RESILIENTE GENERADO CON ÉXITO! (Listo para usar en Chrome)")
        print("✓" * 65)
        print(f"\n{url_final}\n")
        print("=" * 65)
        print("💡 Recuerda: Aplica zoom del 250%-300% en la pestaña de origen.")
        print("=" * 65)

    except Exception as e:
        print(f"\n❌ Ocurrió un error inesperado al parsear el enlace: {e}")

if __name__ == "__main__":
    procesar_enlace_vdo()