import requests
import json
import os
import datetime
import sys
import subprocess
import warnings

# Suprimir advertencia de SSL de urllib3
warnings.filterwarnings("ignore", category=UserWarning, module="urllib3")

# --- CONFIGURACIÓN ---
MODELO = "cyber-copilot"
URL_API = "http://localhost:11434/api/generate"
TIMEOUT_SEGUNDOS = 120

# System Prompt estricto
SYSTEM_PROMPT = """ACTÚA COMO AUDITOR DE SEGURIDAD SENIOR.
ANALIZA EL CÓDIGO Y ENTREGA ÚNICAMENTE UN REPORTE TÉCNICO.
ESTRUCTURA:
1. NIVEL DE RIESGO
2. VULNERABILIDADES DETECTADAS (ENUMERADAS)
3. CÓDIGO CORREGIDO Y SUGERENCIAS DE MITIGACIÓN.
NO RESPONDAS CON SALUDOS, NI PREGUNTAS, NI INTRODUCCIONES. SÉ DIRECTO Y TÉCNICO."""

# --- MÓDULO DE AUTO-MANTENIMIENTO ---
def pre_flight_check():
    print("--- 🚀 PRE-FLIGHT CHECK (Orquestador) ---")
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

# --- LÓGICA DE AUDITORÍA ---
def consultar_ia(texto_usuario):
    payload = {
        "model": MODELO,
        "prompt": f"{SYSTEM_PROMPT}\n\nCONTENIDO A AUDITAR:\n{texto_usuario}",
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
    print("   🤖 ORQUESTADOR DE CIBERSEGURIDAD - MODO AUDITOR")
    print("="*50)
    agentes = {
        "1": "Auditor_de_Codigo", "2": "Analista_de_Logs", "3": "Investigador_de_Amenazas",
        "4": "Simulador_de_Red_Teaming", "5": "Auditor_de_Cumplimiento", "6": "Auditor_de_Infraestructura"
    }
    for k, v in agentes.items(): print(f"[{k}] {v}")
    
    seleccion = input("\nSelecciona el Agente (1-6): ")
    if seleccion in agentes:
        print(f"\n[!] Pega el código para {agentes[seleccion]} y presiona 'Enter' + 'Ctrl + D':")
        texto = sys.stdin.read()
        print(f"\n[*] Ejecutando análisis técnico...")
        resultado = consultar_ia(texto)
        print("\n=== REPORTE TÉCNICO ===\n" + resultado)
        
        os.makedirs("logs", exist_ok=True)
        archivo = f"logs/reporte_{agentes[seleccion]}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(archivo, "w") as f: f.write(resultado)
        print(f"\n[+] Evidencia guardada en: {archivo}")
    else:
        print("\n[!] Opción no válida.")

if __name__ == "__main__":
    menu()