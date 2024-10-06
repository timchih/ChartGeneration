# ChartGeneration

Generation of Chart(pie/bar/line) image and corresponding information(int json) for (Chart QA) specific LMM training datasets using matplotlib

Allows for two different type of generation:
1. chart with random(no-meaning) words
2. chart with given(meaningful) words

|Type|Example|
|---|---|
|Random Texts|![](img/random_words.PNG)|
|Given(Meaningful) Words|![](img/meaningful_words.PNG)|

This is an example json of the information of the image
```json
{
    "image": "output/bar/bar_0_XI7XRJY2J3TAFKNP846V0.png", 
    "json": {
        "title": "Daily Production by Factory", 
        "x_title": "Factory", 
        "y_title": "Production (Units)", 
        "values": {
            "Monday": {"Factory A": 135, "Factory B": 105, "Factory C": 56}, 
            "Tuesday": {"Factory A": 124, "Factory B": 72, "Factory C": 51}, 
            "Wednesday": {"Factory A": 91, "Factory B": 60, "Factory C": 144}, 
            "Thursday": {"Factory A": 72, "Factory B": 52, "Factory C": 94}, 
            "Friday": {"Factory A": 104, "Factory B": 60, "Factory C": 118}}}, 
    "markdown": "### Daily Production by Factory\n\n\n# Monday\n| Factory | Production (Units) |\n| --- | --- |\n| Factory A | 135 |\n| Factory B | 105 |\n| Factory C | 56 |\n\n# Tuesday\n| Factory | Production (Units) |\n| --- | --- |\n| Factory A | 124 |\n| Factory B | 72 |\n| Factory C | 51 |\n\n# Wednesday\n| Factory | Production (Units) |\n| --- | --- |\n| Factory A | 91 |\n| Factory B | 60 |\n| Factory C | 144 |\n\n# Thursday\n| Factory | Production (Units) |\n| --- | --- |\n| Factory A | 72 |\n| Factory B | 52 |\n| Factory C | 94 |\n\n# Friday\n| Factory | Production (Units) |\n| --- | --- |\n| Factory A | 104 |\n| Factory B | 60 |\n| Factory C | 118 |\n", 
    "type": "bar"
}
```

## Generating Charts

### Charts with random texts
The texts are randomly generated from a dictionary. There are default dictionaries.

You will be able to replace the dictionary with your own dictionary by adding a dixtionary(.txt) to `ch_dict_path` or `en_dict_path`.
You can also indicate the language of the output image [chinese/english]
Both the image and the jsonl file will be stored in `output/chart/` by default

Run the following command to generate 2 random bar chart at output/bar/
When `ch_dict_path/en_dict_path` are not specified, the program will use the default word dictionary in the `dict/` folder
```bash
# generating 2 random bar chart
python generate_chart.py --chart_type='bar' --output_path='output/bar/' --img_count=2 --is_random
```

Random mode specific parameter settings:
```bash
--is_random    # random texts mode
--min_txt_len  # minimum length of the text
--max_txt_len  # maximum length of the text
```

General settings:
```bash
--output_path    # output file location
--ch_dict_path   # texts dictionary path (for generating random chinese texts)
--en_dict_path   # texts dictionary path (for generating random english texts)
--chart_type     # specifies the desired chart type
--img_count      # number of charts generated
--language       # specifies the language of the text
```

Pie chart specific settings:
```bash
--max_slice      # maximum number of slices of pie chart
--min_slice      # minimum number of slices of pie chart
```

Bar/Line chart specific settings:
```bash
--min_subcate    # minimum number of sub-categories
--max_subcate    # maximum number of sub-categories
--min_categories # minimum number of categories
--max_categories # maximum number of categories
--val_range      # the range of values e.g. val_range=0.5, then the value will be within the range (50%, 150%)
--center_val     # the center value of the range
```

### Charts with Given texts
Given a dictionary of texts on the chart, the program will be able to generate chart image and corresponding information with the given text

Dictionary of texts:
```json
{
    "title": "Daily Production by Factory", 
    "xlabel": "Factory", 
    "ylabel": "Production (Units)", 
    "category": ["Factory A", "Factory B", "Factory C"], 
    "subcategory": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
}
```

Run the following command to generate results from the given text dictionary
```bash
python generate_chart.py --dict_path='dict/test.jsonl' --chart_type='bar' --output_path='output/bar/'
```

Larger examples("dict/bar_words.jsonl" and "dict/pie_words.jsonl") of Dictionary of texts are included under the `dict/` folder

You can generate loads of these Dictionary of texts through call generative AIs
You can run the following prompt
```
In [Chinese/English], can you generate [10] (title, category, subcategory) for bar chart in a jsonl file? The number of subcategory can 1,2,3,4,5...
    please use utf-8 encoding
    {"title": "", "xlabel": "", "ylabel": "", "category": ["", "", ..], "subcategory": ["", "", ...]}
```

