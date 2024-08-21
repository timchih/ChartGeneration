import argparse
from GenerateChart import GenerateChart

# TODO: argument parsing
        

if __name__ == '__main__':
    # args = parse_args()
    # print(args)
    # chart = GenerateChart(dict_path='dict/test.jsonl', generate_qa=True, chartType='bar', output_path='output/pie/', img_count=2, is_random=True)
    chart = GenerateChart(dict_path='dict/test.jsonl', generate_qa=True, chartType='bar', output_path='output/bar/', img_count=2, is_random=False)

    chart.generate_chart()
