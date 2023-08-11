# Esto no es un completo

Proyecto para implementar, monitorear y desplegar modelos de Machine Learning en producción.

## Objetivo 
El objetivo del proyecto es desarrollar un modelo de Computer Vision que automáticamente realice una clasificación binaria sobre imagenes.

La idea es desarrollar una prueba de concepto de un modelo relativamente sencillo pero estable, mantenible, escalable y eficiente utilizando un conjunto de tecnologías abiertas e infraestructura gratuita así como las mejores prácticas de Data, Desarrollo y Despliege Continuo (DC/CD/CI)

## Arquitectura
El sistema consta de:

- un frontend donde los usuarios pueden enviar imagenes para ser procesadas
- un backend de inferencia que corra el actual modelo en producción (API)
- una pipeline para procesar datos
- Feature Storage para guaradar las imagenes, modelos y funciones de procesamiento entre los procesos de entrnamiento y servicio
- almacenamiento de las metricas de monitoreo en una base de datos

![alt text](https://github.com/pippo-sci/NotHotDog/blob/BaseTransferLearning_CNN/Architecture.drawio.png?raw=true)

### Resultados experimentales:

|Model|Preprocess|Accuracy|
|--|--|--|
|Transfer Learning. Resnet 50 + (8\*8\*2048 - flatten), (256 - relu), (2 - softmax)|Input (250,250,3), Optimizer ADAM lr = 0.001, 10 epoch |0.802 |
|Stacked Model (LogReg, KNeighbors, DT)|Hog features, Canny edges, raw histograms|0.620|
|Linear SVM -Default|Color Histogram. bin size 32, RGB, normalized|0.82|
|Decision Tree -Default|Color Histogram. bin size 32, RGB, normalized|0.87|
|Random Forest -Default|Color Histogram. bin size 32, RGB, normalized|0.93|
|Stacked RandomForest Linear SVM|Color Histogram. bin size 32, RGB, normalized|0.92|


### Creditos
- Basado en la serie Silicon Valley con la aplicacion See Food.

@Los piratas
