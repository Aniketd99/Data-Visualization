# -*- coding: utf-8 -*-
"""Data Visualization.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DZa-fSD-naeheKLQrP5ahVe3-VKDaMTS

DATA VISUALIZATION
"""

!pip install RadViz-Plotly

import pandas as pd
import warnings
warnings.filterwarnings("ignore")
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="white", color_codes=True)
iris = pd.read_csv("/content/Iris.csv")
#To view Iris data below:
iris.head()

import pandas as pd
import warnings
warnings.filterwarnings("ignore")
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="white", color_codes=True)
#To import the Iris dataset:
iris = pd.read_csv("/content/Iris.csv") # the iris dataset is now a Pandas DataFrame

#To view Iris data below:
iris.head()

# Samples from each species
iris["Species"].value_counts()

# The pandas plot extenstion can be used to make a scatterplot
# Display your plot with plt.show

iris.plot(kind="scatter", x="SepalLengthCm", y="SepalWidthCm")
plt.show()

#To change color and size, add the following:
iris.plot(kind="scatter", x="SepalLengthCm", y="SepalWidthCm",color="green",s=70 )
plt.show()

# Use seaborn jointplot, to make bivariate scatterplots and univariate histograms in one graph
sns.jointplot(x="SepalLengthCm", y="SepalWidthCm", data=iris, size=5)
plt.show()

# Modify the graph above by assigning each species an individual color.
sns.FacetGrid(iris, hue="Species", size=5) \
   .map(plt.scatter, "SepalLengthCm", "SepalWidthCm") \
   .add_legend()
plt.show()

# Change the colors of the data points in the graph above
# Assign the colors a variable name, and insert hue_kws="variable name" as shown.
KS = {'color': ['blue', 'red', 'yellow']}
sns.FacetGrid(iris, hue_kws=KS, hue="Species", size=5) \
   .map(plt.scatter, "SepalLengthCm", "SepalWidthCm") \
   .add_legend()
plt.show()

# To plot the species data using a box plot:

sns.boxplot(x="Species", y="PetalLengthCm", data=iris )
plt.show()

# Use Seaborn's striplot to add data points on top of the box plot 
# Insert jitter=True so that the data points remain scattered and not piled into a verticle line.
# Assign ax to each axis, so that each plot is ontop of the previous axis. 

ax= sns.boxplot(x="Species", y="PetalLengthCm", data=iris)
ax= sns.stripplot(x="Species", y="PetalLengthCm", data=iris, jitter=True, edgecolor="gray")
plt.show()

# Tweek the plot above to change fill and border color color using ax.artists.
# Assing ax.artists a variable name, and insert the box number into the corresponding brackets

ax= sns.boxplot(x="Species", y="PetalLengthCm", data=iris)
ax= sns.stripplot(x="Species", y="PetalLengthCm", data=iris, jitter=True, edgecolor="gray")

boxtwo = ax.artists[2]
boxtwo.set_facecolor('red')
boxtwo.set_edgecolor('black')
boxthree=ax.artists[1]
boxthree.set_facecolor('yellow')
boxthree.set_edgecolor('black')

plt.show()

# A violin plot shows the density of the data, simularly to a scatter plot,
#and presents catagorical data like a box plot.
# Denser regions of the data are fatter.
sns.violinplot(x="Species", y="PetalLengthCm", data=iris, size=6)
plt.show()

#To change the fill color of the violin, choose desired colors and set equal to pallete

sns.violinplot(x="Species", y="PetalLengthCm",  palette={"blue","red","yellow"}, data=iris, size=6)
plt.show()

# seaborn's kdeplot, plots univariate or bivariate density estimates.
#Size can be changed by tweeking the value used
sns.FacetGrid(iris, hue="Species", size=5) \
   .map(sns.kdeplot, "PetalLengthCm") \
   .add_legend()
plt.show()

#Use pairplot to analyze the relationship between species for all characteristic combinations. 
# An observable trend shows a close relationship between two of the species

sns.pairplot(iris.drop("Id", axis=1), hue="Species", size=3)
plt.show()

# Set diag_kind equal to kde to modify diagnal elements into showing kernal density estimation.

sns.pairplot(iris.drop("Id", axis=1), hue="Species", size=3, diag_kind="kde")
plt.show()

# Use seaborn's jointplot to make a hexagonal bin plot
#Set desired size and ratio and choose a color.
sns.jointplot(x="SepalLengthCm", y="SepalWidthCm", data=iris, size=10,ratio=10, kind='hex',color='green')
plt.show()

# To make a Pandas boxplot grouped by species, use .boxplot
#Modify the figsize, by placing a value in the X and Y cordinates
iris.drop("Id", axis=1).boxplot(by="Species", figsize=(10, 10))
plt.show()