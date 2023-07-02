# Esto no es un completo

Proyecto para implementar, monitorear y desplegar modelos de Machine Learning en produccion.

## Objetivo 
El objetivo del proyecto es desarrollar un modelo de Computer Vision que automaticamente realice una clasificacion binaria sobre imagenes.

La idea es desarrollar una pruebade concepto de un modelo relativamente sencillo pero estable, mantenible, escalable y eficiente utilizando un conjunto de tecnologias abiertas e infraestructura gratuita asi como las mejores practicas de Data, Desarrollo y Despliege continuo (DC/CD/CI)

## Arquitectura
El sistema consta de:

- un frontend donde los usuarios pueden enviar imagenes para ser procesadas
- un backend de inferencia que corra el actual modelo en produccion
- una pipeline para procesar datos
- almacenamiento de las metricas de monitoreo en una base de datos

### Resultados experimentales:

|Model|Preprocess|Accuracy|
|--|--|--|
|Transfer Learning. Resnet 50 + (8\*8\*2048 - flatten), (256 - relu), (2 - softmax)|Input (250,250,3), Optimizer ADAM lr = 0.001, 10 epoch |0.802 |
|Stacked Model (LogReg, KNeighbors, DT)|Hog features, Canny edges, raw histograms|0.620|
|SVM -Default|Color Histogram. bin seize 32, RGB, normalized|0.82|
|Decision Tree -Default|Color Histogram. bin seize 32, RGB, normalized|0.87|

### Creditos
- Basado en la serie Silicon Valley con la aplicacion See Food.

@Los piratas
