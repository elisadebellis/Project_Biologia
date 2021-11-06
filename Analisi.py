import os
import csv
def analisi_dati(dir):
    dict = {}
    for i in os.listdir(dir):
        file = open(dir + "/" + i)
        csvreader = csv.reader(file, delimiter = ";")
        header = next(csvreader)
        rows = []
        for row in csvreader:
            rows.append(row)
        for j in rows:
            slice_counting = 0
            region_area, object_count, object_area = float(j[3]), float(j[5]), float(j[7])
            if region_area + object_count + object_area > 0:
                slice_counting = 1
            if dict.__contains__(j[1]):
                dict[j[1]][1] += region_area
                dict[j[1]][3] += object_count
                dict[j[1]][4] += object_area
                dict[j[1]][5] += slice_counting
            else:
                dict[j[1]] = [j[0], region_area, j[4], object_count, object_area, slice_counting]
            
            if slice_counting == 1:
                    dict[j[1]].append(file.name)
    print(dict)
analisi_dati("F67")
