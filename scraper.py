import requests
import re

# Solicitar el enlace del curso
curso_url = input("🔗 Ingresa el enlace del curso de Udemy: ").strip()

# Extraer el slug del enlace
match = re.search(r"udemy\.com/course/([^/]+)/?", curso_url)
if not match:
    print("❌ Enlace inválido. Asegúrate de que tenga el formato correcto, por ejemplo:")
    print("   https://www.udemy.com/course/curso-de-scraping/")
    exit()

COURSE_SLUG = match.group(1)

# Paso 1: obtener ID del curso
info = requests.get(f"https://www.udemy.com/api-2.0/courses/{COURSE_SLUG}/")
if info.status_code != 200:
    print("❌ No se pudo obtener el ID del curso.")
    exit()
course_id = info.json()["id"]

# Paso 2: obtener el curriculum
curriculum = requests.get(
    f"https://www.udemy.com/api-2.0/courses/{course_id}/public-curriculum-items/?page_size=1000"
)
if curriculum.status_code != 200:
    print("❌ No se pudo obtener el contenido del curso.")
    exit()

items = curriculum.json()["results"]

# Paso 3: procesar contenido
contenido_txt = []
contenido_md = []

unidad_num = 1
video_num = 1

for item in items:
    if item["_class"] == "chapter":
        unidad_titulo = f"Unidad {unidad_num}: {item['title']}"
        contenido_txt.append(unidad_titulo)
        contenido_md.append(f"## {unidad_titulo}")
        video_num = 1
        unidad_num += 1
    elif item["_class"] == "lecture":
        titulo = item['title']
        contenido_txt.append(f"  {video_num:02d} - {titulo}")
        contenido_md.append(f"{video_num}. {titulo}")
        video_num += 1

# Paso 4: guardar archivos
with open("curriculum.txt", "w", encoding="utf-8") as f_txt, open("curriculum.md", "w", encoding="utf-8") as f_md:
    for linea in contenido_txt:
        f_txt.write(linea + "\n")
    for linea in contenido_md:
        f_md.write(linea + "\n")

print("✅ Temario del curso guardado en curriculum.txt y curriculum.md")
