import pandas as pd
import plotly.express as px
import streamlit as st


car_data = pd.read_csv('vehicles_us.csv')

st.header('Visualizador de Datos', divider="violet")
dataviewer = st.checkbox('Mostrar Datos')
describeviewer = st.checkbox('Mostrar estadisticas de datos')

if dataviewer:
    st.dataframe(car_data)

if describeviewer:
    st.dataframe(car_data.describe())

st.header('Venta de vehículos')

hist_button = st.button('Construir histograma')
scatter_button = st.button('construir gráfico de dispersión')

if hist_button:
    st.subheader('Creación de un histograma precio-modelo')
    his_car = px.histogram(car_data, y="price", x="model")
    st.plotly_chart(his_car, use_container_width=True)


if scatter_button:
    st.subheader('Creación de gráfico de dispersión kilometros-precio')
    scatt_car = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(scatt_car, use_container_width=True)
