import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    slope, intercept, r, p, se = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    var_x = pd.Series(range(df.Year.min(), 2051))
    var_y = slope * var_x + intercept # y = m.x + b
    # Creamos la linea con los valores obtenidos
    ax.plot(var_x, var_y, color='red', label= "Todos los años")

    # Create second line of best fit
    df_dos = df[df.Year >= 2000]
    slope, intercept, r, p, se = linregress(df_dos['Year'], df_dos['CSIRO Adjusted Sea Level'])
    var_x_dos = pd.Series(range(df_dos.Year.min(), 2051))
    var_y_dos = slope * var_x_dos + intercept # y = m.x + b
    # Creamos la linea con los valores obtenidos
    ax.plot(var_x_dos, var_y_dos, color='blue', label= "2000 a 2050")

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()