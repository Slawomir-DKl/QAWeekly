import shutil
import os
input_files = os.listdir('input')
output_files = os.listdir('output')
for i in range(len(input_files)):
    with open(f"input/{input_files[i]}", encoding='utf8') as file:
        lines = file.readlines()
        for line in lines:
            if "<title>" in line:
                ind = line.index("Weekly")
                file_name = "QA Weekly "
                if line[ind + 9] == "<":
                    file_name += "0" + line[ind + 8:ind+9]
                else:
                    file_name += line[ind + 8:ind+10]
                break
        if file_name not in output_files:
            shutil.copy(f"input/{input_files[i]}", f"output/{file_name}.html")
