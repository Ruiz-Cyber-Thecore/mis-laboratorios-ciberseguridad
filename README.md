# 🤖 Local DevSecOps AI Orchestrator 🛡️

Un orquestador secuencial multi-agente de ciberseguridad diseñado para ejecutarse de forma **100% local, privada y asíncrona** en arquitecturas macOS. Este sistema automatiza tareas de auditoría de código, análisis de infraestructura y gestión de vulnerabilidades utilizando un modelo ajustado personalizado sin exponer datos confidenciales a nubes de terceros (Zero Data Leak).

---

## 🏗️ Arquitectura del Sistema
El proyecto opera bajo una arquitectura de microservicios locales independientes consolidados en un script maestro:
*   **El Cerebro (IA Personalizada):** [Ollama](https://ollama.com) ejecutando el ModelFile personalizado **`cyber-copilot`** (basado en Qwen 2.5-Coder), optimizado nativamente con instrucciones del sistema para auditoría de infraestructura y seguridad ofensiva/defensiva.
*   **El Motor de Despliegue:** [Docker Desktop para Mac](https://docker.com) orquestando contenedores aislados de infraestructura crítica (como servidores Jenkins y entornos de pruebas vulnerables).
*   **El Orquestador Secuencial:** Un script de automatización en Python (desarrollado en VS Code) que gestiona la cola de peticiones hacia el socket local de la IA (`http://localhost:11434`) sin saturar la memoria RAM/VRAM unificada de la MacBook Air.

---

## 🥷 Los 6 Agentes de Seguridad Integrados

1.  **Auditor de Código (SAST):** Analiza archivos fuente en busca de malas prácticas, inyecciones (SQL, XSS) y credenciales expuestas (*secrets*) antes del despliegue.
2.  **Analista de Logs (SIEM Local):** Evalúa bitácoras de servidores en tiempo real para clasificar amenazas como ataques de fuerza bruta o escaneos de red.
3.  **Investigador de Amenazas (CTI):** Procesa boletines técnicos de vulnerabilidades globales (CVE, MITRE ATT&CK) y genera resúmenes ejecutivos de impacto.
4.  **Simulador de Adversarios (Red Teaming):** Interpreta reportes de escaneo de puertos (Nmap) y sugiere estrategias de ataque/defensa con herramientas de auditoría.
5.  **Auditor de Cumplimiento (GRC):** Evalúa políticas internas y topologías de red contrastándolas con estándares internacionales (ISO 27001 / NIST).
6.  **Auditor de Infraestructura (IaC):** Revisa archivos de configuración (`Dockerfile`, Kubernetes) buscando malas prácticas, uso de usuarios *root* o puertos inseguros expuestos.

---

## 🚀 Guía de Inicialización Rápida (Entorno Mac Native)

### 1. Inicializar el Entorno de la IA
Accede a tu entorno de Inteligencia Artificial local directamente desde la terminal de macOS (`zsh` en `ttys000`) utilizando tu alias optimizado:
```bash
guillermoruiz1@MacBook-Air-de-Guillermo-2 ~ % lab
Already up to date.
>>> Send a message (/? for help)
```

### 2. Levantar Infraestructura de Automatización (Docker)
Crea el puente de red e inicializa tu servidor Jenkins local desde una segunda terminal para enlazar la red con tu Mac:
```bash
docker run -d \
  -p 8080:8080 \
  -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  --add-host=host.docker.internal:host-gateway \
  --name mi-jenkins \
  jenkins/jenkins:lts
```

### 3. Configurar el Comando Rápido (`ciber-run`)
Para ejecutar tu software de automatización desde cualquier ubicación de tu terminal sin escribir rutas largas, registra el alias nativo ejecutando esto en la carpeta de tu proyecto:
```bash
echo "alias ciber-run='python3 \$(pwd)/orquestador.py'" >> ~/.zshrc && source ~/.zshrc
```

### 4. Lanzar el Orquestador Central
Simplemente ejecuta tu nueva palabra clave en la terminal integrada de tu IDE:
```bash
ciber-run
```

---

## 📊 Historial y Evidencias Automatizadas
El sistema implementa un módulo de cumplimiento normativo automatizado. Cada diagnóstico emitido por el modelo genera un archivo `.txt` independiente indexado por marca de tiempo (`reporte_[Agente]_[Fecha]_[Hora].txt`), ideal para entregar bitácoras académicas ante la SEP (INFOTEC) o registros operativos en laboratorios avanzados de IA (Lab-MexIA). El archivo `.gitignore` local asegura que estas evidencias sensibles queden excluidas del repositorio público.

---
*Desarrollado de forma local como proyecto integrador para el ecosistema de ciberseguridad avanzada y automatización inteligente.*
