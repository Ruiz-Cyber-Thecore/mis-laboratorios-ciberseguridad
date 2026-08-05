# Automated English Language Assistant (Ollama)

A specialized AI teaching assistant built on top of `qwen2.5-coder:1.5b` using Ollama to enhance professional English proficiency (A1-B1) through interactive technical practice and real-time grammar feedback.

## Overview
This custom LLM setup is designed to accelerate language acquisition for technical environments. It acts as an interactive language coach that provides real-time correction in Spanish while keeping conversations strictly in English.

## Features
- **Target Proficiency**: A1-B1 intermediate communication.
- **Bilingual Contextual Feedback**: Corrects grammar/spelling errors in English and explains linguistic rules concisely in Spanish under structured headers (`Correction:` / `Explicación:`).
- **Continuous Engagement**: Dynamically asks follow-up questions to promote continuous practice.

## Configuration Parameters
- **Base Model**: `qwen2.5-coder:1.5b`
- **Temperature**: `0.3` (Optimized for deterministic, accurate grammar evaluation)
- **Top_P**: `0.8`
- **Context Window**: `4096` 

## Setup & Execution

1. **Pull the base model**:
   ```bash
   ollama pull qwen2.5-coder:1.5b
   ```

2. **Build the custom model**:
   ```bash
   ollama create ingles-teacher -f ./Modelfile
   ```

3. **Launch the session**:
   ```bash
   ollama run ingles-teacher
   ```
