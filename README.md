# Data-Visualization
The data set contains 3 classes of 50 instances each, where each class refers to a type of
iris plant. One class is linearly separable from the other 2; the latter are NOT linearly
separable from each other.

PANDAS LIBRARY
Pandas provides the read_csv() function to read data stored as a csv file into a pandas
DataFrame . pandas supports many different file formats or data sources out of the box (csv,
excel, sql, json, parquet, …), each of them with the prefix read_*.
The Iris dataset in our code is in csv format and Hence the read_csv function of pandas was
used here.

SEABORN LIBRARY
Seaborn is used for data visualization and exploratory data analysis. Seaborn works easily
with data frames and the Pandas library.
We have used seaborn so as to detect any outliers, missing values or errors in the data
frame
A scatterplot is plotted to understand the data completely. Jointplot function of seaborn
library is used so as to do the same. The x variable is ‘Sepal Width’ and y variable is ‘Sepal
Length’ .
On top and right side of the graph are the histograms of Sepal Width and Sepal Length
variables respectively whereas in the middle is the scatterplot of Sepal Width vs Sepal
Length. Hence, the outliers are clearly visible.
Now that the numerical variables and pre-processed the pre-processing of categorical
variables is done using barplots or countplots. The countplot function of seaborn library is
used.
The countplot is represented with ‘airport’ variable. Similar countplots are drawn with
variables ‘waterbody’ and ‘bus_ter’.

NUMPY LIBRARY
NumPy can be used to perform a wide variety of mathematical operations on arrays.
The percentile function of numpy library is used on the variable Sepal Width. This is done so
as to know whether the dataset has skewed values.
Once the skewed variables are known the dataset can be modified and pre-processing the
data be completed.
