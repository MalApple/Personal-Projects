# Task-Tracker
A command line interface (CLI) to track what I need to do, what I have done, and what I am currently working on.

Data is sotred in dictonary format in a local JSON file which is created if there is none initially. This file is updated everytime a new item is altered. Using clearlist will delete this JSON file.

# How to use
Add item:
    python task_cli.py add "Task"

Delete item:
    python task_cli.py delete id

Clear list:
    python task_cli.py clearlist

Update item:
    python task_cli.py id "New description"

Change status of item:
    python task_cli.py in-progress
    python task_cli.py mark-done
    
List of items:
    python task_cli.py list
    python task_cli.py list done
    python task_cli.py list in-progress 