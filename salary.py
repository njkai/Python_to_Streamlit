import streamlit as st
import polars as pl
import pandas as pd
import altair as alt

df = (pl.read_csv('~/Downloads/IT_Salary_Survey_EU_2020.csv', has_header=True, dtypes={'Have you been forced to have a shorter working week (Kurzarbeit)? If yes / how many hours per week':pl.Float32}))
    
df2 = df.select(["Age","Gender","Total years of experience"]).filter(pl.col("Age").is_not_null()).filter(pl.col("Total years of experience").is_not_null()).filter(pl.col("Gender").is_not_null())

df3 = df2.select("Age").unique().to_pandas().sort_values(by=['Age'])

# sb=st.sidebar.selectbox('How old?', (df3['Age']))
# sb

# sbs=st.sidebar.slider('Select a range of values',20,69)
# sbs

line=alt.Chart(df2, width=860, height=650).mark_line().encode(
    alt.X('Age').scale(zero=False),
    alt.Y('Total years of experience', aggregate='average', type='quantitative', axis=alt.Axis(title="AVG / Total Years of Experience")))
circle=alt.Chart(df2, width=860, height=650).mark_circle().encode(
    alt.X('Age').scale(zero=False),
    alt.Y('Total years of experience').scale(zero=False),
    color='Gender')
line.mark_line() + circle.mark_circle()

bar=alt.Chart(df).mark_bar().encode(x="Company type", y="Company size",text='count()')
bar.mark_bar(color='red') + bar.mark_text(align='center',color='white')

base = alt.Chart(df,width=1000).encode(
    x='Seniority level',
    y="Have you lost your job due to the coronavirus outbreak?",
    text='count()')
base.mark_bar(color='blue') + base.mark_text(align='center',color='white',size=16)

circle2=alt.Chart(df2,width=860).mark_circle().encode(
    alt.X('Age').scale(zero=False),
    alt.Y('Total years of experience'),
    color='Gender')
line2=alt.Chart(df2, width=860).mark_line().encode(
    alt.X('Age').scale(zero=False),
    alt.Y('Total years of experience', aggregate='average', type='quantitative').scale(zero=False, padding=1),
    color='Gender')
circle2.mark_circle() + line2.mark_line()

if __name__ == "__main__":
    salary.run(host='0.0.0.0', port='8080')
