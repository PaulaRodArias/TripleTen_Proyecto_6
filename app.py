import pandas as pd
import plotly.express as px
import streamlit as st
        
st.header('Análisis exploratorio de datos - Modelos de autos')

car_data = pd.read_csv(r'C:\Users\Lenovo\Desktop\TripleTen\Proyectos_Tripleten\Proyecto_Sprint6\TripleTen_Proyecto_6\vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón

if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    #crear diagrama de dispersión 
    fig_2 = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
    

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

    #mostrar gráfito de dispersión con plotly 
    st.plotly_chart(fig2_use_container_width=True)