import os
import sys
import json
import shutil

# current working dictionary 
BASE_DIR  = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR  = os.path.join(BASE_DIR ,"folder_template")

# STUDIO_TEMPLATE  = os.path.join(TEMPLATE_DIR, "studio_template.json")
# PROJECT_TEMPLATE  = os.path.join(TEMPLATE_DIR, "project_template.json")

PIPELINE_ROOT = r"d:\PipelineTD\studio_pipeline\Pipeline"

def load_json_data(filepath):
    """
    load the json file and data safely
    
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
        print(f"Invalid JSON in {filepath}: {e}")

def create_structure(folder_creation_path, structure_dict):
    """
    Recursively create folder structure 
    
    Parameters : 
    studio_template_path : path for the folders 
    structure_dict : dictionary date 

    """
    for nameFolder, subfolders in structure_dict.items():
        folder_path = os.path.join(folder_creation_path, nameFolder)
        os.makedirs(folder_path, exist_ok=True)
        print(f"Created: {folder_path}")

def build_studio():
    """
    Setup studio pipeline structure.
    
    """
    studio_template_path  = os.path.join(TEMPLATE_DIR, "studio_template.json")
    content_build_studio = load_json_data(studio_template_path)
    
    structure_dict = content_build_studio["studio_pipeline_folder"]
    create_structure(PIPELINE_ROOT, structure_dict)

def create_project(project_name):

    """
    Initialize project folders 
    
    """
    project_template_path  = os.path.join(TEMPLATE_DIR, "project_template.json")
    project_template_folders = load_json_data(project_template_path)
    # print(project_template_path)
    # print(project_template_folders)

    project_root_path = os.path.join(PIPELINE_ROOT, "projects", project_name)
    os.makedirs(project_root_path, exist_ok=True)
    structure_dict = project_template_folders["Project"]

    create_structure(project_root_path, structure_dict)

def publish_versionup():
    version_des = "version"
    file_path = "folder_template/assets_template.json"

    os.makedirs(version_des,exist_ok=True)

    base_name = os.path.basename(file_path)
    name , ext = os.path.splitext(base_name) 
    print(base_name)
    print(name, ext)

    # find next vewrsion number 
    version = 1
    while True:
        new_name = f"{name}_V{version:03d}{ext}"
        dest_path = os.path.join(version_des, new_name)

        if not os.path.exists(dest_path):
            break

        version += 1

    # copy file 
    shutil.copy2(file_path, dest_path)

    print("Crerated:", dest_path)
        
        

if __name__ == "__main__":

    # Run once (setup studio)
    # build_studio()

    # # Create new project
    # create_project("MyFilm")
    # create_project("MyFilm1")

    publish_versionup()