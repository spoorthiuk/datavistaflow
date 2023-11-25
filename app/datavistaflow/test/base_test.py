from datavistaflow import plot_line_animation, plot_scatter_animation

y1 = [10,20,30,25,60,70,30,12,155,245,223,123,454,22,455,2,22,31]
x1 = list(range(len(y1)))
y2 = [12,-23,31,-23,-62,72,-32]
x2 = list(range(len(y2)))
plot_line_animation(input = [(x1,y1),(x2,y2)], n_frames = len(x1), ylim=[-100,500], xlim=[0,20], xlabel = 'x axis', ylabel = 'y axis', title= 'Test', legend_label= ['y1', 'y2'], plot_style = 'ggplot', save = True, save_animation_name='line_test_animation.gif')
plot_scatter_animation(input = [(x1,y1),(x2,y2)], n_frames = len(x1), ylim=[-100,500], xlim=[0,20], xlabel = 'x axis', ylabel = 'y axis', title= 'Test', legend_label= ['y1', 'y2'], plot_style = 'ggplot', save = True, save_animation_name='scatter_test_animation.gif')