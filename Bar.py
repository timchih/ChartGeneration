import matplotlib.pyplot as plt
import random
import generation_helper as gh
import numpy as np
# assert font for displaying chinese 
from pylab import mpl
mpl.rcParams["font.sans-serif"] = ["SimHei"]
class Bar:
    def __init__(self, 
                 lang_dict,
                 num_bars=5,
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
        self.num_bars = num_bars
        self.num_categories = num_categories
        self.min_val = center_val * val_range
        self.max_val = center_val * (1 + val_range)
        self.is_random = is_random
        self.bar_colors = gh.randomcolors(num_bars)
        rand_colors = gh.randomcolors(3)
        self.title_color = rand_colors[0]
        self.xlabel_color = rand_colors[1]
        self.ylabel_color = rand_colors[2]

    def randSimpleBar(self, output_file_name, gen_data, index=0, is_show=False):
        # Generate random data
        _, _, bar_labels, cate_labels, values, title, xlabel, ylabel = gen_data
        # only for simple bar chart
        category = cate_labels[index]
        values = values[index]
        bar_color = self.bar_colors[index]

        # TODO: abstracted random function(e.g. color...)
        # Create a bar chart
        plt.figure(figsize=(10, 5))
        plt.bar(bar_labels, values, color=bar_color)

        plt.xlabel(xlabel, color=self.xlabel_color)
        plt.ylabel(ylabel, color=self.ylabel_color)
        plt.title(title, fontweight='bold', color=self.title_color)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        # Display/save the chart
        self.showOrSave(output_file_name, is_show)

        # create info dict from data
        result_dict = self.generateResult(title, xlabel, ylabel, output_file_name, {category: dict(zip(bar_labels, values))})
        # print(result_dict['markdown'])
        return result_dict
        

    def randStackBar(self, output_file_name, gen_data, is_show=False):
        # Generate random data
        num_bars, _, bar_labels, cate_labels, values, title, xlabel, ylabel = gen_data

        # Create the stacked bar chart
        _, ax = plt.subplots()

        # Initialize the bottom position for each stack
        bottom = np.zeros(num_bars)

        # Plot each subcategory
        for i, subcat in enumerate(cate_labels):
            ax.bar(bar_labels, values[i], label=subcat, bottom=bottom)
            bottom += values[i]

        # TODO: abstracted random function(e.g. color...)
        # display categories as legends
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
            val_dict[cate] = dict(zip(bar_labels, values[i]))

        # print(val_dict)
        result_dict = self.generateResult(title, xlabel, ylabel, output_file_name, val_dict)
        return result_dict

    def randGroupBar(self, output_file_name, gen_data, is_show=False):
        # generate random data
        num_bars, num_categories, bar_labels, cate_labels, values, title, xlabel, ylabel = gen_data

        # Set the width of the bars
        bar_width = 0.2

        # Set the positions of the x-axis ticks
        index = np.arange(num_bars)

        # Create the figure and axes
        _, ax = plt.subplots()

        # Plotting the bars
        for i in range(num_categories):
            ax.bar(index + i * bar_width, values[i], bar_width, label=cate_labels[i])

        # Adding labels and title
        ax.legend()
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        ax.set_xticks(index + bar_width / 2)
        ax.set_xticklabels(bar_labels)

        # Display/save the chart
        self.showOrSave(output_file_name, is_show)

        # generate result dictionary
        val_dict = dict()
        for i, cate in enumerate(cate_labels):
            val_dict[cate] = dict(zip(bar_labels, values[i]))

        # print(val_dict)
        result_dict = self.generateResult(title, xlabel, ylabel, output_file_name, val_dict)
        return result_dict
    
    def randBar(self, output_file_name, is_show=False):
        gen_data = self.generateData()
        if self.num_categories == 1:
            return self.randSimpleBar(output_file_name, gen_data, is_show=is_show)
        return self.randStackBar(output_file_name, gen_data, is_show) if random.randint(0, 1) == 0 else self.randGroupBar(output_file_name, gen_data, is_show)
        
    def barFromDict(self, output_file_name, data, is_show=False):
        # get all data from dictionary
        num_categories = len(data["subcategory"])
        # obtain data from data(dict)
        gen_data = self.generateData(data)
        # create list for all dicts created
        dict_list = []
        
        # assign full slice to generating bar and group chart
        dict_list.append(self.randGroupBar(output_file_name+'0', gen_data, is_show))
        dict_list.append(self.randStackBar(output_file_name+'1', gen_data, is_show))
        for i in range(num_categories):
            dict_list.append(self.randSimpleBar(output_file_name+str(i+2), gen_data, i, is_show))

        return dict_list

    def randLabelList(self, count):
        return [gh.generate_label(self.language, self.min_txt_len, self.max_txt_len, self.lang_dict) for _ in range(count)]
    
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

    def generateResult(self, title, xlabel, ylabel, output_file_name, values):
        json_dict = {'title': title, 'x_title': xlabel, 'y_title': ylabel, 'values': values}
        result_dict = {'image': output_file_name + '.png', 'json' : json_dict, 'markdown' : self.barToMarkdown(json_dict), 'type': 'bar', 'source': 'Tim'}
        return result_dict
    
    def generateData(self, data=None):
        # num_bars = np.random.randint(self.min_bars, self.max_bars)
        # num_categories = np.random.randint(self.min_categories, self.max_categories)
        if not self.is_random and data != None:
            title = data["title"]
            xlabel = data["xlabel"]
            ylabel = data["ylabel"]
            bar_labels = data["category"]
            cate_labels = data["subcategory"]
            self.num_bars = len(bar_labels)
            self.num_categories = len(cate_labels)
        else:
            bar_labels = self.randLabelList(self.num_bars)
            cate_labels = self.randLabelList(self.num_categories)
            title, xlabel, ylabel = self.randLabelList(3)

        values = [[random.randint(self.min_val, self.max_val) for _ in range(self.num_bars)] for _ in range(self.num_categories)]
        # print(values)
        return self.num_bars, self.num_categories, bar_labels, cate_labels, values, title, xlabel, ylabel

    # save the image or show; just for easy debugging
    def showOrSave(self, output_file_name, is_show):
        if is_show:
            plt.show()
        else:
            plt.savefig(output_file_name + '.png')


if __name__ == "__main__":
    bar = Bar(gh.load_courp("dict/en_corpus.txt", ''))
    bar.randSimpleBar("something", is_show=True)
    # bar.randStackBar('something')
    # bar.randGroupBar("something")