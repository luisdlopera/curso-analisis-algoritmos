# Entorno de Trabajo — Semana 02

Guía rápida para la configuración y reproducción del entorno virtual único en la raíz del repositorio (`curso-analisis-algoritmos/`).

## 1. Creación y Activación del Entorno Virtual

Desde la raíz del repositorio:

```bash
# Crear el entorno virtual aislado
python3 -m venv venv

# Activar el entorno virtual en macOS / Linux
source venv/bin/activate

# Verificar que la terminal muestre el prefijo (venv) y validar entorno limpio
pip list
```

## 2. Instalación y Congelamiento de Dependencias

Con el prefijo `(venv)` activo en la terminal:

```bash
# Instalar matplotlib para generación de gráficos
pip install matplotlib

# Congelar dependencias exactas en la raíz del proyecto
pip freeze > requirements.txt
```

## 3. Reproducción del Entorno en Otro Equipo

Para restaurar idénticamente las dependencias en cualquier máquina:

```bash
# Clonar repositorio y entrar a la raíz
cd curso-analisis-algoritmos

# Crear y activar nuevo venv
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias fijadas
pip install -r requirements.txt
```
