import random
import string

def generate_text(txt_len, dict):
    random_star_idx = random.randint(0, len(dict) - txt_len)
    txt = dict[random_star_idx:random_star_idx + txt_len]
    return list(txt)

def generate_label(language, min_txt_len, max_txt_len, ch_dict, en_dict):
    if language == 'en':
        txt_len = random.randint(min_txt_len, max_txt_len)
        out = generate_text(txt_len, en_dict)

        if random.random() < 0.5:
            out[0] = out[0].upper()
    elif language == 'ch':
        txt_len = random.randint(min_txt_len, max_txt_len)
        out = generate_text(txt_len, ch_dict)
    return ''.join(out)

def load_courp(p, join_c=''):
    courp = []
    with open(p, mode='r', encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip("\n").strip("\r\n")
            courp.append(line)
    courp = join_c.join(courp)
    return courp

def random_bool(length):
    return [random.choice([True, False]) for _ in range(length)]

def randomcolor():
    colorArr = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    color ="#"+''.join([random.choice(colorArr) for i in range(6)])
    return color

def randomFileName(chartType, it):
    output_file_name = "".join(random.choices(string.ascii_uppercase + string.digits, k=20))
    return "{}_{}_{}".format(chartType, it, output_file_name)

def dict_to_markdown(data):
    markdown_table = f"# {data['title']}\n\n"
    markdown_table += "| Slice | Value |\n"
    markdown_table += "| --- | --- |\n"

    for slice_name, slice_value in data['values'].items():
        markdown_table += f"| {slice_name} | {slice_value} |\n"

    return markdown_table