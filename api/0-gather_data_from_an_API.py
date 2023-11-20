#!/usr/bin/python3
""" Task 0 - Gather data from API """

import requests
import sys


def employee_tasks(ID):
    """ Returns all tasks of an employee """
    url = "https://jsonplaceholder.typicode.com/"
    url += "users/{}/todos".format(ID)
    response = requests.get(url)
    return response.json()


def employee_name(ID):
    """ Returns name of employee """
    url = "https://jsonplaceholder.typicode.com/"
    url += "users/{}".format(ID)
    response = requests.get(url)
    return response.json().get("name")


def completed_tasks(tasks):
    """ Returns completed tasks """
    completed_tasks = []

    for item in tasks:
        if item.get("completed"):
            completed_tasks.append(item)
    return completed_tasks


def print_report(employee_name, tasks_completed, tasks_total):
    """ Displays report of tasks by employee ID """
    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, len(tasks_completed), len(tasks_total)))
    for item in tasks_completed:
        print("t/ {}".format(item.get("title")))


if __name__ == "__main__":
    ID = sys.argv[1]
    tasks = employee_tasks(ID)
    employee_name = employee_name(ID)
    completed_tasks = tasks_completed(tasks)
    print_report(employee_name, completed_tasks, len(tasks))
