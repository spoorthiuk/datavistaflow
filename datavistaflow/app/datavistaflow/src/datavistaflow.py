import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def plot_line_animation(input, n_frames, frame_interval = 100, legend_label = [], plot_style = None, xlim = [], ylim = [], title = None, xlabel = None, ylabel = None, save = False, save_animation_name = 'animation.gif'):
    """
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
    """
    def animate(i):
        ax.cla()
        if xlim != [] :
            ax.set_xlim(xlim)
        if ylim != []:
            ax.set_ylim(ylim)
        if title != None:
            ax.set_title(title)
        if xlabel != None:
            ax.set_xlabel(xlabel)
        if ylabel != None:
            ax.set_ylabel(ylabel)
        for (x_val, y_val) in input:
            ax.plot(x_val[:i], y_val[:i])
        if legend_label != []:
            ax.legend(legend_label)
    assert all(isinstance(val, tuple) for val in input), "Invalid datatype"
    assert all(len(val) == 2 for val in input), "Invalid input, expected a tuple of length 2"
    #setting the plot style
    plot_styles = plt.style.available
    assert plot_style in plot_styles, "Invalid plot style. Choose from {}".format(plt.style.available)
    if plot_style != None:
        plt.style.use(plot_style) 
    fig, ax = plt.subplots(1,1)
    animation = FuncAnimation(fig, animate, frames = n_frames, interval =  frame_interval)
    plt.show()
    if save == True:
        animation.save(save_animation_name, writer='imagemagick', fps=30)

def plot_scatter_animation(input, n_frames, frame_interval = 100, legend_label = [], plot_style = None, xlim = [], ylim = [], title = None, xlabel = None, ylabel = None, save = False, save_animation_name = 'animation.gif'):
    """
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
    """
    def animate(i):
        ax.cla()
        if xlim != [] :
            ax.set_xlim(xlim)
        if ylim != []:
            ax.set_ylim(ylim)
        if title != None:
            ax.set_title(title)
        if xlabel != None:
            ax.set_xlabel(xlabel)
        if ylabel != None:
            ax.set_ylabel(ylabel)
        for (x_val, y_val) in input:
            ax.scatter(x_val[:i], y_val[:i])
        if legend_label != []:
            ax.legend(legend_label)
    assert all(isinstance(val, tuple) for val in input), "Invalid datatype"
    assert all(len(val) == 2 for val in input), "Invalid input, expected a tuple of length 2"
    #setting the plot style
    plot_styles = plt.style.available
    assert plot_style in plot_styles, "Invalid plot style. Choose from {}".format(plt.style.available)
    if plot_style != None:
        plt.style.use(plot_style) 
    fig, ax = plt.subplots(1,1)
    animation = FuncAnimation(fig, animate, frames = n_frames, interval =  frame_interval)
    plt.show()
    if save == True:
        animation.save(save_animation_name, writer='imagemagick', fps=30)
