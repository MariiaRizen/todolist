import csv
from datetime import datetime
from data.test import TEST_DATA
from helpers.classtodolist import Task


# todo_list = TEST_DATA
todo_list = []


def add_entry(
        ftitle: str,
        fdue_date: datetime,
        fdescription: str = '',
        fpriority: int = 1,
):
    """ add new entry"""
    new_id = len(todo_list) + 1
    task_o = Task(
        id=new_id,
        title=ftitle,
        description=fdescription,
        priority=fpriority,
        due_date=fdue_date,
        done=False
    )

    # task_d = {
    #     'id': new_id,
    #     'title': title,
    #     'description': description,
    #     'priority': priority,
    #     'due_date': due_date,
    #     'done': False,
    # }
    todo_list.append(task_o)


def show_todo_list():
    """Show all list of case record"""
    print([x.to_dict() for x in todo_list])


def search_task_by_title(query: str):
    """ Search task by title in to do list"""
    return [x.to_dict() for x in todo_list if query in x.title]


def done_task(task_id):
    """ Find and mark a task as completed"""
    task = [x for x in todo_list if x.id == task_id]
    if not task:
        print('task was not found')
    else:
        # task[0].done = True
        task[0].done_task()
        print('Task status was successfully changed')


def change_priority(task_id, new_priority):
    """ Find a case and change its priority"""
    task = [x for x in todo_list if x.id == task_id]
    if not task:
        print('task was not found')
    else:
        #task[0].priority = new_priority
        task[0].change_priority(new_priority)


def delete_task(task_id):
    """ Log in and delete the case"""
    global todo_list
    # task = [x for x in todo_list if x['id'] == task_id]
    todo_list = [x for x in todo_list if x.id != task_id]
    # todo_list.remove(task)


def show_titles():
    """ View all scheduled cases (names only) in the order they were added"""
    title_list = [x.title for x in todo_list]
    print(title_list)


def show_titles_for_priority():
    """ View all scheduled cases (names only) in descending order of priority"""
    sorted_list = sorted(todo_list, key=lambda x: x.priority)
    titles_list = [x.title for x in sorted_list]
    print(titles_list)


def show_title_for_unfinished():
    """ View all open cases (names only)"""
    done_list = [x for x in todo_list if x.done == False]
    titles_list = [x.title for x in done_list]
    print(titles_list)


def show_title_for_finished():
    """ View completed cases (names only)"""
    done_list = [x for x in todo_list if x.done == True]
    titles_list = [x.title for x in done_list]
    print(titles_list)


def show_title_time_off():
    """ View overdue cases (titles only)"""
    time_off_list = [x.title for x in todo_list if x.done == False and x.due_date < datetime.now()]
    print(time_off_list)


def statistic_list():
    """ View statistics (total number of cases, number of executed/unexecuted/overdue cases)"""
    no_done_list = len([x for x in todo_list if x.done == False])
    done_list = len([x for x in todo_list if x.done == True])
    time_off_list = len([x for x in todo_list if x.due_date < datetime.now()])
    print('Total number of cases is ' + str(len(todo_list)) + '\n' + 'Number of done cases ' + str(done_list) + '\n' + 'Number of no done cases is ' + str(no_done_list) + '\n' + 'Number of time off cases is ' + str(time_off_list) )


def save_as_csv_file():
    """ Save the to-do list as a csv file."""
    with open('data/todolistcsvfile.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow([
            "id",
            "title",
            "description",
            "priority",
            "due_date",
            "done"])
        for obj in todo_list:
            row = obj.to_dict()
            w.writerow(row.values())


def download_test_data():
    """ Download test data"""
    # global todo_list
    # todo_list = TEST_DATA
    todo_list = [x.to_dict() for x in TEST_DATA]
    print(todo_list)


if __name__ == '__main__':

    d1 = '2022-12-21'
    add_entry(title='title',
              description='description',
              priority=2,
              due_date=datetime.strptime(d1, '%Y-%m-%d'))
    # print(search_task_by_title('t'))
    # done_task(1)

    print(todo_list)

    delete_task(1)

    print(todo_list)

