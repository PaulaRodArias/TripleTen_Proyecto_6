import pandas as pd
import plotly.express as px
import streamlit as st
        
st.header('Análisis exploratorio de datos - Modelos de autos según distancia recorrida')

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón hist
scat_button = st.button('Construir gráfico de dispersión') #diagrama de dispersión  

if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches según distancia recorrida')
    
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if scat_button:
    #escribir mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches en relación precio-distancia recorrida')

    #crear diagrama de dispersión 
    fig_2 = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
    
    #mostrar gráfito de dispersión con plotly 
    st.plotly_chart(fig_2,_use_container_width=True)