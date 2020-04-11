# Distribution Plots :

"""
1. Distribution plots ,or Distplots ,typically layer three plots
   on top of one another.

2. The first is a histogram , where each data points is placed
   inside a bin of similar values.

3. The second is a rug plot-marks are placed along the x-axis for
   every data point, which lets you see the distribution of
   values inside each bin.

4. Lastly , Distribution plots often include a "Kernel density
   estimation",or KDE line that tries to describes the shape
   of the distribution

"""
# Importing the librries

import numpy as np
import plotly.offline as pyo
import plotly.figure_factory as ff

#x = np.random.randn(1000)
x1 = np.random.randn(200)-2
x2 = np.random.randn(200)
x3 = np.random.randn(200)+2
x4 = np.random.randn(200)+4


hist_data = [x1,x2,x3,x4]
group_labels = ['X1','X2','X3',"X4"]

fig = ff.create_distplot(hist_data,group_labels,bin_size=[0.2,0.1,0.3,0.4])
pyo.plot(fig,filename="advance_distplot.html")
