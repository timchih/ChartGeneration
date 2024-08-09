import random
import string
from Pie import Pie
import os
import json
import argparse
import generation_helper as gh
    
from pylab import mpl
# a font that includes chinese letters
mpl.rcParams["font.sans-serif"] = ["SimHei"]

def generate_pie(chartType, output_path, is_random, f_gt, img_count=None, dict_path=None):
    if is_random:
        for i in range(img_count):
            output_file_name = gh.randomFileName(chartType, i)
            output_full_path = os.path.join(output_path, output_file_name)
            result_dict = pie.randPie(output_full_path)

            f_gt.write(json.dumps(result_dict, ensure_ascii=False) + '\n')

    else:
        with open(dict_path, 'r', encoding='utf-8') as file:
            for i, line in enumerate(file):
                output_file_name = gh.randomFileName(chartType, i)
                output_full_path = os.path.join(output_path, output_file_name)
                data = json.loads(line)
                # generate chart and save results
                result_dict = pie.pieFromDict(output_full_path, data)

                # write dictionary to json file
                f_gt.write(json.dumps(result_dict, ensure_ascii=False) + '\n')

def generate_chart(chartType, output_path, is_random, img_count=None, dict_path=None):
    # jsonl output file
    f_gt = open(os.path.join(output_path, "gt.jsonl"), encoding="utf-8", mode="w")

    # identify the type of chart need to be generated
    if chartType == 'pie':
        generate_pie(chartType, output_path, is_random, f_gt, img_count, dict_path)
    elif chartType == 'chart':
        pass
    elif chartType == 'line':
        pass
    elif chartType == 'mix':
        pass
    else:
        raise TypeError

    f_gt.close()

# chartType = "Pie"
# output_path = 'output/pie/'
            
# pie = Pie("dict/ch_news.txt", "dict/en_corpus.txt", 3, 8, 'output/pie/' + output_file_name)
pie = Pie(language='ch')

# generate_chart_random(4, 'pie', 'output/pie/')
generate_chart('pie', 'output/pie/', False, img_count=2, dict_path='dict/test.jsonl')