from datetime import datetime
from helpers.classtodolist import Task

TEST_DATA = [
    Task(
        id=1,
        title="Buy book",
        description="Psychological book",
        priority=3,
        due_date=datetime(2022, 9, 24, 16, 00),
        done=True
),

    Task(**{
        "id": 2,
        "title": "Shopping",
        "description": "Grosery shopping",
        "priority": 4,
        "due_date": datetime(2022, 11, 1, 12, 37),
        "done": False
    }),
    Task(**{
        "id": 3,
        "title": "Bake a cheesecake",
        "description": "Buy cremchees and nuts",
        "priority": 2,
        "due_date": datetime(2022, 10, 13, 18, 45),
        "done": False
    }),
    Task(**{
        "id": 4,
        "title": "Visit cosmetology",
        "description" : "buy cream",
        "priority": 1,
        "due_date": datetime(2022, 11, 13, 14, 00),
        "done": False
    })
]