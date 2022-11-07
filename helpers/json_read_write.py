import datetime
import os
import json
from source.functionality import todo_list


def read_todo_list_json():
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, 'data', 'tasks.json')
    with open(file_path, 'r') as test_data1:
        read_todo_list = json.load(test_data1)
    for el_d in read_todo_list:
        el_d['due_date'] = datetime.datetime.fromisoformat(el_d['due_date'])
    return read_todo_list


def write_todo_list_json():
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, 'data', 'tasks.json')
    with open(file_path, 'w') as test_data1:
        todo_list_copy = todo_list.copy()
        for el_d in todo_list_copy:
            el_d['due_date'] = el_d['due_date'].isoformat()
        json.dump(todo_list, test_data1)



if __name__ == '__main__':
    pass
