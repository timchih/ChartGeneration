import matplotlib.pyplot as plt
import numpy as np
import random

def generate_random_data(num_categories, num_subcategories):
    data = {}
    for i in range(num_categories):
        category_name = f'Category {i+1}'
        data[category_name] = {}
        for j in range(num_subcategories):
            subcategory_name = f'Subcategory {j+1}'
            data[category_name][subcategory_name] = random.randint(1, 100)
    return data

def plot_stacked_bar_chart(data):
    categories = list(data.keys())
    subcategories = list(data[categories[0]].keys())
    
    # Initialize the bottom for each category
    bottom = np.zeros(len(categories))
    
    # Create the figure and axis
    fig, ax = plt.subplots()
    
    # Plot each subcategory
    for subcategory in subcategories:
        values = [data[category][subcategory] for category in categories]
        print(values)
        ax.bar(categories, values, label=subcategory, bottom=bottom)
        bottom += values
    
    # Add labels and title
    ax.set_xlabel('Categories')
    ax.set_ylabel('Values')
    ax.set_title('Random Stacked Bar Chart')
    ax.legend()
    
    # Show the plot
    plt.show()

# Parameters
num_categories = 5
num_subcategories = 3

# Generate random data
data = generate_random_data(num_categories, num_subcategories)

# Plot the stacked bar chart
plot_stacked_bar_chart(data)