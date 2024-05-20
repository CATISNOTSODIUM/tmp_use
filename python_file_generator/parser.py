#!pip install faker        
#!pip install mdgen
#!pip install mdprint
#!pip install dominate

import os 
from faker import Faker
from mdgen import MarkdownPostProvider
from mdprint import mdprint

import glob 
import dominate
from dominate.tags import *

def create_dir(curr_path:str, dir_name:str):
    try:
        new_path = os.path.join(curr_path, dir_name)
        os.mkdir(new_path)
    except:
        print(dir_name, "has already been initialized"); 


def generate_markdown(curr_path: str, file_name: str):
    fake = Faker()

    fake.add_provider(MarkdownPostProvider)
    fake_post = fake.post(size='medium') # available sizes: 'small', 'medium', 'large'    
    #generate files
    with open(os.path.join(curr_path,file_name), 'w') as f:
        mdprint( fake_post, heading=2, file=f)

def create_dir_from_tree(directory_tree, root, *args, **kwargs):
    
    #optional arguments (bool)
    with_convention = kwargs.get("with_convention") #follows the directory and file convention
    with_seeds = kwargs.get("with_seeds") 
    path_iter = root
    
    if (not with_convention):
        for course_name in directory_tree:
            
            create_dir(path_iter, course_name)
            course_path = os.path.join(path_iter,course_name)

            for skill_set in directory_tree[course_name]:
                
                create_dir(course_path, skill_set)
                skill_set_path = os.path.join(course_path,skill_set)
            
                for skill in directory_tree[course_name][skill_set]:
                    
                    create_dir(skill_set_path, skill)
                    skill_path = os.path.join(skill_set_path,skill)
                    
                    for file_name in directory_tree[course_name][skill_set][skill]:
                        #create random markdown
                        if (with_seeds): generate_markdown(skill_path, file_name)
    else: #follows convention
        for course_name in directory_tree:
            course_name_dir = course_name
            create_dir(path_iter, course_name_dir)
            course_path = os.path.join(path_iter,course_name_dir)

            for skill_set in directory_tree[course_name]:
                skill_set_dir = course_name + '_' + skill_set
                create_dir(course_path, skill_set_dir)
                skill_set_path = os.path.join(course_path,skill_set_dir)
            
                for skill in directory_tree[course_name][skill_set]:
                    skill_dir = course_name + '_' + skill_set + '_'+skill
                    create_dir(skill_set_path, skill_dir)
                    skill_path = os.path.join(skill_set_path,skill_dir)
                    
                    for file_name in directory_tree[course_name][skill_set][skill]:
                        #create random markdown
                        generate_markdown(skill_path, file_name)
                        
def generate_html(directory_tree, root, *args, **kwargs):
    with_convention = kwargs.get("with_convention") #follows the directory and file convention (bool)
    
    
    path_iter = ""
    root_link = "http://localhost:3000"
    prefix_link = "http://localhost:3000/receiver/`?name="
    if (with_convention):
        doc = dominate.document(title='File directories')
        with doc.head:
            link(rel="preconnect", href="https://fonts.googleapis.com")
            link(rel="preconnect", href="https://fonts.gstatic.com")
            link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Inter:wght@100..900&display=swap")
            style(r'body{background-color:#dedede;color: #000000;font-family: Inter, sans-serif;}')
        with doc:
            with div(id='header'):
                attr(cls='body')
                h2('File directories')
                a("Raw data", href=os.path.join(root_link, "tree_raw"))
            with div():
                attr(cls='body')
                for course_name in directory_tree:
                    course_name_dir = course_name
                    h3(course_name_dir)
                    for skill_set in directory_tree[course_name]:
                        skill_set_dir = course_name + '_' + skill_set
                        h4(skill_set_dir)
                        for skill in directory_tree[course_name][skill_set]:
                            skill_dir = course_name + '_' + skill_set + '_'+skill
                            p(skill_dir)
                            for file_name in directory_tree[course_name][skill_set][skill]:
                                li(a(file_name, href=os.path.join(prefix_link + course_name_dir, skill_set_dir, skill_dir, file_name)))
    else:
        doc = dominate.document(title='File directories')
        with doc:
            with div(id='header'):
                attr(cls='body')
                h2('File directories')
            with div():
                attr(cls='body')
                for course_name in directory_tree:
                    course_name_dir = course_name
                    h3(course_name_dir)
                    for skill_set in directory_tree[course_name]:
                        skill_set_dir = skill_set
                        h4(skill_set_dir)
                        for skill in directory_tree[course_name][skill_set]:
                            skill_dir = skill
                            p(skill_dir)
                            for file_name in directory_tree[course_name][skill_set][skill]:
                                li(a(file_name, href=os.path.join(prefix_link + course_name_dir, skill_set_dir, skill_dir, file_name)))
    with open(os.path.join(root,"index.html"), "w") as f:
        f.write(doc.render())