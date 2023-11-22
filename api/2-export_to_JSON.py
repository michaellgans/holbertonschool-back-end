#!/usr/bin/python3
""" Task 2 """
import csv
import json
import requests
import sys
import urllib.request


def get_employee_tasks(employeeId):
    """ Returns all tasks associated with an employee """
    url = "https://jsonplaceholder.typicode.com/"
    url += "users/{}/todos".format(employeeId)
    response = requests.get(url)
    return response.json()


def get_employee_name(employeeId):
    """ Returns employee name from specific ID """
    url = "https://jsonplaceholder.typicode.com/"
    url += "users/{}".format(employeeId)
    response = requests.get(url)
    return response.json().get("username")


def print_employee_tasks(employeeName, completedTasks, totalTasks):
    """ Prints all tasks by employee ID """
    print("Employee {} is done with tasks({}/{}):"
          .format(employeeName, len(completedTasks), totalTasks))
    for task in completedTasks:
        print("\t {}".format(task.get("title")))


def export_to_json(employeeId, employeeName, completedTasks):
    """ Exports data to a json file """
    data_dict = {str(employeeId): []}

    for task in completedTasks:
        task_dict = {"task": task.get("title"),
                     "completed": task.get("completed"),
                     "username": employeeName}
        data_dict[str(employeeId)].append(task_dict)

    json_data = json.dumps(data_dict)

    filename = "{}.json".format(employeeId)
    with open(filename, "w") as jsonfile:
        jsonfile.write(json_data)


if __name__ == "__main__":
    employeeId = sys.argv[1]
    tasks = get_employee_tasks(employeeId)
    employeeName = get_employee_name(employeeId)
    export_to_json(employeeId, employeeName, tasks)
