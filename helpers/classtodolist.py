from datetime import datetime

class Task:

    def __init__(self, id: int, title: str, description: str, priority: int, due_date: datetime, done: bool):
        self.id = id
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.done = done

    def done_task(self):
        self.done = True

    def change_priority(self, new_priority):
        if 1 <= new_priority <= 10:
            self.priority = new_priority
        else:
            print('Please write correct number for 1 to 10')

    def to_dict(self):
        return {
            'id':self.id,
            'title':self.title,
            'description':self.description,
            'priority':self.priority,
            'due_date':self.due_date,
            'done':self.done
        }


if __name__ == '__main__':
    print(my_test.change_priority())
    print(my_test.done_task())