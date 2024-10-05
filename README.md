# ChartGeneration

Generation of Chart(pie/bar/line) image and corresponding information(int json) for (Chart QA) specific LMM training datasets using matplotlib

Allows for two different type of generation:
1. chart with random(no-meaning) words
2. chart with meaningful words

|Type|Example|
|---|---|
|Meaningless Words|![](img/random_words.PNG)|
|Meaningful Words|![](img/meaningful_words.PNG)|

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
    "type": "bar"}
```