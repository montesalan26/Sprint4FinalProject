import pandas as pd
import streamlit as st
import plotly.express as px
import altair as alt
from matplotlib import pyplot as plt

st.header("Used Car Sale Analysis.")

cars_for_sale = pd.read_csv("/Users/monte/Desktop/Sprint4Project/vehicles_us.csv")
print(cars_for_sale.info())

cars_for_sale.head()

st.write(pd.DataFrame(cars_for_sale).head())

duplicated_cars = cars_for_sale.duplicated().sum()

print(f"There are {duplicated_cars} duplicated vehicles in this DataFrame.")

cars_for_sale["date_posted"] = pd.to_datetime(cars_for_sale["date_posted"])

median_model_year = cars_for_sale["model_year"].median()

cars_for_sale["model_year"] = cars_for_sale["model_year"].fillna(median_model_year)

cars_for_sale["model_year"].isna().sum()

average_model_year = cars_for_sale["cylinders"].median()

cars_for_sale["cylinders"] = cars_for_sale["cylinders"].fillna(average_model_year)

cars_for_sale["cylinders"].isna().sum()

average_odometer = cars_for_sale.groupby("model_year")["odometer"].transform('mean')

cars_for_sale["odometer"] = cars_for_sale["odometer"].fillna(average_odometer)

cars_for_sale["odometer"].isna().sum()

print(cars_for_sale)

agree = st.checkbox('Do You want to see this beautiful DataFrame?')

if agree:
    st.write(cars_for_sale.head())

df = pd.DataFrame(
    cars_for_sale)

c = alt.Chart(cars_for_sale).mark_circle().encode(
    x='condition', y='price')

st.write(c)

cars_for_sale["transmission"].value_counts().plot(kind="bar",
                                                  title="Transmission of Vehicles for Sale",
                                                  ylabel="Frequency")



cars_for_sale["condition"].value_counts().plot(kind="bar",
                                               ylabel="Frequency",
                                               title="Vehicle Condition")


cars_for_sale["fuel"].value_counts().plot(kind="bar",
                                          ylabel="Frequency",
                                          title="Types of Fuel")

st.header('This is a header with a divider', divider='rainbow')
st.header('_Streamlit_ is :blue[cool] :sunglasses:')

data = cars_for_sale

# Sample data (replace with your actual data)
df = pd.DataFrame(data, columns=['fuel'])

# Configure histogram options (optional)
num_bins = 10  # Adjust the number of bins as needed
hist_fig, hist_ax = plt.subplots()  # Create a figure and axis

# Create the histogram
hist_ax.hist(cars_for_sale['fuel'], bins=num_bins, edgecolor='black')
hist_ax.set_title('Histogram of Values')
hist_ax.set_xlabel('Value')
hist_ax.set_ylabel('Frequency')

# Display the histogram in Streamlit
st.pyplot(hist_fig)


plt.show()