import matplotlib.pyplot as plt
import numpy as np
import generation_helper as gh

from pylab import mpl
# a font that includes chinese letters
mpl.rcParams["font.sans-serif"] = ["SimHei"]
class Pie:
    def __init__(self, 
                 langauge_dict,
                 num_slices,
                 language='en',
                 min_txt_len=5,
                 max_txt_len=12,
                 is_random=True,
                 ):
        self.lang_dict = langauge_dict
        self.num_slices = num_slices
        self.language = language
        self.min_txt_len = min_txt_len
        self.max_txt_len = max_txt_len
        self.is_random = is_random
        # assign random variables
        self.colors = plt.cm.viridis(np.linspace(0,1,num_slices))
        rand_bools = gh.random_bool(3)
        self.with_legend = rand_bools[0]
        self.with_rotate = rand_bools[1]
        self.is_counter = rand_bools[2]
        rand_colors = gh.randomcolors(2)
        self.pie_color = rand_colors[0]
        self.title_color = rand_colors[1]

    def createPie(self, output_file_name, is_show=False, data=None):
        # generate random data
        num_slices, sizes, labels, title = self.generateData(data)

        size_display = [f"{size*100:{2}.{1}f}%" for size in sizes]

        # draw random components pie with given data
        self.drawPie(sizes, labels, title)
        
        # show/save pie chart
        self.showOrSave(output_file_name, is_show)

        # generate result json
        result_dict = self.generateResult(title, dict(zip(labels, size_display)), output_file_name)
        return result_dict 
    
    def generateResult(self, title, values, output_file_name):
        json_dict = {'title': title, 'x_title': 'None', 'y_title': 'None', 'values': values}
        result_dict = {'image': output_file_name + '.png', 'json' : json_dict, 'markdown' : self.pieToMarkdown(json_dict), 'type': 'pie', 'source': 'Tim'}
        return result_dict

    def generateData(self, data=None):
        if self.is_random:
            labels = [gh.generate_label(self.language, self.min_txt_len, self.max_txt_len, self.lang_dict) for i in range(self.num_slices)]
            title = gh.generate_label(self.language, self.min_txt_len, self.max_txt_len, self.lang_dict)
        else:
            labels = list(data["labels"])
            title = data["title"]
            self.num_slices = len(labels)
            
        sizes = np.random.rand(self.num_slices)
        sizes = sizes / sizes.sum()


        return self.num_slices, sizes, labels, title
    
    def pieToMarkdown(self, data):
        markdown_table = f"# {data['title']}\n\n"
        markdown_table += "| Slice | Value |\n"
        markdown_table += "| --- | --- |\n"

        for slice_name, slice_value in data['values'].items():
            markdown_table += f"| {slice_name} | {slice_value} |\n"

        return markdown_table

    def showOrSave(self, output_file_name, is_show):
        if is_show:
            plt.show()
        else:
            plt.savefig(output_file_name + '.png')

        
    def drawPie(self, sizes, labels, title):
        _, ax1 = plt.subplots()
        size_display = [f"{size*100:{2}.{1}f}%" for size in sizes]

        if self.with_legend:
            # ? 1. percentage outside, label as legend
            wedges, texts = ax1.pie(sizes, labels=size_display, colors=self.colors,startangle=90, labeldistance=1.1, textprops={'fontsize': 8}, rotatelabels=self.with_rotate, counterclock=self.is_counter, wedgeprops=
       {'edgecolor':self.pie_color})
            plt.subplots_adjust(left=0.1, right=0.6)
            plt.legend(wedges, labels, loc="upper left", bbox_to_anchor=(1.0, 1.0))
        else:
            # ? 2. pencentage inside, label outside
            ax1.pie(sizes, labels=labels, autopct='%1.1f%%', colors=self.colors,startangle=90, labeldistance=1.1, textprops={'fontsize': 8}, rotatelabels=self.with_rotate, counterclock=self.is_counter, wedgeprops=
       {'edgecolor':self.pie_color})
            
        ax1.axis('equal')

        plt.title(title, fontweight='bold', color=self.title_color)
        plt.tight_layout()

if __name__ == "__main__":
    pie = Pie(language='ch')
    pie.randPie('something', True)
