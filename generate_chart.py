import argparse
from GenerateChart import GenerateChart

# TODO: argument parsing
        

if __name__ == '__main__':
    # args = parse_args()
    # print(args)
    chart = GenerateChart(dict_path='dict/test.jsonl', generate_qa=True, chartType='pie', output_path='output/pie/', img_count=2, is_random=True)
    # chart = GenerateChart('dict/test.jsonl', 'bar', 'output/bar/', 2, is_random=False)
    chart.generate_chart()
