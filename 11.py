# import packages
import pandas as pd 
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# show the title
st.title('Titanic App by Xiuqi Liang')

# read csv and show the dataframe
df = pd.read_csv('train.csv')
df
# create a figure with three subplots, size should be (15, 5)
# show the box plot for ticket price with different classes
# you need to set the x labels and y labels
# a sample diagram is shown below
df['Fare'] = pd.to_numeric(df['Fare'], errors='coerce')
df = df.dropna(subset=['Fare'])
plt.figure(figsize=(15, 5))
for i, pclass in enumerate([1, 2, 3], start=1):
    plt.subplot(1, 3, i)
    data = df[df['Pclass'] == pclass]['Fare']
    plt.boxplot(data, patch_artist=False)
    
    plt.title(f'Pclass {pclass} Ticket Prices')
    
    if pclass == 1:
        plt.ylim(-2, 520)
        plt.yticks(range(0, 501, 100))
    else:
        plt.ylim(-2, 74)
        plt.yticks(range(0, 71, 10))
    
    plt.xlabel('Pclass')
    plt.ylabel('Ticket Price ($)')

st.pyplot(plt)

