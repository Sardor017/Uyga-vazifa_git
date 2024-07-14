import streamlit as st
import pandas as pd
import time
import matplotlib.pyplot as plt
import seaborn as sns


st.write("# Dasturlash sohasidagi mutahassislarning maoshlari")

salary = pd.read_csv("Dataset salary 2024.csv")

salary = salary[salary["employment_type"] == "FT"]
salary = salary[salary["company_location"] == "US"]
salary = salary[salary["employee_residence"] == "US"]
salary = salary.drop(["salary","salary_currency","employment_type","company_location","employee_residence"], axis = "columns")

st.write("Bitta sohada faqat 3ta mutaxassis ma'lumotlari boshqasida esa 1000 tasini bor. Filtrlash uchun")
bin = st.select_slider(
    "Son kiriting:",
    options=list(range(20, 501)))
st.write("Tanlangan son:", bin)

fig, ax = plt.subplots()
job_title_value_counts = salary["job_title"].value_counts()
filtered_job_title = job_title_value_counts[job_title_value_counts > bin]
job = filtered_job_title.index
maosh_filtered = salary[salary["job_title"].isin(job)]
maosh = maosh_filtered.groupby("job_title")["salary_in_usd"].mean()
df_combined = pd.DataFrame({
    'job_title': job,
    'maosh': maosh
})
sns.scatterplot(x = job, y = maosh, data = df_combined)
plt.xticks(rotation = 90)
st.pyplot(fig)

st.write("## Tajriba bo'yicha mutahassislar soni")
st.write("### Asosan Senior lavozimidagilar ma'lumotlari yig'ilgan")
fig, ax = plt.subplots(figsize=(10, 5))
lavozimi = salary["experience_level"]
sns.countplot(x = lavozimi, data = salary)
st.pyplot(fig)

st.write("## Sohalar bo'yicha soni:")
bin = st.select_slider(
    "Son kiriting:",
    options=list(range(30, 301)))
st.write("Tanlangan son:", bin)
fig, ax = plt.subplots(figsize=(10,5))
job_title_value_counts = salary["job_title"].value_counts()
filtered_job_titles = job_title_value_counts[job_title_value_counts > bin]
jobs = filtered_job_titles.index
df = salary[salary["job_title"].isin(jobs)]
sns.countplot(x = df["job_title"], order = jobs, data=df)
plt.xticks(rotation = 90)
st.pyplot(fig)


st.write("## Maoshlarning o'sish va pasayishi tahlili:")
bin = st.select_slider(
    "Son kiriting:",
    options=list((300,350,400,450,500)))
st.write("Tanlangan son:", bin)
fig, ax = plt.subplots(figsize=(10,7))
job_title_value_counts = salary["job_title"].value_counts()
filtered_job_title = job_title_value_counts[job_title_value_counts > bin]
job = filtered_job_title.index
maosh_filtered = salary[salary["job_title"].isin(job)]
maosh = maosh_filtered.groupby("job_title")["salary_in_usd"].mean()
df = maosh_filtered
sns.lineplot(x = "work_year", y = "salary_in_usd", data = df,
            style = "job_title", hue = "job_title", markers=True, ci=None)
plt.xticks(rotation = 90)
st.pyplot(fig)