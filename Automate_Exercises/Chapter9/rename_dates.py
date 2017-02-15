import re, shutil, os

data_pattern = r"^(.*?)((0|1)?\d)-((0|1|2|3)?\d)-((19|20)\d\d)(.*?)$"

for amer_file in os.listdir():
    if os.path.isfile(amer_file):
        match_result = re.search(data_pattern, amer_file)
        
        if match_result == None:
            continue
        
        beforePart = match_result.group(1)
        monthPart = match_result.group(2)
        dayPart = match_result.group(4)
        yearPart = match_result.group(6)
        afterPart = match_result.group(8)
        
        euro_file = beforePart + dayPart + "-" + monthPart + "-" + yearPart + afterPart
        abs_working_dir = os.path.abspath(".")
        amer_file = os.path.join(abs_working_dir, amer_file)
        euro_file = os.path.join(abs_working_dir, euro_file)
        
        print("Renaming '%s' to '%s'..." % (amer_file, euro_file))
        shutil.move(amer_file, euro_file)