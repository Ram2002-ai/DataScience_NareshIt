import streamlit as st
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

# set up the title and description of the app
# st.title('Sales data analysis for Retail Store')
# st.write('This app analyze sales data for various product categories')

st.markdown(
    """
    <h1 style='text-align: center; color: #2E86C1;'>
    📊 Sales Data Analysis for Retail Store
    </h1>
    <p style='text-align: center; font-size:18px;'>
    This app analyzes sales data for various product categories
    and provides meaningful insights.
    </p>
    """,
    unsafe_allow_html=True
)

# generate a synthetic sales data
def generate_data():
    np.random.seed(42)
    data={
        'prodct_id':range(1,21),
        'product_name':[f'Product{i}' for i in range(1,21)],
        'category':np.random.choice(['electronics','clothing','homes','sports'],20),
        'unit_sold':np.random.poisson(lam=20,size=20),
        'sale_date':pd.date_range(start='2023-01-01',periods=20,freq='D')
    }
    return pd.DataFrame(data)

sales_data=generate_data()

# display the sales data
st.subheader('sales data')
st.dataframe(sales_data)


# descriptive statestics
st.subheader('Descriptive statistics')
descriptive_stats=sales_data['unit_sold'].describe()
st.write(descriptive_stats)


# central tendency
mean_sales=sales_data['unit_sold'].mean()
median_sales=sales_data['unit_sold'].median()
mode_sales=sales_data['unit_sold'].mode()[0]

st.subheader('central tendencies')
st.write(f'Mean units sold: {mean_sales}')
st.write(f'Median units sold: {median_sales}')
st.write(f'Mode units sold: {mode_sales}')


# Group statistics by category
category_stats=sales_data.groupby('category')['unit_sold'].agg(['sum','mean','std']).reset_index()
category_stats.columns=['category','total units sold','average unit sold','std of units sold']
st.subheader('Category statestics')
st.dataframe(category_stats)


# Inferential statestics
confidence_level=0.95
degres_freedom=len(sales_data['unit_sold'])-1
sample_mean=mean_sales
sample_std_error=sales_data['unit_sold'].std()/np.sqrt(sales_data['unit_sold'].shape[0])

# t-score for confidence level 95%
confidence_level=0.95
t_score=stats.t.ppf((1+confidence_level)/2,degres_freedom)
margin_of_error=t_score*sample_std_error
confidence_interval=(sample_mean-margin_of_error,sample_mean+margin_of_error)

st.subheader('confidence interval for mean units sold')
st.write(confidence_interval)


# Hypothesis testing
t_statestics,p_value=stats.ttest_1samp(sales_data['unit_sold'],20)

st.subheader('Hypothesis Testing (t-test)')
# st.write(f'T-statestic:{t_statestics},P-value:{p_value}')

col1, col2 = st.columns(2)

with col1:
    st.metric("T-Statistic", round(t_statestics, 4))

with col2:
    st.metric("P-Value", round(p_value, 4))


# if p_value<0.05:
#     st.write('reject the null hypothesis:the mean units sold is singinficantly differnet from 20,')
# else:
#     st.write('fail to reject the null hypothesis:the mean units sold is not significantly different from 20.')
# alpha=0.05

if p_value < 0.05:
    st.success(
        "📌 **Final Conclusion:** Reject the Null Hypothesis.\n\n"
        "The mean units sold is **significantly different from 20**."
    )
else:
    st.info(
        "📌 **Final Conclusion:** Fail to Reject the Null Hypothesis.\n\n"
        "The mean units sold is **not significantly different from 20**."
    )


# visualization

# Create interactive histogram
color = st.color_picker("Pick a Histogram Color", "#636EFA")
fig = px.histogram(
    sales_data,
    x="unit_sold",
    nbins=10,
    title="Distribution of Units Sold",
    opacity=0.8,
    color_discrete_sequence=[color]
    
)

# Add vertical lines
fig.add_vline(
    x=mean_sales,
    line_dash="dash",
    line_color="red",
    annotation_text="Mean",
    annotation_position="top right"
)

fig.add_vline(
    x=median_sales,
    line_dash="dash",
    line_color="blue",
    annotation_text="Median",
    annotation_position="top right"
)

fig.add_vline(
    x=mode_sales,
    line_dash="dash",
    line_color="green",
    annotation_text="Mode",
    annotation_position="top right"
)

# Layout improvements
fig.update_layout(
    xaxis_title="Units Sold",
    yaxis_title="Frequency",
    template="plotly_white"
)

st.plotly_chart(fig, use_container_width=True)

# box plot
fig = px.box(
    sales_data,
    x="category",
    y="unit_sold",
    color="category",
    points="all",  # show individual data points
    template="plotly_white",
     color_discrete_sequence=["#636EFA", "#FA3411", "#00CC96"]
)

fig.update_traces(boxmean=True)  # show mean marker

st.plotly_chart(fig, use_container_width=True)



# bar chart

category_stats_sorted = category_stats.sort_values(
    by="total units sold",
    ascending=False
)

fig = px.bar(
    category_stats_sorted,
    x="category",
    y="total units sold",
    color="category",
    text_auto=True,
    title="Total Units Sold by Category (Sorted)"
)

st.plotly_chart(fig, use_container_width=True)