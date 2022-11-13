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
        return self.done

    def change_priority(self,new_priority):
        #new_priority = input('Write new priority: ')
        self.priority = new_priority
        return new_priority

    def to_dict(self):
        return {
            'id':self.id,
            'title':self.title,
            'description':self.description,
            'priority':self.priority,
            'due_date':self.due_date,
            'done':self.done
        }


my_test = Task(1, "Buy book", "Psychological book", 3,datetime(2022,11,23), False)
print()

if __name__ == '__main__':
    print(my_test.change_priority())
    print(my_test.done_task())