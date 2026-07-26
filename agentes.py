import requests
import json
import os
import datetime
import sys
import subprocess
import warnings

# Suprimir advertencia de SSL de urllib3
warnings.filterwarnings("ignore", category=UserWarning, module="urllib3")

# Configuración
MODELO = "cyber-copilot"
URL_API = "http://localhost:11434/api/generate"
TIMEOUT_SEGUNDOS = 120

# Definición de los 6 agentes
CONFIGURACION_AGENTES = {
    "1": {"nombre": "Auditor_de_Codigo", "prompt": "ACTÚA COMO AUDITOR DE CÓDIGO (SAST). ANALIZA EL CÓDIGO EN BUSCA DE CWE, INYECCIONES Y VULNERABILIDADES LÓGICAS. ENTREGA REPORTE TÉCNICO Y CÓDIGO CORREGIDO."},
    "2": {"nombre": "Analista_de_Logs", "prompt": "ACTÚA COMO ANALISTA DE SEGURIDAD (SOC). BUSCA PATRONES DE ATAQUE, ACCESOS NO AUTORIZADOS O ANOMALÍAS EN LOS LOGS PROPORCIONADOS."},
    "3": {"nombre": "Investigador_de_Amenazas", "prompt": "ACTÚA COMO INTEL DE AMENAZAS (CTI). ANALIZA EL TEXTO BUSCANDO INDICADORES DE COMPROMISO (IOCs), TÉCNICAS MITRE ATT&CK Y VECTORES DE ATAQUE."},
    "4": {"nombre": "Simulador_de_Red_Teaming", "prompt": "ACTÚA COMO RED TEAMER. EVALÚA LA POSIBILIDAD DE EXPLOTACIÓN DE LOS HALLAZGOS Y SUGIERE VECTORES DE ATAQUE PARA PRUEBAS DE PENETRACIÓN."},
    "5": {"nombre": "Auditor_de_Cumplimiento", "prompt": "ACTÚA COMO AUDITOR DE COMPLIANCE (NIST/GDPR/ISO). VERIFICA SI EL CÓDIGO O LA CONFIGURACIÓN CUMPLE CON LOS ESTÁNDARES DE SEGURIDAD INDUSTRIAL."},
    "6": {"nombre": "Auditor_de_Infraestructura", "prompt": "ACTÚA COMO INGENIERO DE HARDENING. ANALIZA CONFIGURACIONES DE RED, SERVIDORES Y SERVICIOS EN LA NUBE. SUGIERE MEJORAS DE SEGURIDAD PARA EL HARDENING."}
}

# --- MÓDULO DE AUTO-MANTENIMIENTO ---
def pre_flight_check():
    print("--- 🚀 PRE-FLIGHT CHECK (Agentes) ---")
    try:
        subprocess.run(["git", "pull", "origin", "main"], capture_output=True)
        print("[+] Repositorio sincronizado.")
    except:
        print("[!] No se pudo sincronizar git.")
    if os.path.exists("requirements.txt"):
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", "-q", "-r", "requirements.txt"], check=True)
            print("[+] Dependencias validadas.")
        except:
            print("[!] Error al validar dependencias.")
    print("---------------------------\n")

def consultar_ia(texto_usuario, prompt_sistema):
    payload = {
        "model": MODELO,
        "prompt": f"{prompt_sistema}\n\nCONTENIDO A ANALIZAR:\n{texto_usuario}",
        "stream": False
    }
    try:
        response = requests.post(URL_API, json=payload, timeout=TIMEOUT_SEGUNDOS)
        response.raise_for_status()
        return response.json().get("response", "Error: Respuesta vacía.")
    except Exception as e:
        return f"Error de conexión con Ollama: {e}"

def menu():
    pre_flight_check()
    print("\n" + "="*50)
    print("   🤖 HUB MULTI-AGENTE DE CIBERSEGURIDAD")
    print("="*50)
    for k, v in CONFIGURACION_AGENTES.items(): 
        print(f"[{k}] {v['nombre']}")
    
    seleccion = input("\nSelecciona el Agente (1-6): ")
    if seleccion in CONFIGURACION_AGENTES:
        agente = CONFIGURACION_AGENTES[seleccion]
        print(f"\n[!] Has seleccionado a: {agente['nombre']}")
        print(f"[!] Pega el contenido y presiona 'Enter' + 'Ctrl + D':")
        texto = sys.stdin.read()
        print(f"\n[*] Ejecutando análisis con agente {agente['nombre']}...")
        resultado = consultar_ia(texto, agente['prompt'])
        print("\n=== REPORTE TÉCNICO ===\n" + resultado)
        
        os.makedirs("logs", exist_ok=True)
        archivo = f"logs/reporte_{agente['nombre']}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(archivo, "w") as f: f.write(resultado)
        print(f"\n[+] Evidencia guardada en: {archivo}")
    else:
        print("\n[!] Opción no válida.")

if __name__ == "__main__":
    menu()