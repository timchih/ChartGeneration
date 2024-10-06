import argparse
from GenerateChart import GenerateChart

def parse_args():
    parser = argparse.ArgumentParser()
    # input path
    parser.add_argument('--dict_path', type=str, default='dict/test.jsonl')
    # output path
    parser.add_argument('--output_path', type=str, default='output/chart/')
    # courp path
    parser.add_argument('--ch_dict_path', type=str, default='dict/ch_news.txt')
    parser.add_argument('--en_dict_path', type=str, default='dict/en_corpus.txt')
    # chart type
    parser.add_argument('--chart_type', type=str, default='pie')
    # generate chart with random words or not
    parser.add_argument('--is_random', action='store_true', help='The words will be randomly generated')
    # number of images generated
    parser.add_argument('--img_count', type=int, default=2)
    # language of the words in chart
    parser.add_argument('--language', type=str, default='en')
    # max/min text length (only for random text generation)
    parser.add_argument('--min_txt_len', type=int, default=5)
    parser.add_argument('--max_txt_len', type=int, default=12)

    # ! pie chart setting
    # max/min number of slices
    parser.add_argument('--max_slice', type=int, default=8)
    parser.add_argument('--min_slice', type=int, default=3)
    
    # ! bar chart setting
    # max/min number of bars
    parser.add_argument('--min_subcate', type=int, default=3)
    parser.add_argument('--max_subcate', type=int, default=10)
    # max/min number of categories
    parser.add_argument('--min_categories', type=int, default=1)
    parser.add_argument('--max_categories', type=int, default=4)
    # range of the values of data
    parser.add_argument('--val_range', type=int, default=0.5)
    parser.add_argument('--center_val', type=int, default=100)

    args = parser.parse_args()

    return args
    

if __name__ == '__main__':
    args = parse_args()
    # print(args)
    # chart = GenerateChart(dict_path='dict/test.jsonl', generate_qa=True, chartType='bar', output_path='output/pie/', img_count=2, is_random=True)
    # chart = GenerateChart(dict_path='dict/test.jsonl', generate_qa=False, chartType='bar', output_path='output/bar/', img_count=2, is_random=False)
    chart = GenerateChart(dict_path=args.dict_path, generate_qa=False, chartType=args.chart_type, output_path=args.output_path, img_count=args.img_count, is_random=args.is_random)

    chart.generate_chart()
