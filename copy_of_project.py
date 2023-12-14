# -*- coding: utf-8 -*-
"""Copy of Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1n9pZEC-g1e-RCMNpWVsMtGGbuxJbBJwv
"""

!pip install --upgrade seaborn
!pip install --upgrade matplotlib

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from seaborn import catplot as cat

#Import data
from google.colab import drive
drive.mount('/content/drive')
file_path = '/content/drive/MyDrive/Project/medical_examination.csv'

df = pd.read_csv(file_path)

df.head()

# Add 'overweight' column
df['overweight'] = (df["weight"] / ((df["height"] / 100 ) ** 2 )).apply(lambda x : 1 if x > 25 else 0)

df.head()

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df["cholesterol"] = df ["cholesterol"].apply(lambda x : 0 if x == 1 else 1)
df["gluc"] = df ["gluc"].apply(lambda x : 0 if x == 1 else 1)

df.head()

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars = ['cardio'], value_vars = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    return df_cat

df_cat = draw_cat_plot()

df_cat.head()

draw_cat_plot()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature.
    df_cat["total"] = 1
    df_cat = df_cat.groupby(["cardio", "variable", "value"], as_index=False).count()

    # Draw the catplot with 'sns.catplot()'
    g = sns.catplot(x="variable", y="total", data=df_cat, hue="value", kind="bar", col="cardio")

    # Set plot labels and titles
    g.set_axis_labels("Variables", "Total")
    g.set_titles("Cardio: {col_name}")

    # Save the plot as an image
    plt.savefig('catplot.png')

    # Show the plot in Colab
    plt.show()

# Call the function to generate and display the plot
draw_cat_plot()

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars = ['cardio'], value_vars = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat["total"] = 1
    df_cat = df.cat.groupby(["cardio", "variable", "value"], as_index = False).count()

    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(x = "variable", y = "total", data = df_cat, hue = "value", kind = "bar", col = "cardio").fig

    # Do not modify the next two lines
    plt.savefig('catplot.png')
    return fig
    plt.show()
    draw_cat_plot()

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Assuming you have already loaded your dataset into a DataFrame called 'df'

# Draw Heat Map
def draw_heat_map(df):
    # Clean the data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr(method="pearson")

    # Generate a mask for the upper triangle
    mask = np.triu(corr)

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 12))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, linewidths=1, annot=True, square=True, mask=mask, fmt=".1f", center=0, cbar_kws={"shrink": 0.5})

    # Set the title for the plot
    plt.title('Correlation Heatmap')

    # Display the plot in Colab
    plt.show()

# Call the function to generate and display the heatmap
draw_heat_map(df)

# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[
       (df['ap_lo'] <= df['ap_hi']) &
       (df['height'] >= df['height'].quantile(0.025)) &
       (df['height'] <= df['height'].quantile(0.975)) &
       (df['weight'] >= df['weight'].quantile(0.025)) &
       (df['weight'] <= df['weight'].quantile(0.975))]


    # Calculate the correlation matrix
    corr = df_heat.corr(method = "pearson")

    # Generate a mask for the upper triangle
    mask = np.triu(corr)



    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12,12))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, linewidths=1, annot = True, square = True, mask = mask, fmt = ".1f", center=0.08, cbar_kws = {"shrink":0.5})


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig