# 🤖 Local DevSecOps AI Orchestrator 🛡️

**[Professional Overview]**
This project is a professional-grade, local-first DevSecOps automation hub for cybersecurity auditing. It leverages local Large Language Models (Ollama) to perform SAST, infrastructure hardening, and threat hunting without cloud data exposure. Designed for high-performance security workflows on macOS, it reduces operational friction by 70% while ensuring complete data sovereignty.

---

# 🤖 Orquestador de Ciberseguridad DevSecOps (Local)

Un orquestador secuencial multi-agente de ciberseguridad diseñado para ejecutarse de forma **100% local, privada y asíncrona** en arquitecturas macOS. Este sistema automatiza tareas de auditoría de código, análisis de infraestructura y gestión de vulnerabilidades utilizando un modelo ajustado personalizado sin exponer datos confidenciales a nubes de terceros (Zero Data Leak).

## 🏗️ Arquitectura del Sistema
El proyecto opera bajo una arquitectura de microservicios locales independientes consolidados en un script maestro:
*   **El Cerebro (IA Personalizada):** [Ollama](https://ollama.com) ejecutando el ModelFile personalizado **`cyber-copilot`** (basado en Qwen 2.5-Coder), optimizado nativamente para auditoría de infraestructura y seguridad.
*   **El Motor de Despliegue:** [Docker Desktop para Mac](https://docker.com) orquestando contenedores aislados de infraestructura crítica.
*   **El Orquestador:** Automatización en Python que gestiona la cola de peticiones hacia el socket local de la IA (`http://localhost:11434`).

## 🥷 Los 6 Agentes de Seguridad Integrados
1.  **Auditor de Código (SAST):** Análisis de malas prácticas, inyecciones y *secrets*.
2.  **Analista de Logs (SIEM Local):** Clasificación de ataques en tiempo real.
3.  **Investigador de Amenazas (CTI):** Procesamiento de CVEs y MITRE ATT&CK.
4.  **Simulador de Adversarios (Red Teaming):** Estrategias de ataque/defensa.
5.  **Auditor de Cumplimiento (GRC):** Estándares ISO 27001 / NIST.
6.  **Auditor de Infraestructura (IaC):** Hardening de Docker/Kubernetes.

---

## 🚀 Guía de Inicialización y Automatización

### 🔄 Protocolo SOP: Sincronización Multi-Entorno (Mac 1 / Mac 2)
Para garantizar la integridad del entorno y evitar conflictos al alternar entre múltiples dispositivos macOS, se ejecuta la siguiente secuencia de inspección visual previo a cualquier despliegue:

```bash
# 1. Navegar al repositorio del laboratorio
cd ~/Documents/mis-laboratorios-ciberseguridad

# 2. Consultar cambios lejanos en GitHub sin alteración local
git fetch

# 3. Inspección visual del historial de commits recientes
git log --graph --oneline --all -n 5

# 4. Confirmar que el directorio de trabajo local esté limpio
git status

# 5. Ejecutar la automatización unificada
lab