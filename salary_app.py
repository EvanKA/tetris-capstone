import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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
plt.rcParams.update({'font.size':5.5}) # change font size of the visualization
"## Data Jobs Annual Salary Visualization in USD"
fig, ax = plt.subplots(nrows=3, ncols=2)
fig.tight_layout(pad=3.0, w_pad=5.0, h_pad=5.0)
bins = np.arange(0, 610000, 10000)
ax[0][0].hist(ds_salary_df_1['salary_in_usd'], bins=bins)
ax[0][0].set_title('Annual salary distribution (USD)')
ax[0][0].set_xlabel('salary (USD)')
ax[0][0].set_ylabel('frequency')
year_salary = ds_salary_df_1.groupby('work_year')['salary_in_usd'].mean()
ax[0][1].bar(year_salary.index, year_salary)
ax[0][1].set_xticks([2020, 2021, 2022])
ax[0][1].set_title('Annual salary by year (USD)')
ax[0][1].set_xlabel('year')
ax[0][1].set_ylabel('salary (USD)')
xp_salary = ds_salary_df_1.groupby('experience_level')['salary_in_usd'].mean()
ax[1][0].bar(xp_salary.index, xp_salary)
ax[1][0].set_title('Annual salary by experience level (USD)')
ax[1][0].set_xlabel('experience level')
ax[1][0].set_ylabel('salary (USD)')
size_salary = ds_salary_df_1.groupby('company_size')['salary_in_usd'].mean()
ax[1][1].bar(size_salary.index, size_salary)
ax[1][1].set_title('Annual salary by company size (USD)')
ax[1][1].set_xlabel('company size')
ax[1][1].set_ylabel('salary (USD)')
type_salary = ds_salary_df_1.groupby('employment_type')['salary_in_usd'].mean()
ax[2][0].bar(type_salary.index, type_salary)
ax[2][0].set_title('Annual salary by employment type (USD)')
ax[2][0].set_xlabel('employment type')
ax[2][0].set_ylabel('salary (USD)')
wfa_salary = ds_salary_df_1.groupby('remote_ratio')['salary_in_usd'].mean()
ax[2][1].bar(wfa_salary.index, wfa_salary, width=40)
ax[2][1].set_xticks([0, 50, 100])
ax[2][1].set_title('Annual salary by remote ratio (USD)')
ax[2][1].set_xlabel('remote ratio (0=WFO, 50=hybrid, 100=WFA)')
ax[2][1].set_ylabel('salary (USD)')

fig