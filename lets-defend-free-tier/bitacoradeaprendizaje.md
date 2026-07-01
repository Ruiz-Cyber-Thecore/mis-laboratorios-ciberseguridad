# Bitácora de Aprendizaje: De la Defensa al Ataque

**Fecha:** 1 de julio de 2026
**Plataformas:** LetsDefend ➡️ Hack The Box (Starting Point)
**Objetivo actual:** Entender el lado ofensivo para mejorar mis habilidades defensivas.

---

## 1. Contexto: El origen en LetsDefend
Comencé analizando alertas de seguridad en **LetsDefend**. Para ser un mejor Analista SOC (Blue Team), identifiqué la necesidad de aprender cómo operan los atacantes reales, lo que me llevó a experimentar en los laboratorios ofensivos de **Hack The Box**.

---

## 2. Fase de Reconocimiento (Hack The Box)
Inicié el análisis de mi primera máquina en la infraestructura de HTB para simular las fases iniciales de un ciberataque.

*   **Entorno utilizado:** Pwnbox (Instancia de ataque en la nube)
*   **IP Objetivo Analizada:** `10.10.14.30`

### Comando de escaneo ejecutado:
```bash
nmap -sV 10.10.14.30
```

### 🕵️‍♂️ Análisis de Resultados con Asistencia de IA
Tras lanzar el escaneo, exporté los puertos abiertos y utilicé un LLM para agilizar la priorización de vulnerabilidades.

*   **Mi Prompt Utilizado:** *"Actúa como un Analista SOC Senior. Analiza este output de Nmap [pegar output] e identifica los 2 vectores de ataque más probables basados en las versiones de los servicios."*
*   **Sugerencia de la IA:** La IA identificó que el servicio corriendo en el puerto HTTP tenía una vulnerabilidad conocida de ejecución remota de código (RCE).
*   **Validación Humana (Mi Acción):** Verifiqué en Exploit-DB que el exploit sugerido correspondiera exactamente a la versión detectada para evitar falsos positivos de la IA.
## 3. Resolución y Conclusiones del Módulo Inicial

Una vez completado el escaneo inicial, utilicé la información de los puertos abiertos para responder las preguntas guía del módulo en la plataforma.

### 🔑 Hallazgos Clave
*   **Servicio Vulnerable:** Se identificó la versión exacta del servicio para responder los cuestionarios básicos de HTB.
*   **Captura de la Flag:** Se localizó el archivo `flag.txt` en el sistema para completar el laboratorio con éxito.

---

## 🛡️ Mi Flujo de Aprendizaje con IA en este Curso
Para asimilar mejor los conceptos de este curso de inicio, utilicé la Inteligencia Artificial de la siguiente manera:

1.  **Explicación de Parámetros:** Le pedí a la IA que me desglosara el significado exacto de los modificadores de Nmap (`-sV`) para entender qué ocurre a nivel de red y no solo copiar el comando.
2.  **Glosario Personalizado:** Usé prompts para que la IA me explicara con analogías sencillas conceptos nuevos como *Shell Reversa*, *Vulnerabilidad RCE* y *Protocolo SMB*.

---

## 🏁 Próximos Pasos
*   [ ] Completar la siguiente máquina del Starting Point (Nivel Básico).
*   [ ] Documentar los comandos de enumeración de directorios web (Gobuster/Dirbuster).
