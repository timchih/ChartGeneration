import generation_helper as gh
import os
from Pie import Pie
from Bar import Bar
import json
import numpy as np

from pylab import mpl
# a font that includes chinese letters
mpl.rcParams["font.sans-serif"] = ["SimHei"]

class GenerateChart:
    def __init__(self,
                 dict_path,
                 chartType='pie',
                 output_path='output/',
                 img_count=2,
                 is_random=True,
                 min_txt_len=5,
                 max_txt_len=12,
                 ch_dict_path="dict/ch_news.txt",
                 en_dict_path="dict/en_corpus.txt",
                 language='en',
                 min_slice=3,
                 max_slice=8,
                 min_bars=3,
                 max_bars=10,
                 min_categories=1,
                 max_categories=4,
                 val_range=0.5,
                 center_val=100,
                 ) -> None:
        # general variables
        self.chartType = chartType
        self.output_path = output_path
        self.is_random = is_random
        self.img_count = img_count
        self.dict_path = dict_path
        self.ch = gh.load_courp(ch_dict_path, '')
        self.en = gh.load_courp(en_dict_path, '')
        self.language = language
        self.min_txt_len = min_txt_len
        self.max_txt_len = max_txt_len
        # Pie variables
        self.min_slice = min_slice
        self.max_slice = max_slice
        # bar variables
        self.min_bars = min_bars
        self.max_bars = max_bars
        self.min_categories = min_categories
        self.max_categories = max_categories
        self.val_range = val_range
        self.center_val = center_val

    def generate_pie(self, f_gt):
        if self.is_random:
            for i in range(self.img_count):
                output_full_path = gh.randomFileName(self.chartType, i, self.output_path)
                pie = self.assignPie()
                result_dict = pie.createPie(output_full_path)

                f_gt.write(json.dumps(result_dict, ensure_ascii=False) + '\n')

        else:
            with open(self.dict_path, 'r', encoding='utf-8') as file:
                for i, line in enumerate(file):
                    output_full_path = gh.randomFileName(self.chartType, i, self.output_path)
                    data = json.loads(line)
                    # generate chart and save results
                    pie = self.assignPie()
                    result_dict = pie.createPie(output_full_path, data=data)

                    # write dictionary to json file
                    f_gt.write(json.dumps(result_dict, ensure_ascii=False) + '\n')

    def assignPie(self):
        if self.language == 'en':
            lang_dict = self.en
        else:
            lang_dict = self.ch
        num_slices = np.random.randint(self.min_slice, self.max_slice)
        return Pie(lang_dict,
                   num_slices,
                   self.language,
                   self.min_txt_len,
                   self.max_txt_len,
                   self.is_random)

    def generate_bar(self, f_gt):
        if self.is_random:
            for i in range(self.img_count):
                output_full_path = gh.randomFileName(self.chartType, i, self.output_path)
                bar = self.assignBar()
                result_dict = bar.randBar(output_full_path)

                f_gt.write(json.dumps(result_dict, ensure_ascii=False) + '\n')
        else:
            with open(self.dict_path, 'r', encoding='utf-8') as file:
                for i, line in enumerate(file):
                    output_full_path = gh.randomFileName(self.chartType, i, self.output_path)
                    data = json.loads(line)
                    bar = self.assignBar()
                    
                    result_dict_list = bar.barFromDict(output_full_path, data=data)

                    for result_dict in result_dict_list:
                        f_gt.write(json.dumps(result_dict, ensure_ascii=False) + '\n')

    def assignBar(self):
        if self.language == 'en':
            lang_dict = self.en
        else:
            lang_dict = self.ch
        num_bars = np.random.randint(self.min_bars, self.max_bars)
        num_categories = np.random.randint(self.min_categories, self.max_categories)
        return Bar(lang_dict,
                   num_bars,
                   num_categories,
                   self.language,
                   self.min_txt_len,
                   self.max_txt_len,
                   self.val_range,
                   self.center_val,
                   self.is_random)

    def generate_chart(self):
        # jsonl output file
        f_gt = open(os.path.join(self.output_path, "gt.jsonl"), encoding="utf-8", mode="w")

        # identify the type of chart need to be generated
        if self.chartType == 'pie':
            self.generate_pie(f_gt)
        elif self.chartType == 'bar':
            self.generate_bar(f_gt)
        elif self.chartType == 'line':
            pass
        elif self.chartType == 'mix':
            pass
        else:
            raise TypeError

        f_gt.close()
