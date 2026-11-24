import pandas as pd
import streamlit as st
import numpy as np

st.set_page_config(page_title="Las redes sociales en el bienestar propio",layout="centered")



st.title("Las redes sociales en el bienestar propio")
st.subheader("¿Cómo las redes sociales pueden perjudicar en el bienestar propio?")

archivo = st.file_uploader("Sube un archivo CSV con datos de redes sociales", type=["csv"])

if archivo:
    df = pd.read_csv(archivo)
    columnas = [
    "Sleep_Duration",
    "Study_Hours",
    "Screen_Time",
    "Physical_Activity",
    "Sleep_Quality"
]

    st.dataframe(df[columnas])

    duracion = df["Sleep_Duration"]
    horas_estudio = df["Study_Hours"]
    tiempo_pantalla = df["Screen_Time"]
    actividad_fisica = df["Physical_Activity"]
    calidad_sueño = df["Sleep_Quality"]

    promedio_duracion = np.mean(duracion)
    promedio_horas_estudio = np.mean(horas_estudio) 
    promedio_tiempo_pantalla = np.mean(tiempo_pantalla)
    promedio_actividad_fisica = np.mean(actividad_fisica)
    promedio_calidad_sueño = np.mean(calidad_sueño)

    st.subheader("Estadísticas de Bienestar")
    col1,col2,col3,col4,col5 = st.columns(5)

    col1.metric(f"promedio duración",  f"{promedio_duracion:.2f}" )
    col2.metric(f"promedio_horas_estudio",  f"{promedio_horas_estudio:.2f}" )
    col3.metric(f"promedio_tiempo_pantalla",  f"{promedio_tiempo_pantalla:.2f}" )
    col4.metric(f"promedio_actividad_fisica",  f"{promedio_actividad_fisica:.2f}" )
    col5.metric(f"promedio_calidad_sueño",  f"{promedio_calidad_sueño:.2f}" )

    datos_grafica = pd.DataFrame({
    "Hábito": ["Sueño", "Estudio", "Tiempo en pantalla", "Actividad física"],
    "Horas al día": [
        np.mean(duracion),
        np.mean(horas_estudio),
        np.mean(tiempo_pantalla),
        np.mean(actividad_fisica) / 60
    ]
        })
    st.subheader("Comparación de hábitos de bienestar")
    seleccion = st.multiselect(
    "Selecciona los hábitos que deseas comparar:",
    options=["Sueño", "Estudio", "Tiempo en pantalla", "Actividad física"],
    default=["Sueño", "Tiempo en pantalla"]
    )
    
    boton_seleccion = st.button("Mostrar gráfica")
    if boton_seleccion:
        if seleccion:
            datos_filtrados = datos_grafica[datos_grafica["Hábito"].isin(seleccion)]
            st.bar_chart(
        datos_filtrados,
        x="Hábito",
        y="Horas al día",
        color="Hábito",
        width=400,
        height=520,
        use_container_width=False
    )
        else:
            st.warning("Selecciona al menos un hábito para mostrar la gráfica.")

    st.subheader("Habitos de bienestar según tiempo en pantalla")
    max_pantalla = st.slider(
        "Selecciona el máximo de horas en pantalla al día:",
        min_value=1.0,
        max_value=4.0,
        value=4.0,
        step=0.1
    )

    df_filtrado = df[df["Screen_Time"] <= max_pantalla]

    if not df_filtrado.empty:
        datos_pantalla = pd.DataFrame({
            "Indicador": ["Tiempo de sueño", "Calidad de sueño", "Tiempo en pantalla", "Actividad física", "Tiempo de estudio"],
            "Promedio": [
            np.mean(df_filtrado["Sleep_Duration"]),
            np.mean(df_filtrado["Sleep_Quality"]),
            np.mean(df_filtrado["Screen_Time"]),
            np.mean(df_filtrado["Physical_Activity"]/60),
            np.mean(df_filtrado["Study_Hours"])
        ]
    })

    st.bar_chart(
        datos_pantalla,
        x="Indicador",
        y="Promedio",
        color="Indicador",
        width=400,
        height=520,
        use_container_width=False
    )

    datos_dispersion = pd.DataFrame({
    "Tiempo en pantalla (h)": tiempo_pantalla,
    "Duración de sueño (h)": duracion,
    "Calidad de sueño": calidad_sueño,
    "Horas de estudio (h)": horas_estudio,
    
})
    st.subheader("dispersión de hábitos de bienestar según tiempo en pantalla")

    comparar_con = st.selectbox(
    "Elige qué variable comparar contra el tiempo en pantalla:",
    options=["Duración de sueño (h)", "Calidad de sueño", "Horas de estudio (h)"]
)

    ver_tendencia = st.toggle("Mostrar promedio limpio por hora de pantalla (sin puntos encimados)")

    if ver_tendencia:
        tendencia = datos_dispersion.groupby("Tiempo en pantalla (h)", as_index=False).mean()
        st.line_chart(
        tendencia,
        x="Tiempo en pantalla (h)",
        y=comparar_con,
        height=420
    )
    else:
        st.scatter_chart(
        datos_dispersion,
        x="Tiempo en pantalla (h)",
        y=comparar_con,
        color="Calidad de sueño",
        height=420
    )
else:
    st.warning("Por favor, sube un archivo CSV para continuar con el análisis.") 