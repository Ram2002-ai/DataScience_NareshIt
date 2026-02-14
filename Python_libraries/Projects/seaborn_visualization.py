import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# set seaborn  style
sns.set_style("whitegrid")

# load the tips dataset
tips = pd.read_csv(r"C:\Users\USER\DataScience_NareshIt\Python_libraries\tips.csv")

# streamlit app
st.title("Seaborn Visualization on Tips Dataset")
st.write('This page contains variety of Seaborn Plots')

# Function to create and display a plot
def display_plot(title,plot_func):
    st.subheader(title)
    fig,ax=plt.subplots(figsize=(8,6))
    plot_func(ax)
    st.pyplot(fig)
    plt.close(fig) # close the figure to free memory

# plot definations

def scatter_plot(ax):
    sns.scatterplot(data=tips,x='total_bill',y='tip',hue='time',size='size',palette='Set1',ax=ax)
    ax.set_title('Total bill vs Tip over the time')
def line_plot(ax):
    sns.lineplot(data=tips,x='size',y='total_bill',hue='time',ci=None,marker='o',palette='Set1',ax=ax)
    ax.set_title('Total bill by family and sex')


def bar_plot(ax):
    sns.boxplot(data=tips,x='day',y='tip',hue='smoker',palette='colorblind',ax=ax)
    ax.set_title('Day wise tips comaparision b/w smoker and non-smoker')

def box_plot(ax):
    sns.boxplot(data=tips,x='day',y='tip',hue='smoker',palette='bright',ax=ax)
    ax.set_title('Box plot of tip on smoker status')

def violin_plot(ax):
    sns.violinplot(data=tips,x='day',y='total_bill',hue='time',palette='pastel',split=True,ax=ax)
    ax.set_title('Total bill by day and time')

def countplot(ax):
    sns.countplot(data=tips,x='day',hue='smoker',palette='dark',ax=ax)
    ax.set_title('Orders by day and smoker status')

def reg_plot(ax):
    sns.regplot(data=tips,x='total_bill',y='tip',scatter_kws={'s':50},line_kws={'color':'red'},ax=ax)
    ax.set_title('Total bill vs tip')

def hist_plot(ax):
    sns.histplot(data=tips,x='total_bill',kde=True,bins=20,color='blue',ax=ax)
    ax.set_title('Distribution of total bill per day')

def strip_plot(ax):
    sns.stripplot(data=tips, x="day", y="tip", hue="sex", palette="Set1", jitter=True, ax=ax)
    ax.set_title("Strip Plot: Tips by Day and Sex")

def swarm_plot(ax):
    sns.swarmplot(data=tips, x="day", y="tip", hue="smoker", palette="Set3", ax=ax)
    ax.set_title("Swarm Plot: Tips by Day and Smoker Status")

def kde_plot(ax):
    sns.kdeplot(data=tips,x='total_bill',hue='sex',fill=True,palette='tab10',ax=ax)
    ax.set_title('Total bill density by sex')



# display all standard plots
display_plot("Scatter Plot",scatter_plot)
display_plot("Line Plot",line_plot)
display_plot("Bar Plot",bar_plot)
display_plot("Violin Plot",violin_plot)
display_plot("Countplot",countplot)
display_plot("Reg Plot",reg_plot)
display_plot("Hist Plot",hist_plot)
display_plot("Strip Plot",strip_plot)
display_plot("Swarmplot Plot",swarm_plot)
display_plot("KDE Plot",kde_plot)

#  Special cases that need custom handling
st.subheader('Pair Plot: Numerical variable by Sex')
pair_fig=sns.pairplot(tips,hue='sex',vars=['total_bill','tip','size'],palette='husl')
pair_fig.fig.suptitle('Pair Plot:Numerical Variables by Sex',y=1.02)
st.pyplot(pair_fig.fig)
plt.close(pair_fig.fig)


st.subheader('Joint Plot: Total Bill vs tip by Smoker')
joint_fig=sns.jointplot(data=tips,x='total_bill',y='tip',kind='scatter',hue='smoker',palette='coolwarm')
joint_fig.fig.suptitle('Joint Plot: Total Bill vs Tip by Smoker',y=1.02)
st.pyplot(joint_fig.fig)
plt.close(joint_fig.fig)


st.subheader('FacetGrid:Total Bill by Time and Smoker')
g=sns.FacetGrid(tips,col='time',row='smoker',margin_titles=True)
g.map(sns.histplot,'total_bill',bins=20)
g.fig.suptitle('FacetGrid:Total Bill by Time and Smoker',y=1.02)
st.pyplot(g.fig)
plt.close(g.fig)


st.subheader('Catplot (Point): Tips by day and sex')
cat_fig=sns.catplot(data=tips,x='day',y='tip',hue='sex',kind='point',palette='Set1',ax=g.axes[1])
cat_fig.fig.suptitle('Catplot (Point): Tips by day and Smoker',y=1.02)
st.pyplot(cat_fig.fig)
plt.close(cat_fig.fig)

