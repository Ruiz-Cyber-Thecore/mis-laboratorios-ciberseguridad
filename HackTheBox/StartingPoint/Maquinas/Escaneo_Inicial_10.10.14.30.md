# Reporte Técnico: Escaneo de Infraestructura Básica
**Plataforma:** Hack The Box (HTB)  
**Módulo:** Starting Point  
**Categoría:** Red Team / Reconocimiento  

---

## 1. Identificación del Objetivo (MV)
Detalles técnicos de la Máquina Virtual asignada por el laboratorio para el análisis ofensivo:

* **Dirección IP de la Víctima:** `10.10.14.30`
* **Entorno de Ataque:** Pwnbox (Instancia Linux basada en la nube provista por HTB)
* **Estado del Reto:** Completado con éxito (Cuestionario inicial aprobado)

---

## 2. Fase de Reconocimiento y Escaneo
Para identificar los vectores de entrada potenciales, se procedió a realizar un análisis de puertos utilizando la herramienta de escaneo de red por excelencia en el sector.

### Comando Ejecutado:
```bash
nmap -sV 10.10.14.30
