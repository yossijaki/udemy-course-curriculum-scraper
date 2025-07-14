import requests

COURSE_SLUG = "curso-de-guitarra-desde-cero"

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
contenido = []
unidad_num = 1
video_num = 1

for item in items:
    if item["_class"] == "chapter":
        contenido.append(f"Unidad {unidad_num}: {item['title']}")
        video_num = 1
        unidad_num += 1
    elif item["_class"] == "lecture":
        contenido.append(f"  {video_num:02d} - {item['title']}")
        video_num += 1

# Paso 4: guardar archivos
with open("curriculum.txt", "w", encoding="utf-8") as f_txt, open("curriculum.md", "w", encoding="utf-8") as f_md:
    for linea in contenido:
        f_txt.write(linea + "\n")
        f_md.write(linea + "\n")

print("✅ Curriculum guardado en curriculum.txt y curriculum.md")
