import json
import os


data_dict = {"abs": "rrr"}
with open('dictionary.txt', 'a') as f:
    json.dump(data_dict, f)
    f.write(os.linesep)

with open('dictionary.txt') as f:
    my_list = []
    for line in f:
        js = json.loads(line)
        print()
        # my_list.append(json.loads(line))
    # my_list = [json.loads(line) for line in f]

# print(my_list)
