from datetime import datetime

TEST_DATA = [
    {
        "id": 1,
        "title": "Buy book",
        "description": "Psychological book",
        "priority": 3,
        "due_date": datetime(2022, 9, 24, 16, 00),
        "done": True
    },

    {
        "id": 2,
        "title": "Shopping",
        "description": "Grosery shopping",
        "priority": 4,
        "due_date": datetime(2022, 11, 1, 12, 37),
        "done": False
    },
    {   "id": 3,
        "title": "Bake a cheesecake",
        "description": "Buy cremchees and nuts",
        "priority": 2,
        "due_date": datetime(2022, 10, 13, 18, 45),
        "done": False
    },
    {
        "id": 4,
        "title": "Visit cosmetology",
        "priority": 1,
        "due_date": datetime(2022, 11, 13, 14, 00),
        "done": False
    }
]