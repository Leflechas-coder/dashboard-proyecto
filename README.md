# Las redes sociales en el bienestar propio

Este proyecto nació en el primer semestre de Ingeniería de Datos e Inteligencia Artificial como una forma práctica de responder a una inquietud muy cotidiana. Es un dashboard interactivo hecho con Python y Streamlit para entender cómo el tiempo frente a las pantallas termina afectando nuestro descanso y nuestros hábitos diarios.

## Contexto y pregunta guía

Cuando entras a la universidad, una de las primeras cosas que se desordena es la rutina. Entre clases, entregas y la costumbre de quedarse viendo el celular antes de dormir, las redes sociales van ganando terreno sin que uno lo note y le quitan horas al sueño, al estudio y al ejercicio. Al ver que esto nos pasaba tanto a nosotros como a nuestros compañeros, quisimos dejar de suponer y comprobarlo con datos reales, lo cual nos llevó a nuestra pregunta:

> **¿Cómo las redes sociales pueden perjudicar en el bienestar propio?**

## Sobre los datos

Trabajamos con el conjunto de datos `student_sleep_patterns.csv` porque retrata exactamente el entorno universitario: estudiantes lidiando con cargas académicas y pantallas todo el día. De toda la base de datos, filtramos únicamente las cinco variables que necesitábamos para medir el equilibrio diario

## Qué hace el dashboard

* **Vista limpia de los datos:** Al subir el archivo CSV, la aplicación muestra una tabla únicamente con las cinco columnas del estudio para no distraer con información innecesaria.
* **Resumen rápido:** En la parte superior aparecen cinco tarjetas con los promedios generales de sueño, estudio, tiempo en pantalla, actividad física y calidad de descanso.
* **Comparación de hábitos:** Incluye un selector múltiple para elegir qué actividades comparar en una gráfica de barras y ver cómo se reparten las horas del día.
* **Filtro por tiempo en pantalla:** Tiene una barra deslizante (entre 1 y 4 horas) que recalcula en tiempo real cómo cambian los promedios de sueño, descanso y estudio según el límite de exposición a pantallas.
* **Relación entre variables:** Al final hay un gráfico de dispersión para cruzar el tiempo en pantalla contra el sueño o el estudio, con un interruptor para ver la línea de tendencia promedio sin puntos amontonados.

## Herramientas utilizadas

* **Python**
* **Streamlit** para construir la interfaz web y las gráficas interactivas.
* **Pandas y NumPy** para leer, filtrar y calcular los promedios de los datos.