import csv
import os
import re
import argparse

parser=argparse.ArgumentParser()

parser.add_argument('--root', '-r', type=str, default=os.getcwd(), help='root directory')
parser.add_argument('--depth', '-d', type=int, default=0, help='depth of "director" directories relative to root')
parser.add_argument('--output', '-o', type=str, default='output.csv', help='output file')

args=parser.parse_args()

def path2array(path):
    return os.path.normpath(path).split(os.path.sep)

root_path = args.root
top = args.depth
path_csv = args.output

res = []
print("Scanning '{}' ...".format(root_path))
for root, dirs, files in os.walk(root_path):
    rel = os.path.relpath(root, root_path)
    rel_dirs = path2array(rel)

    if (len(rel_dirs) == 2 + top):
        director = rel_dirs[-2]
        match = re.search("^(\d{4})\s*[\u2013\u2015_-]\s*(.*)$", rel_dirs[-1])

        if not match:
            continue
        year, title = match.groups()

        res.append([director, year, title])

# print("found {} items".format(len(res)))

with open(path_csv, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Director', 'Year', 'Title'])

    for item in res:
        writer.writerow(item)

print("wrote '{file}' with {num_items} items".format(file=path_csv, num_items=len(res)))