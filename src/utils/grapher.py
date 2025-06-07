import matplotlib.pyplot as plt


def continuous_plotter(
        ind_var, dep_var,
        title: str = "", graph_label: str = "",
        x_label: str = "", y_label: str = ""):
    plt.plot(ind_var, dep_var, label=graph_label)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.show()


def discrete_plotter(
        ind_var, dep_var,
        title: str = "", graph_label: str = "",
        x_label: str = "", y_label: str = ""):
    plt.stem(ind_var, dep_var, label=graph_label)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.show()
    
import matplotlib.pyplot as plt

def combined_plotter(
        ind_var_cont, dep_var_cont,
        ind_var_disc, dep_var_disc,
        title: str = "", graph_label_cont: str = "", graph_label_disc: str = "",
        x_label: str = "", y_label: str = ""):
    
    plt.figure(figsize=(10, 4))
    
    plt.plot(ind_var_cont, dep_var_cont, label=graph_label_cont, color='blue')
    plt.stem(ind_var_disc, dep_var_disc, linefmt='r-', markerfmt='ro', basefmt='k-', 
             label=graph_label_disc)  

    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    
def more_continous_signal(
        time,
        signal_1, signal_2,
        label_1: str = "", label_2: str = "",
        title: str = "",
        x_label: str = "", y_label: str = ""):

    plt.plot(time, signal_1, label=label_1)
    plt.plot(time, signal_2, label=label_2, linestyle='--')  # Estilo punteado para diferenciar
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.show()

    
