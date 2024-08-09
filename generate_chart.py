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

def generate_chart_random(img_count, chartType, output_path):
    f_gt = open(os.path.join(output_path, "gt.jsonl"), encoding="utf-8", mode="w")

    for i in range(img_count):
        output_file_name = gh.randomFileName(chartType, i)
        output_full_path = os.path.join(output_path, output_file_name)
        result_dict = pie.randPie(output_full_path)

        f_gt.write(json.dumps(result_dict, ensure_ascii=False) + '\n')

    f_gt.close()

def generate_chart_from_dict(dict_path, chartType, output_path):
    # jsonl output file
    f_gt = open(os.path.join(output_path, "gt.jsonl"), encoding="utf-8", mode="w")
    # read from generated dictionary of title and labels
    with open(dict_path, 'r', encoding='utf-8') as file:
        for i, line in enumerate(file):
            output_file_name = gh.randomFileName(chartType, i)
            output_full_path = os.path.join(output_path, output_file_name)
            data = json.loads(line)
            # generate chart and save results
            result_dict = pie.pieFromDict(output_full_path, data)

            # write dictionary to json file
            f_gt.write(json.dumps(result_dict, ensure_ascii=False) + '\n')

    f_gt.close()

# chartType = "Pie"
# output_path = 'output/pie/'
            
# pie = Pie("dict/ch_news.txt", "dict/en_corpus.txt", 3, 8, 'output/pie/' + output_file_name)
pie = Pie(language='ch')

# generate_chart_random(4, 'pie', 'output/pie/')
generate_chart_from_dict('dict/test.jsonl', 'pie', 'output/pie/')