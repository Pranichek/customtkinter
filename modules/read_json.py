import json
import os

def read_json(file_name:str):
    path_file = os.path.abspath(__file__ + f"/../../static/{file_name}")
    with open(path_file, "r") as file:
        return json.load(file)
    