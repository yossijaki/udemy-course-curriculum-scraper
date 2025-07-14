# 🎓 Udemy Course Scraper

Este script en Python permite obtener y guardar el contenido estructurado de un curso público de [Udemy](https://www.udemy.com), incluyendo sus unidades y lecciones, usando la API pública de Udemy.

El resultado se guarda en dos archivos:

- `curriculum.txt`: versión en texto plano.
- `curriculum.md`: versión en formato Markdown.

---

## 📋 Requisitos previos

- Python **3.7 o superior**
- Acceso a internet
- Curso de Udemy público con URL accesible (sin autenticación)

---

## 📦 Instalación

### 1. Clona o descarga este repositorio

```bash
git clone https://github.com/tuusuario/udemy-scraper.git
cd udemy-scraper
```

### 2. Crea un entorno virtual (opcional pero recomendado)

```bash
python -m venv venv
```

### 3. Activa el entorno virtual

- En Windows:
  ```bash
  venv\Scripts\activate
  ```
- En macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

### 4. Instala las dependencias necesarias

Este script solo necesita `requests`, que puedes instalar con:

```bash
pip install -r requirements.txt
```

## 🚀 Uso

1. Asegúrate de tener activo tu entorno virtual (si usaste uno).
2. Ejecuta el script con:

   ```bash
   python scraper.py
   ```

3. Introduce el enlace del curso de Udemy cuando se te solicite. Ejemplo:
   ```less
   https: //www.udemy.com/course/curso-de-scraping/;
   ```
4. El script extraerá automáticamente el slug, procesará el contenido y generará dos archivos:
   - curriculum.txt
   - curriculum.md
5. Al finalizar, verás un mensaje de confirmación:
   ```bash
   ✅ Curriculum guardado en curriculum.txt y curriculum.md
   ```

## 🧪 Ejemplo de salida

### curriculum.md

```markdown
## Unidad 1: Introducción

1. Bienvenida
2. Cómo usar el curso

## Unidad 2: Fundamentos

1. Acordes básicos
2. Ejercicios prácticos
```

## ⚠️ Errores comunes

- ❌ Enlace inválido  
  Asegúrate de que el enlace tenga este formato:

```bash
https://www.udemy.com/course/nombre-del-curso/
```

- ❌ No se pudo obtener el ID del curso  
  El curso puede ser privado, inexistente o estar protegido por autenticación.

## 🛡️ Notas importantes

- Este script no descarga contenido multimedia ni materiales del curso.
- Solo se usa la API pública de Udemy para obtener la estructura del curso.
- Cumple con los Términos de uso de Udemy.

## 📄 Licencia

MIT License – libre para uso personal o educativo. No usar con fines comerciales sin autorización.
