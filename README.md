# Proyecto de Análisis de sentimiento con Google Cloud NLP API

Este proyecto demuestra cómo usar la API de Google Cloud Natural Language para analizar el sentimiento de las reseñas de productos y almacenar los resultados en BigQuery.

## Repositorio de GitHub

[Repositorio de GitHub](https://github.com/hugoortuno/cloud-computing.project)

## Autor

Hugo Ortuño Suárez

* [Perfil de LinkedIn](https://www.linkedin.com/in/hugo-ortuño-suarez/)
* [Perfil de GitHub](https://github.com/hugoortuno)

## Descripción

El proyecto utiliza las siguientes herramientas de Google Cloud:

* **Natural Language API:** Para analizar el sentimiento de las reseñas.
* **BigQuery:** Para almacenar y analizar las reseñas y los resultados del análisis.

## Estructura del proyecto

```
cloud-computing.project/
├── functions.py
└── main.py
```

* **`functions.py`:** Contiene las funciones para analizar el sentimiento y guardar los resultados en BigQuery.
* **`main.py`:**  Ejecuta el análisis de sentimiento utilizando las funciones de `functions.py`.

## Instrucciones

1. **Clona el repositorio:**
   ```bash
   git clone [https://github.com/hugoortuno/cloud-computing.project.git](https://github.com/hugoortuno/cloud-computing.project.git)


2. **Crea un entorno virtual:**
   ```bash
   python -m venv .venv
   ```

3. **Activa el entorno virtual:**
   ```bash
   .\.venv\Scripts\activate
   ```

4. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Crea un proyecto en Google Cloud.**

6. **Habilita la API de Natural Language.**

7. **Crea un dataset y una tabla en BigQuery.**

8. **Configura las credenciales de Google Cloud:**
   * Descarga el archivo JSON de credenciales de tu proyecto de Google Cloud.
   * Establece la variable de entorno `GOOGLE_APPLICATION_CREDENTIALS` con la ruta al archivo JSON.

9. **Ejecuta el código:**
   ```bash
   python main.py
   ```

10. **Verifica los resultados en BigQuery.**


## Visualizaciones (opcional)

Puedes usar Google Data Studio para crear visualizaciones interactivas con los datos almacenados en BigQuery.

## Notas

* Asegúrate de tener los permisos necesarios en BigQuery para escribir datos en la tabla.
* Reemplaza `"tu_proyecto.tu_dataset.tu_tabla"` en `functions.py` con el ID de tu proyecto, dataset y tabla en BigQuery.
```
