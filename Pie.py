import matplotlib.pyplot as plt
import numpy as np
import generation_helper as gh

class Pie:
    def __init__(self, 
                 ch_dict_path="dict/ch_news.txt",
                 en_dict_path="dict/en_corpus.txt",
                 minSlice=3,
                 maxSlice=8,
                 language = 'en',
                 min_txt_len = 5,
                 max_txt_len = 12
                 ):
        self.ch = gh.load_courp(ch_dict_path, '')
        self.en = gh.load_courp(en_dict_path, '')
        self.minSlice = minSlice
        self.maxSlice = maxSlice
        self.language = language
        self.min_txt_len = min_txt_len
        self.max_txt_len = max_txt_len


    def randPie(self, output_file_name):
        # ? create random variables
        num_slices = np.random.randint(self.minSlice, self.maxSlice)
        sizes = np.random.rand(num_slices)
        sizes = sizes / sizes.sum()

        rand_bools = gh.random_bool(4)
        colors = plt.cm.viridis(np.linspace(0,1,num_slices))
        rand_colors = [gh.randomcolor() for i in range(2)]
        
        if rand_bools[0]:
            # ? 1. random word label
            labels = [gh.generate_label(self.language, self.min_txt_len, self.max_txt_len, self.ch, self.en) for i in range(num_slices)]
        else:
            # ? 2. simple label Slice<number>
            labels = [f'Slice {i+1}' for i in range(num_slices)]
        
        fig1, ax1 = plt.subplots()
        size_display = [f"{size*100:{2}.{1}f}%" for size in sizes]

        # ? randomly generate pie chart
        if rand_bools[1]:
            # ? 1. percentage outside, label as legend
            wedges, texts = ax1.pie(sizes, labels=size_display, colors=colors,startangle=90, labeldistance=1.1, textprops={'fontsize': 8}, rotatelabels=rand_bools[2], counterclock=rand_bools[3], wedgeprops=
       {'edgecolor':rand_colors[0]})
            plt.subplots_adjust(left=0.1, right=0.6)
            plt.legend(wedges, labels, loc="upper left", bbox_to_anchor=(1.0, 1.0))
        else:
            # ? 2. pencentage inside, label outside
            ax1.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors,startangle=90, labeldistance=1.1, textprops={'fontsize': 8}, rotatelabels=rand_bools[2], counterclock=rand_bools[3], wedgeprops=
       {'edgecolor':rand_colors[0]})
        

        
        ax1.axis('equal')

        # ? generate title
        title = gh.generate_label(self.language, self.min_txt_len, self.max_txt_len, self.ch, self.en)
        plt.title(title, fontweight='bold', color=rand_colors[1])
        
        plt.savefig(output_file_name + '.png')

        json_dict = {'title': title, 'x_title': 'None', 'y_title': 'None', 'values': dict(zip(labels, size_display))}
        result_dict = {'image': output_file_name + '.png', 'json' : json_dict, 'markdown' : gh.dict_to_markdown(json_dict)}
        return result_dict
    
    def pieFromDict(self, output_file_name, data):
        title = data["title"]
        labels = list(data["labels"])
        num_slices = len(labels)

        sizes = np.random.rand(num_slices)
        sizes = sizes / sizes.sum()

        rand_bools = gh.random_bool(4)
        colors = plt.cm.viridis(np.linspace(0,1,num_slices))
        rand_colors = [gh.randomcolor() for i in range(2)]
        
        fig1, ax1 = plt.subplots()
        size_display = [f"{size*100:{2}.{1}f}%" for size in sizes]

        # ? randomly generate pie chart
        if rand_bools[0]:
            # ? 1. percentage outside, label as legend
            wedges, texts = ax1.pie(sizes, labels=size_display, colors=colors,startangle=90, labeldistance=1.1, textprops={'fontsize': 8}, rotatelabels=rand_bools[1], counterclock=rand_bools[2], wedgeprops=
       {'edgecolor':rand_colors[0]})
            plt.subplots_adjust(left=0.1, right=0.6)
            plt.legend(wedges, labels, loc="upper left", bbox_to_anchor=(1.0, 1.0))
        else:
            # ? 2. pencentage inside, label outside
            ax1.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors,startangle=90, labeldistance=1.1, textprops={'fontsize': 8}, rotatelabels=rand_bools[1], counterclock=rand_bools[2], wedgeprops=
       {'edgecolor':rand_colors[0]})
        

        
        ax1.axis('equal')

        # ? generate title
        plt.title(title, fontweight='bold', color=rand_colors[1])
        
        plt.savefig(output_file_name + '.png')

        json_dict = {'title': title, 'x_title': 'None', 'y_title': 'None', 'values': dict(zip(labels, size_display))}
        result_dict = {'image': output_file_name + '.png', 'json' : json_dict, 'markdown' : gh.dict_to_markdown(json_dict), 'source': 'Tim'}
        return result_dict
