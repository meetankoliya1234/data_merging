import csv

dataset_1 = []
dataset_2 = []

with open("bright_stars.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        dataset_1.append(row)

with open("brown_dwarfs_final.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        dataset_2.append(row)
        
headers_1 = dataset_1[0]
star_data_1 = dataset_1[1:]

headers_2 = dataset_2[0]
star_data_2 = dataset_2[1:]

headers = headers_1 + headers_2
stars_data = []

for index, data_row in enumerate(star_data_1):
    stars_data.append(star_data_1[index] + star_data_2[index])
    
with open("final.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(stars_data)