import os

def convert_dir_to_dict(root_dir):
    result = {}

    # Iterate over directories in the root directory
    for subject_dir in os.listdir(root_dir):
        subject_path = os.path.join(root_dir, subject_dir)
        if os.path.isdir(subject_path):
            subject_dict = {}
            result[subject_dir] = subject_dict

            # Iterate over directories inside the subject directory
            for chapter_dir in os.listdir(subject_path):
                chapter_path = os.path.join(subject_path, chapter_dir)
                if os.path.isdir(chapter_path):
                    chapter_dict = {}
                    subject_dict[chapter_dir] = chapter_dict

                    # Iterate over directories inside the chapter directory
                    for section_dir in os.listdir(chapter_path):
                        section_path = os.path.join(chapter_path, section_dir)
                        if os.path.isdir(section_path):
                            files = []
                            for filename in os.listdir(section_path):
                                file_path = os.path.join(section_path, filename)
                                if os.path.isfile(file_path):
                                    files.append(filename)
                            chapter_dict[section_dir] = files

    return result

root_dir =  os.path.join(os.getcwd(), "./") 
file_path = os.path.join(root_dir, "templates/from_pyvert.yml") 
asset_path = os.path.join(root_dir, "assets") 
#import json
#with open("./templates/from_pyvert.json", "w") as outfile: 
#    json.dump(convert_dir_to_dict("./assets"), outfile, sort_keys=True,indent=4) 

import yaml
with open(file_path, 'w') as outfile:
    yaml.dump(convert_dir_to_dict(asset_path), outfile, default_flow_style=False)