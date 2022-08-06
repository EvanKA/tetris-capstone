import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px

st.sidebar.write(
    '''
    # Data Jobs Salary Visualization in Developed Countries
    Made with **streamlit** by Evan Kurnia Alim
    '''
)
# magically displays data insights
'''
- Employees in developed countries typically earn more salary in average than in developing countries like Indonesia. 
- Full-time and contract employees typically earn much higher than part-time and flexible time employees. 
- Hybrid employees typically earn less than full WFA and full WFO. Full WFA employees typically earn higher than even full WFO.
- Salary distribution is right-skewed, i.e. there are very high earning employees in extremely rare cases.
- The salary tend to increase each year due to inflation, and the increase from 2021 to 2022 is much higher than that from 2020 to 2021.
- Dataset source: https://salaries.ai-jobs.net/download/salaries.csv
'''
# read from .csv file
ds_salary_df_1 = pd.read_csv('ds_salaries_clean.csv')
"## Data Jobs Annual Salary Visualization in USD"
fig, ax = plt.subplots(nrows=3, ncols=2)
plt.suptitle("Annual Salary Visualizations in USD")
ax[0][0].hist(ds_salary_df_1['salary_in_usd'])
ax[0][0].set_title('Annual salary distribution (USD)')
ax[0][0].set_xlabel('salary (USD)')
ax[0][0].set_ylabel('frequency')
year_salary = ds_salary_df_1.groupby('work_year')['salary_in_usd'].mean()
ax[0][1].bar(year_salary.index, year_salary)
ax[0][1].set_title('Annual salary by year (USD)')
ax[0][1].set_xlabel('year')
ax[0][1].set_ylabel('salary (USD)')
xp_salary = ds_salary_df_1.groupby('experience_level')['salary_in_usd'].mean()
size_salary = ds_salary_df_1.groupby('company_size')['salary_in_usd'].mean()
type_salary = ds_salary_df_1.groupby('employment_type')['salary_in_usd'].mean()
wfa_salary = ds_salary_df_1.groupby('remote_ratio')['salary_in_usd'].mean()
st.pyplot(fig)