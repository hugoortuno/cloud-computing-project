{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'functions'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[2], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mfunctions\u001b[39;00m\n\u001b[0;32m      3\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mmain\u001b[39m():\n\u001b[0;32m      4\u001b[0m \u001b[38;5;250m  \u001b[39m\u001b[38;5;124;03m\"\"\"\u001b[39;00m\n\u001b[0;32m      5\u001b[0m \u001b[38;5;124;03m  Función principal que ejecuta el análisis de sentimiento.\u001b[39;00m\n\u001b[0;32m      6\u001b[0m \u001b[38;5;124;03m  \"\"\"\u001b[39;00m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'functions'"
     ]
    }
   ],
   "source": [
    "import functions\n",
    "\n",
    "def main():\n",
    "  \"\"\"\n",
    "  Función principal que ejecuta el análisis de sentimiento.\n",
    "  \"\"\"\n",
    "  reseñas = [\n",
    "      \"Este producto es excelente. Lo recomiendo.\",\n",
    "      \"No me gustó este producto. Es de mala calidad.\",\n",
    "      \"El producto está bien, pero podría ser mejor.\"\n",
    "  ]\n",
    "\n",
    "  resultados = []\n",
    "  for reseña in reseñas:\n",
    "    sentimiento = functions.analizar_sentimiento(reseña)\n",
    "    resultados.append({'texto': reseña, **sentimiento})\n",
    "\n",
    "  functions.guardar_resultados(resultados)\n",
    "\n",
    "  print(\"Análisis de sentimiento completado. Resultados guardados en BigQuery.\")\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "  main()"
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
