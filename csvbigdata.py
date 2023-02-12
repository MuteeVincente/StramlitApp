
# VINCENT MUTETHIA ,SCT211-0017/2019
# ASSIGNMENT 2
# SCIENTIFIC COMPUTING
# build violin plots for the data set of lifeExp,population and GDP for the year 2007(use seaborn for guidance)....then use streamlit to present the data inform of a  data app for the above data sets....then present the assignmen
import seaborn as sns
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("VIOLIN PLOT WITH STREAMLIT")
st.subheader("ASSIGNMENT 2")
# Load data from a CSV file
st.subheader("VINCENT MUTETHIA")
st.subheader('SCT211-0017/2019')

data = pd.read_csv("gapminder_with_codes.csv")
data_2007 = data[data['year']==2007][['gdpPercap', 'pop', 'lifeExp']]

# Plot the data using a violin plot
fig, ax = plt.subplots()
sns.violinplot(data=data_2007, ax=ax)
plt.title("GDP, Population, and Life Expectancy in 2007\n", fontweight='bold')

ax.set_xlabel("Population,GDP,Life Expectancy", fontweight='bold')
ax.set_ylabel("Values", fontweight='bold')
# Display the plot in the Streamlit app
st.pyplot(fig)

st.set_option('deprecation.showPyplotGlobalUse', False)
