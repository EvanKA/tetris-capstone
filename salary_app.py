import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.sidebar.write(
    '''
    # Annual Salary Visualization App
    Made with **streamlit** by Evan Kurnia Alim
    '''
)

# read from .csv file
ds_salary_df = pd.read_csv('ds_salaries.csv')
ds_salary_df_1 = ds_salary_df.drop(columns=['Unnamed: 0'])

"## Annual Salary Boxplot"
fig, ax = plt.subplots()
ax.boxplot(ds_salary_df_1['salary_in_usd'])
ax.set_title('Annual salary distribution (USD)')
ax.set_ylabel('salary')
st.pyplot(fig)

"## Average Annual Salary by Category"
