import os.path
from time import sleep
from source import functionality
from datetime import datetime
from helpers import json_read_write




functions_list = {
    1: 'show_possible_actions',
    2: 'show_all_tasks',
    3: 'add_task',
    4: 'search_by_title',
    5: 'done task',
    6: 'change_priority',
    7: 'delete_task',
    8: 'show titles',
    9: 'show titles order by priority',
    10: 'show titles of unfinished act',
    11: 'show titles of finished act',
    12: 'show titles of time off',
    13: 'show statistic information',
    14: 'save as csv file',
    15: 'downland test data',
    16: 'exit'

}


def main():
    file_path = os.path.join(os.getcwd(), 'data', 'tasks.json')
    if os.path.isfile(file_path) is True:
        functionality.todo_list = json_read_write.read_todo_list_json()

    while True:
        sleep(5)
        os.system('cls')
        print('Possible actions')
        for action_id, task_name in functions_list.items():
            print(f'{action_id}: {task_name}')

        action_id = int(input('please choose action: '))
        if action_id == 1:
            for action_id, task_name in functions_list.items():
                print(f'{action_id}: {task_name}')

        if action_id == 2:
            functionality.show_todo_list()

        if action_id == 3:
            title = input('please enter title: ')
            description = input('please enter description: ')
            priority = int(input('please enter priority: '))
            due_date_s = input('please enter due date in next format yyyy-mm-dd: ')
            due_date_d = datetime.strptime(due_date_s, '%Y-%m-%d')
            functionality.add_entry(
                title=title,
                description=description,
                priority=priority,
                due_date=due_date_d
            )
            print('Entry was succesfully added')

        if action_id == 4:
            query = input('please enter search query: ')
            found_tasks = functionality.search_task_by_title(query)
            print(found_tasks)

        if action_id == 5:
            task_id = int(input('Please pass task id: '))
            functionality.done_task(task_id)

        if action_id == 6:
            task_id = int(input('Please pass task id: '))
            new_priority = int(input('Please choose new priority: '))
            functionality.change_priority(task_id, new_priority)

        if action_id == 7:
            task_id = int(input('Please pass task id: '))
            functionality.delete_task(task_id)

        if action_id == 8:
            functionality.show_titles()

        if action_id == 9:
            functionality.show_titles_for_priority()

        if action_id == 10:
            functionality.show_title_for_unfinished()

        if action_id == 11:
            functionality.show_title_for_finished()

        if action_id == 12:
            functionality.show_title_time_off()

        if action_id == 13:
            functionality.statistic_list()

        if action_id == 14:
            functionality.save_as_csv_file()

        if action_id == 15:
            functionality.downlad_test_data()

        if action_id == 16:
            json_read_write.write_todo_list_json()
            break


if __name__ == '__main__':
    main()