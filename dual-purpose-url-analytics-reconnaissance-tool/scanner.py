import requests

def generar_enlace():
    url_larga = input("Pega tu enlace de WhatsApp: ").strip()
    if not url_larga:
        return

    # Usamos requests para enviar los parámetros, esto es más seguro y evita errores de sintaxis
    api_url = "https://tinyurl.com/api-create.php"
    
    try:
        print(f"\n⏳ Enviando a TinyURL...")
        # El parámetro 'params' codifica automáticamente los espacios y caracteres especiales
        respuesta = requests.get(api_url, params={'url': url_larga}, timeout=10)
        
        if respuesta.status_code == 200:
            print(f"\n✅ Enlace generado: {respuesta.text}")
            print("---")
            print("⚠️ Prueba este enlace en tu navegador. Si no funciona, es posible que TinyURL esté bloqueando el formato del enlace de WhatsApp.")
        else:
            print(f"\n❌ Error del servicio: {respuesta.status_code}")
    except Exception as e:
        print(f"\n❌ Error de conexión: {e}")

if __name__ == "__main__":
    generar_enlace()
