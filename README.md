# Docker_Alzheimer_Detector
Este repositorio contiene un contenedor Docker para ejecutar un modelo de detección de Alzheimer a partir de imágenes cerebrales.

El algoritmo acepta imágenes individuales como entrada, predice su clase (por ejemplo, No Impairment, Mild Cognitive Impairment, etc.), muestra la predicción junto con el porcentaje de seguridad y guarda el resultado en un archivo CSV.

---
## Construcción y ejecución 

- Para construir la imagen Docker, ejecuta el siguiente comando desde el directorio donde se encuentra el `Dockerfile`:

```bash
docker build -t alzheimer_detector .
```

- Para ejecutar la detección sobre una imagen específica:

```bash
docker run -v E:/00.Kaggle/23.Docker/Prueba_archivo_docker/:/data alzheimer_detector /data/Imagenes/NoImpairment(1).jpg
```

## Output

Los resultados se guardarán automáticamente en un archivo CSV llamado resultados.csv, con el siguiente formato:
| image      | prediction    | precision |
| ------------------- | ------------- | --------- |
| NoImpairment(1).jpg | No Impairment | 99.95     |
