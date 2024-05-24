import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

st.header('Venta de vehículos')

hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Creación de un histograma precio-modelo')

    his_car = px.histogram(car_data, x="price", y="model")
    his_car.show()

    build_histogram = st.checkbox('Construir un histograma')

    if build_histogram:
        st.write('Construir un histograma para la columna precio-modelo')

st.plotly_chart(his_car, use_container_width=True)

scatter_button = st.button('construyendo gráfico de dispersión')

if scatter_button:
    st.write('Creación de gráfico de dispersión kilometros-precio')

    scatt_car = px.scatter(car_data, x="odometer", y="price")
    scatt_car.show()
