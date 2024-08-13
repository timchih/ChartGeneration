import random
import generation_helper as gh

def generate_qa(result_dict):
    if result_dict["type"] == 'pie':
        result = dict()
        result["id"] = extract_substring(result_dict["image"])
        result["image"] = result_dict["image"]
        result["conversations"] = generate_qa_pie(result_dict)
        return result
    elif result_dict["type"] == 'bar':
        generate_qa_bar(result_dict)
    elif result_dict["type"] == 'line':
        pass
    elif result_dict["type"] == 'mix':
        pass
    else:
        raise TypeError

def generate_qa_pie(result_dict):
    title = result_dict["json"]["title"]
    values = result_dict["json"]["values"]

    largest_slice = max(values, key=lambda k: float(values[k].strip('%')))
    smallest_slice = min(values, key=lambda k: float(values[k].strip('%')))

    random_key = gh.random_pick(list(values.keys()))

    # Get a random percentage from the values
    random_percentage = gh.random_pick(list(values.values()))
    
    # Find the label for the random percentage
    random_label = next(key for key, value in values.items() if value == random_percentage)
    
    qa_data = [
        {"from": "human", "value": "<image>\nWhat is the title of the pie chart?"},
        {"from": "gpt", "value": title},
        {"from": "human", "value": "Which slice has the largest percentage in the pie chart?"},
        {"from": "gpt", "value": largest_slice},
        {"from": "human", "value": "Which slice has the smallest percentage in the pie chart?"},
        {"from": "gpt", "value": smallest_slice},
        {"from": "human", "value": f"What percentage does the '{random_key}' slice represent?"},
        {"from": "gpt", "value": values[random_key]},
        {"from": "human", "value": "How many slices are there in the pie chart?"},
        {"from": "gpt", "value": str(len(values))},
        {"from": "human", "value": f"What label does the '{random_percentage}' slice represent?"},
        {"from": "gpt", "value": random_label}
    ]
    
    return qa_data

def generate_qa_bar(result_dict):
    pass

def extract_substring(full_string):
    # Split the string by '/' and take the last element
    parts = full_string.split('/')
    filename = parts[-1]
    
    # Split the filename by '.' and take the first element
    name_parts = filename.split('.')
    return name_parts[0]