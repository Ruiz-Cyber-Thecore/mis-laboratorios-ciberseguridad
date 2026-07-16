# 🔎 Caso Práctico: Fundamentos de Log Management (LetsDefend)

Este documento detalla la metodología de resolución para el módulo introductorio de Gestión de Logs en LetsDefend.

## 🎯 Objetivos de Aprendizaje
*   Comprender la centralización de logs (Proxy, Firewalls, DNS).
*   Aprender a realizar búsquedas eficientes utilizando indicadores de compromiso (IoCs).
*   Correlacionar logs de red con protocolos de capa de aplicación.

---

## 🛡️ Preguntas Clave y Resolución Forense

### 1. ¿Qué dirección IP de origen se introdujo en la URL 'https://github.com/apache/flink/compare'?

*   **IoC de Búsqueda:** `apache/flink/compare` (Búsqueda específica para reducir el ruido).
*   **Metodología:** Al ingresar el término en el buscador de la base de datos de logs, se filtraron miles de registros irrelevantes, devolviendo el evento exacto de acceso al repositorio de GitHub.
*   **Análisis del Registro:** El campo `source_address` contenía la dirección interna del host afectado.
*   **Respuesta:** `172.16.17.54`

---

### 2. ¿Cuál es el tipo de log que tiene un puerto de destino de 52567 y una IP de origen de 8.8.8.8?

*   **Filtros de Búsqueda:** `source_address:"8.8.8.8" AND destination_port:52567`
*   **Análisis de Red:** 
    *   La IP de origen es `8.8.8.8` (DNS público de Google) respondiendo desde el puerto de origen `53`.
    *   La IP de destino es la IP pública externa de nuestra organización (`3.134.39.220`) en el puerto efímero de retorno `52567`.
*   **Clasificación del Log:** El sistema clasifica de forma inteligente este evento por su protocolo de capa de aplicación y no solo por la capa de red.
*   **Respuesta:** `DNS`
---

📥 **Descarga Ejecutiva:** Para una visualización ejecutiva, formal y con mis datos de contacto, puedes descargar mi [Cuaderno de Analista de SOC (PDF)](../../assets/docs/Cuaderno_SOC_Guillermo_Ruiz.pdf).
