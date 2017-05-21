import os, csv

csv_file_dir = "removeCsvHeader"
csv_file_new_dir = "HeaderRemoved"
csv_file_suffix = ".csv"

os.makedirs(csv_file_new_dir, exist_ok=True)

for csv_file_name in os.listdir(csv_file_dir):
    if csv_file_name.endswith(csv_file_suffix):
        print("Removing header from " + csv_file_name + "...")
        csv_new_lines = []
        csv_file_obj = open(os.path.join(csv_file_dir, csv_file_name))
        csv_file_reader = csv.reader(csv_file_obj)
        
        for each_line in csv_file_reader:
            if csv_file_reader.line_num == 1:
                continue
            
            csv_new_lines.append(each_line)
            
        csv_file_obj.close()
        
        csv_new_file_obj = open(os.path.join(csv_file_new_dir, csv_file_name), "w", newline="")
        csv_new_file_writer = csv.writer(csv_new_file_obj)
        csv_new_file_writer.writerows(csv_new_lines)
        csv_new_file_obj.close()