import argparse
from GenerateChart import GenerateChart

# TODO: argument parsing
        

if __name__ == '__main__':
    # args = parse_args()
    # print(args)
    chart = GenerateChart('dict/test.jsonl', 'pie', 'output/pie/', 2, is_random=True)

    chart.generate_chart()
