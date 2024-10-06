import matplotlib.pyplot as plt
import random
import generation_helper as gh
import numpy as np
from pylab import mpl

# Set font for displaying Chinese
mpl.rcParams["font.sans-serif"] = ["SimHei"]

class Line:
    def __init__(self, 
                 lang_dict,
                 num_lines=5,
                 num_categories=3,
                 language='en',
                 min_txt_len=5,
                 max_txt_len=12,
                 val_range=0.5,
                 center_val=100,
                 is_random=True,
                 ):
        self.lang_dict = lang_dict
        self.language = language
        self.min_txt_len = min_txt_len
        self.max_txt_len = max_txt_len
        self.num_lines = num_lines
        self.num_categories = num_categories
        self.min_val = center_val * val_range
        self.max_val = center_val * (1 + val_range)
        self.is_random = is_random
        self.line_colors = gh.randomcolors(num_lines)
        rand_colors = gh.randomcolors(3)
        self.title_color = rand_colors[0]
        self.xlabel_color = rand_colors[1]
        self.ylabel_color = rand_colors[2]

    def randSimpleLine(self, output_file_name, gen_data, is_show=False):
        # Generate random data
        num_lines, _, line_labels, cate_labels, values, title, xlabel, ylabel = gen_data

        # Create the stacked line chart
        _, ax = plt.subplots()

        # Plot each subcategory
        for i, subcat in enumerate(cate_labels):
            ax.plot(line_labels, values[i], label=subcat, marker='o')

        # Display categories as legends
        ax.legend()
        # Adding title and labels
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        # Display/save the chart
        self.showOrSave(output_file_name, is_show)

        val_dict = dict()
        for i, cate in enumerate(cate_labels):
            val_dict[cate] = dict(zip(line_labels, values[i]))

        return self.generateResult(title, xlabel, ylabel, output_file_name, val_dict)

    def randLine(self, output_file_name, is_show=False):
        gen_data = self.generateData()
        return self.randSimpleLine(output_file_name, gen_data, is_show)

    def lineFromDict(self, output_file_name, data, is_show=False):
        # Get all data from dictionary
        num_categories = len(data["subcategory"])
        # Obtain data from data(dict)
        gen_data = self.generateData(data)

        return self.randSimpleLine(output_file_name, gen_data, is_show)

    def randLabelList(self, count):
        return [gh.generate_label(self.language, self.min_txt_len, self.max_txt_len, self.lang_dict) for _ in range(count)]

    def lineToMarkdown(self, data):
        # Extract data from JSON
        x_title = data['x_title']
        y_title = data['y_title']
        values = data['values']

        markdown_tables = []
        markdown_tables.append(f"### {data['title']}\n\n")

        # Iterate over each section in values
        for section_title, section_values in values.items():
            # Start constructing the Markdown table for the section
            markdown_table = f"# {section_title}\n"
            markdown_table += f"| {x_title} | {y_title} |\n"
            markdown_table += f"| --- | --- |\n"

            # Add rows to the table
            for key, value in section_values.items():
                markdown_table += f"| {key} | {value} |\n"

            markdown_tables.append(markdown_table)

        return "\n".join(markdown_tables)

    def generateResult(self, title, xlabel, ylabel, output_file_name, values):
        json_dict = {'title': title, 'x_title': xlabel, 'y_title': ylabel, 'values': values}
        result_dict = {'image': output_file_name + '.png', 'json' : json_dict, 'markdown' : self.lineToMarkdown(json_dict), 'type': 'line'}
        return result_dict

    def generateData(self, data=None):
        if not self.is_random and data is not None:
            title = data["title"]
            xlabel = data["xlabel"]
            ylabel = data["ylabel"]
            line_labels = data["category"]
            cate_labels = data["subcategory"]
            self.num_lines = len(line_labels)
            self.num_categories = len(cate_labels)
        else:
            line_labels = self.randLabelList(self.num_lines)
            cate_labels = self.randLabelList(self.num_categories)
            title, xlabel, ylabel = self.randLabelList(3)

        values = [[random.randint(self.min_val, self.max_val) for _ in range(self.num_lines)] for _ in range(self.num_categories)]
        return self.num_lines, self.num_categories, line_labels, cate_labels, values, title, xlabel, ylabel

    # Save the image or show; just for easy debugging
    def showOrSave(self, output_file_name, is_show):
        if is_show:
            plt.show()
        else:
            plt.savefig(output_file_name + '.png')