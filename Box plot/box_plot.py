# Box Plot

"""

1. Box plot visualize the variation of feature by
   depicting the continous numerical data through
   quartiles.

2. We can then separate the data based on a categorical
   feature to compare the continous feature based on
   category.

3. The Box plot is a way of visually displaying the data
   distribution through their quartiles

4. Quartiles separate the data into four equal parts.

5. In Box plot middle line represent the median .

6. In Box plot the range between Q3 to Q1 is known as
   IQR interquartile range.

7. Min and Max values are shown with "whiskers".

8. The main use of box plot is to perform a real analysis

"""

# Importing the libraries

import plotly.offline as pyo
import plotly.graph_objs as go

# set up an array of 20 data points, with 20 as the median value
y = [1,14,14,15,16,18,18,19,19,20,20,23,24,26,27,27,28,29,33,54]

# BAsic box plot
data = [go.Box(y=y)]
pyo.plot(data,filename="basic_box_plot.html")

# Changes applied


"""
In this exammple a additional parameter is 'boxpoints' which is use
to show all points
"""
data_1 = [go.Box(y=y,boxpoints='all')]
pyo.plot(data_1,filename="box_plot_1.html")



"""
In this example a additional parameter "jitter" is use to add some 
noise to increase distance between the points.
And "pointpos" is use to place the points on different possition

"""
data_2 = [go.Box(y=y,boxpoints='all',jitter=0.3,pointpos=0)]
pyo.plot(data_2,filename="box_plot_2.html")


"""
In this example "boxpoints = outliers" , it means in this graph 
only outliers will be present only
"""

data_3 = [go.Box(y=y,boxpoints='outliers')]
pyo.plot(data_3,filename="box_plot_3.html")


# New Data

snodgrass = [.209,.205,.196,.210,.202,.207,.224,.223,.220,.201]
twain = [.225,.262,.217,.240,.230,.229,.235,.217]

data_4 = [go.Box(y=snodgrass,name="Snodgrass"),
           go.Box(y=twain,name="Twain")]


pyo.plot(data_4,filename="box_plot.html")