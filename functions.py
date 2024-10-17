{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from google.cloud import language_v1\n",
    "from google.cloud import bigquery\n",
    "\n",
    "def analizar_sentimiento(texto):\n",
    "  \"\"\"\n",
    "  Analiza el sentimiento de un texto usando la API de Google Cloud Natural Language.\n",
    "\n",
    "  Args:\n",
    "    texto: El texto a analizar.\n",
    "\n",
    "  Returns:\n",
    "    Un diccionario con la puntuación y la magnitud del sentimiento.\n",
    "  \"\"\"\n",
    "  client = language_v1.LanguageServiceClient()\n",
    "  document = language_v1.Document(content=texto, type_=language_v1.Document.Type.PLAIN_TEXT)\n",
    "  response = client.analyze_sentiment(request={'document': document})\n",
    "  sentiment = response.document_sentiment\n",
    "\n",
    "  return {'puntuacion': sentiment.score, 'magnitud': sentiment.magnitude}\n",
    "\n",
    "def guardar_resultados(resultados):\n",
    "  \"\"\"\n",
    "  Guarda los resultados del análisis de sentimiento en BigQuery.\n",
    "\n",
    "  Args:\n",
    "    resultados: Una lista de diccionarios con los resultados.\n",
    "  \"\"\"\n",
    "  client = bigquery.Client()\n",
    "  table_id = \"tu_proyecto.tu_dataset.tu_tabla\"  # Reemplaza con tu proyecto, dataset y tabla\n",
    "\n",
    "  # Configurar el esquema de la tabla\n",
    "  job_config = bigquery.LoadJobConfig(\n",
    "      schema=[\n",
    "          bigquery.SchemaField(\"texto\", \"STRING\"),\n",
    "          bigquery.SchemaField(\"puntuacion\", \"FLOAT\"),\n",
    "          bigquery.SchemaField(\"magnitud\", \"FLOAT\"),\n",
    "      ]\n",
    "  )\n",
    "\n",
    "  # Cargar los datos en la tabla\n",
    "  job = client.load_table_from_json(resultados, table_id, job_config=job_config)\n",
    "  job.result()  # Esperar a que se complete la carga"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": ".venv",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
