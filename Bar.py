import matplotlib.pyplot as plt
import random
import generation_helper as gh
import numpy as np
# assert font for displaying chinese 
from pylab import mpl
mpl.rcParams["font.sans-serif"] = ["SimHei"]
class Bar:
    def __init__(self, 
                 ch_dict_path="dict/ch_news.txt",
                 en_dict_path="dict/en_corpus.txt",
                 language='en',
                 min_txt_len = 5,
                 max_txt_len = 12,
                 min_bars=3,
                 max_bars=10,
                 min_categories=2,
                 max_categories=4,
                 val_range=0.5,
                 center_val=100,
                 is_random=True,
                 ):
        self.ch = gh.load_courp(ch_dict_path, '')
        self.en = gh.load_courp(en_dict_path, '')
        self.language = language
        self.min_txt_len = min_txt_len
        self.max_txt_len = max_txt_len
        self.min_bars = min_bars
        self.max_bars = max_bars
        self.min_categories = min_categories
        self.max_categories = max_categories
        self.min_val = center_val * val_range
        self.max_val = center_val * (1 + val_range)
        self.is_random = is_random

    def randBar(self, output_file_name):
        # Generate random data
        _, _, bar_labels, cate_labels, values, title, xlabel, ylabel = self.generateData()
        # ! only for simple bar chart
        category = cate_labels[0]
        values = values[0]

        # Create a bar chart
        plt.figure(figsize=(10, 5))
        plt.bar(bar_labels, values, color='blue') #? color

        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        # display/save chart
        plt.show()
        # plt.savefig(output_file_name + '.png')

        # create info dict from data
        result_dict = self.generateResult(title, xlabel, ylabel, output_file_name, {category: dict(zip(bar_labels, values))}, 'simple bar')
        # print(result_dict['markdown'])
        return result_dict
        

    def randStackBar(self, output_file_name):
        # Generate random data
        num_bars, num_categories, bar_labels, cate_labels, values, title, xlabel, ylabel = self.generateData()

        # Create the stacked bar chart
        _, ax = plt.subplots()

        # Initialize the bottom position for each stack
        bottom = np.zeros(num_bars)

        # Plot each subcategory
        for i, subcat in enumerate(cate_labels):
            ax.bar(bar_labels, values[i], label=subcat, bottom=bottom)
            bottom += values[i]

        # display categories as legends
        ax.legend()
        # Adding title and labels
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        # Display/save the chart
        plt.show()
        # plt.savefig(output_file_name + '.png')

        val_dict = dict()
        for i, cate in enumerate(cate_labels):
            val_dict[cate] = dict(zip(bar_labels, values[i]))

        # print(val_dict)
        result_dict = self.generateResult(title, xlabel, ylabel, output_file_name, val_dict, 'stacked bar')
        return result_dict

    def randGroupBar(self, output_file_name):
        pass

    def randLabelList(self, count):
        return [gh.generate_label(self.language, self.min_txt_len, self.max_txt_len, self.ch, self.en) for i in range(count)]
    
    def barToMarkdown(self, data):
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

    def generateResult(self, title, xlabel, ylabel, output_file_name, values, typeBar):
        json_dict = {'title': title, 'x_title': xlabel, 'y_title': ylabel, 'values': values}
        result_dict = {'image': output_file_name + '.png', 'json' : json_dict, 'markdown' : self.barToMarkdown(json_dict), 'type': typeBar, 'source': 'Tim'}
        return result_dict
    
    def generateData(self):
        num_bars = np.random.randint(self.min_bars, self.max_bars)
        num_categories = np.random.randint(self.min_categories, self.max_categories)
        bar_labels = self.randLabelList(num_bars)
        cate_labels = self.randLabelList(num_categories)
        values = [[random.randint(self.min_val, self.max_val) for _ in range(num_bars)] for _ in range(num_categories)]
        title, xlabel, ylabel = self.randLabelList(3)
        # print(values)
        return num_bars, num_categories, bar_labels, cate_labels, values, title, xlabel, ylabel



if __name__ == "__main__":
    bar = Bar()
    # bar.randBar("something")
    bar.randStackBar('something')