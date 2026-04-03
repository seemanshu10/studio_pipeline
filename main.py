import os
import sys
import json

# current working dictionary 
folder_path = os.path.dirname(os.path.abspath(__file__))

root_path = os.path.join(folder_path,"folder_template")

studio_template_path = os.path.join(root_path, "studio_template.json")
project_template_path = os.path.join(root_path, "project_template.json")


folder_pipeline_path= r"d:\PipelineTD\studio_pipeline\Pipeline"

def load_json_data(filepath):
    """
    load the json data 
    
    Parameters : 
    filePath : First Number

    returns : 
    json data returned in dict 
    """
    try:
        with open(filepath, "r") as json_file_data:
            content_json_data = json.load(json_file_data)

        return content_json_data    # returning json data 
    except FileNotFoundError:
        print(f"Error: File Path {filepath} not found! Check With TD.")

    except json.JSONDecodeError as e:
        print(f"Error: Connot Read config File.")

def create_structure(studio_template_path, structure_dict):
    for key, value in structure_dict.items():
        folder_path = os.path.join(studio_template_path, key)
        os.makedirs(folder_path, exist_ok=True)
        print(f"Created: {folder_path}")

def build_studio(studio_template_path):
    content_build_studio = load_json_data(studio_template_path)
  
    structure_dict = content_build_studio["studio_pipeline_folder"]
    # print(structure_dict)
    create_structure(folder_pipeline_path, structure_dict)

def create_project(folder_path, project_name, project_template_path):
    project_template_folders = load_json_data(project_template_path)
    # print(project_template_folders)
    # print(folder_path)

    project_folder_path_root = os.path.join(folder_path, "projects")
    project_folder_path = os.path.join(project_folder_path_root, project_name)

    # print(project_folder_path)
    structure_dict = project_template_folders["Project"]
    # print(structure_dict)

    create_structure(project_folder_path, structure_dict)

# Run once (setup studio)
build_studio(studio_template_path)

# Create new project
create_project(folder_pipeline_path, "MyFilm", project_template_path)
create_project(folder_pipeline_path, "MyFilm1", project_template_path)