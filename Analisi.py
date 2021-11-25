import os
import csv
import xlsxwriter
import sys


# Function that checks if a file/directory is the one that we want to analyze
def check(dir):

    if not os.path.isdir(dir) or dir[0] == ".":
        return False
    return True

# Function that explores the first layer of the Directories, where there are all the Directories of experiments
def explore_dir(dir, dir_o):
    # Checks if exists a directory called "Results" in which we put the Files of results. If this directory
    # does not exists, then create it
    if not os.path.exists(dir_o + "Results"):
        os.mkdir(dir_o + "Results")
    else:
        x = input("La cartella esiste gia', vuoi sovrascriverla? \n [Y/N?] ")
        if (x == "N" or x == "n"):
            y = input ("Dove vuoi salvarla? (specificare il path della cartella dove si vuole salvarlo)\n")
            if not os.path.exists(y + "/" + "Results"):
                os.mkdir(y + "/" + "Results")
            dir_o = y +"/"
        
    # Explores the directories
    for i in os.listdir(dir):
        # Checks if the directory is legit
        if not check(dir + "/" + i):
            continue
        # Checks for a space in the path (Windows does not like that :D)
        file_xlsx = i.replace(" ", "_")
        # Creates the file in which we put the results
        workbook = xlsxwriter.Workbook(dir_o + "Results" + "/" + file_xlsx + '.xlsx')
        # Calling the function
        analisi_dati(dir + "/" + i, workbook)
        workbook.close()

# Function that is use to write on file created in function "explore_dir()"
def write_on_file(dict, dir, workbook):
    # Creates the sheet in which we put the results
    worksheet = workbook.add_worksheet(dir)
    # Starting writing the file, taking the datas from the dictonary created in the function "analisi_dati()"
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
        row += 1
        column = 0 

# Function that creates a dictonary that is useful for the organization of the datas
def analisi_dati(dir, workbook):
    
    dict = {}
    # Beginning exploration
    for x in os.listdir(dir):
        if not check(dir + "/" + x):
            continue
        for y in os.listdir(dir + "/" + x):            
            # Checking for skipping the file that we does not want to analyze
            if y[0] == "." or not y[-5].isdigit():
                continue                
            try:
                # Opens the file, reads it and organizes all the datas in dict
                file = open(dir + "/" + x + "/" + y)
                csvreader = csv.reader(file, delimiter = ";")
                # Taking the first line of file (the heading of the columns)
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
                            dict[id].append(y)
            except Exception as e : print("Error while opening" + " " + y)
        write_on_file(dict, x, workbook)
  
if __name__ == "__main__":
    try:
        # Taking in input the directory, in this case the one that has the experiments
        path_i = sys.argv[1]
        print(path_i)

        try:
            path_o = sys.argv[2]
            path_o = path_o + "/"
        

        except Exception as e : path_o = ""
        
        # Checking if the directory exists, if this is true, then explore the directory
        if os.path.exists(path_i) and os.path.isdir(path_i):
            explore_dir(path_i,path_o)
        # Else print an Error message end exit
        else:
            print("The directory doesn't exixst!") 
            exit(1)   
    except Exception as e : print(e)