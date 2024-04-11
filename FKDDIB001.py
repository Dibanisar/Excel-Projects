import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams["figure.figsize"] = [12, 16]

fig, ax = plt.subplots(nrows=4, ncols=2)  # Create 8 subplots with 4 in the first column and 4 in the second column
fig.tight_layout()  # Adjust spacing between subplots

yrs = np.arange(start=1961, stop=2020)  # Generate an array of years from 1961 to 2019
ax_flattened = ax.ravel()  # Flatten the axes array

df = pd.read_excel("Environment_Temperature_change_E_All_Data_NOFLAG.xlsx")  # Read the Excel data

areas = ["South Africa", "Namibia", "Botswana",
         "Zimbabwe", "Mozambique", "Lesotho",
         "Eswatini", "Africa"]  # List of areas to read data from

# Define parameters for filtering data
month = "Meteorological year"
element = "Temperature change"
plus_minus = "\u00b1"  # Plus minus symbol
degrees_symbol = "\u00b0"  # Degrees symbol
count = 0  # Initialize the count for areas indexes

colors = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'brown', 'gray']  # List of colors for each plot

for i, axes_block in enumerate(ax_flattened):
    area = areas[count]  # Select each country from the list of areas

    # Select row with the country/region name, meteorological year, and temperature change element
    selected_row = df.loc[(df['Area'] == area) & (df['Months'] == month) & (df['Element'] == element)]

    temp_data = selected_row.loc[:, "Y1961":]  # Extract columns from 1961 to 2019
    temp_data_squeezed = np.squeeze(temp_data)  # Reshape the data to match the shape of 'yrs' (59,)

    axes_block.plot(yrs, temp_data_squeezed,marker = '*', color=colors[count])  # Plot years against temperature change
    axes_block.set_title(area, fontsize=20)  # Set the title of the subplot as the area/country name

    mean_each_row = np.mean(temp_data_squeezed)  # Calculate the mean of each row
    sd_each_row = np.std(temp_data_squeezed)  # Calculate the standard deviation of each row

    x = 1980  # X coordinate for writing mean and standard deviation
    y = 1.25  # Y coordinate for writing mean and standard deviation
    text = f"Mean: {np.round(mean_each_row, 3)} {degrees_symbol} {plus_minus} {np.round(sd_each_row, 3)} {degrees_symbol} Celsius"
    # Construct the text to be displayed in each subplot
    axes_block.text(x, y, text, ha='center', va='center', fontsize=14)  # Add text to the subplot

    count += 1  # Increment the count for areas indexes

plt.savefig("temperature_plots.pdf")  # Save the plots to a PDF file
plt.show()  # Display the plots
