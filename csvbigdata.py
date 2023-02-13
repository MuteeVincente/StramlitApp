import seaborn as sns  
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Violin Plot for GDP, Population, and Life Expectancy")

st.subheader("Vincent Mutethia, SCT211-0017/2019")
st.subheader("Assignment 2 - Scientific Computing")

# Load data from a CSV file
data = pd.read_csv("gapminder_with_codes.csv")
data_2007 = data[data['year']==2007]

# Plot the data using a violin plot
# GDP
fig, ax = plt.subplots()
sns.violinplot(data=data_2007, x='gdpPercap', ax=ax)
ax.set_ylabel("GDP", fontweight='bold')
ax.set_xlabel("Values", fontweight='bold')
plt.title("GDP in 2007\n", fontweight='bold')

# Display the plot in the Streamlit app
st.pyplot(fig)

# POPULATION 
fig2, ax2 = plt.subplots()
sns.violinplot(data=data_2007, x='pop', ax=ax2)
ax2.set_ylabel("Population", fontweight='bold')
ax2.set_xlabel("Values", fontweight='bold')
plt.title("Population in 2007\n", fontweight='bold')

st.pyplot(fig2)

# LIFE EXPECTANCY
fig3, ax3 = plt.subplots()
sns.violinplot(data=data_2007, x='lifeExp', ax=ax3)
ax3.set_ylabel("Life Expectancy", fontweight='bold')
ax3.set_xlabel("Values", fontweight='bold')
plt.title("Life Expectancy in 2007\n", fontweight='bold')

st.pyplot(fig3)
