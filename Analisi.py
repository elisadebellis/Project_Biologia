import os
import csv
import pandas as pd
import xlsxwriter
import sys



def write_on_file(dict, dir, workbook):
    
    
    worksheet = workbook.add_worksheet(dir)

    row = 0
    column = 0

    content = ["Region ID", "Region Name", "Region Area", "Area Unit", "Object Count", "Object Area", "Slice counting"]
    
    
    for item in content:

        worksheet.write(row, column, item)
        column += 1
        
        
        
    column = 0
    row = 1
    for i in sorted(dict.keys()):
        worksheet.write(row, column, i)
        column += 1
        for j in dict[i]:
            worksheet.write(row, column, j)
            column += 1
        
        row+=1
        column = 0  
        
    


def analisi_dati(dir):
    workbook = xlsxwriter.Workbook(dir + '.xlsx')
    dict = {}
    for x in os.listdir(dir):
        for y in os.listdir(dir + "/" + x):
            file = open(dir + "/" + x + "/" + y)
            csvreader = csv.reader(file, delimiter = ";")
            header = next(csvreader)
            rows = []
            for row in csvreader:
                rows.append(row)
            for j in rows:
                id = int(j[0])
                slice_counting = 0
                region_area, object_count, object_area = float(j[3]), float(j[5]), float(j[7])
                if region_area + object_count + object_area > 0:
                    slice_counting = 1
                if dict.__contains__(id):
                    dict[id][1] += region_area
                    dict[id][3] += object_count
                    dict[id][4] += object_area
                    dict[id][5] += slice_counting
                else:
                    dict[id] = [j[1], region_area, j[4], object_count, object_area, slice_counting]
                
                if slice_counting == 1:
                        dict[id].append(file.name)
        write_on_file(dict, x, workbook)
    workbook.close()
    


if __name__ == "__main__":
    dir = sys.argv[1]
    analisi_dati(dir)







    
