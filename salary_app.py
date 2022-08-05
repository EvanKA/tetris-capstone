import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.sidebar.write(
    '''
    # Annual Salary Visualization App
    Made with **streamlit** by Evan Kurnia Alim
    '''
)

# read from .csv file
ds_salary_df_1 = pd.read_csv('ds_salaries_clean.csv')

"## Annual Salary Boxplot"
fig, ax = plt.subplots()
ax.boxplot(ds_salary_df_1['salary_in_usd'])
ax.set_title('Annual salary distribution (USD)')
ax.set_ylabel('salary')
st.pyplot(fig)

"## Average Annual Salary by Category"
categories = st.sidebar.selectbox('Select category: ', ('work_year', 'experience_level', 'company_size', 'employment_type', 'company_location', 'remote_ratio'))
grouped = ds_salary_df_1.groupby(categories)['salary_in_usd'].mean().sort_values(ascending=False)
st.write("Average Annual Salary by "+categories)
st.bar_chart(grouped)
