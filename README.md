# Datavistaflow
[This python package is under development]
## Installation
Install by typing the following command in the terminal
```python
pip install datavistaflow
```
## Usage
1) Line plot animation

A line graph plotter to create animated graphical visuals.
Parameters:
input : list of tuples containing data to be plotted as a line graph. Each tuple represents a line graph. ex: [(x1_data, y1_data), (x1_data, y1_data)]
plot_style (optional): defines the plot's style. 
xlim (optional): defines the x axis limit
ylim (optional): defines the y axis limit
title (optional): Title of the plot
xlabel (optional): defines the x axis label
ylabel (optional): defines the y axis label
n_frames (optional): total number of frames in the animation
frame_interval (optional): time interval between two consecutive frames in milli seconds. Default: 100ms
save (optional): save animation as a GIF

```python
from datavistaflow import plot_line_animation

y1 = [10,20,30,25,60,70,30]
x1 = list(range(len(y1)))
y2 = [12,23,31,23,62,72,32]
x2 = list(range(len(y2)))
plot_line_animation(input = [(x1,y1),(x2,y2)], n_frame = len(x2), plot_style = 'ggplot', save = True)
```
2) Scatter plot animation

A scatter graph plotter to create animated graphical visuals.
Parameters:
input : list of tuples containing data to be plotted as a line graph. Each tuple represents a line graph. ex: [(x1_data, y1_data), (x1_data, y1_data)]
plot_style (optional): defines the plot's style. 
xlim (optional): defines the x axis limit
ylim (optional): defines the y axis limit
title (optional): Title of the plot
xlabel (optional): defines the x axis label
ylabel (optional): defines the y axis label
n_frames (optional): total number of frames in the animation
frame_interval (optional): time interval between two consecutive frames in milli seconds. Default: 100ms
save (optional): save animation as a GIF

```python
from datavistaflow import plot_scatter_animation

y1 = [10,20,30,25,60,70,30]
x1 = list(range(len(y1)))
y2 = [12,23,31,23,62,72,32]
x2 = list(range(len(y2)))
plot_scatter_animation(input = [(x1,y1),(x2,y2)], n_frame = len(x2), plot_style = 'ggplot', save = True)
```
