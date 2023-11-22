#!/usr/bin/python3
""" Task 3 """

import json
import requests
import sys


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
    return response.json().get("name")


def export_all_to_json():
    """ Exports data to a json file """
    data_dict = {}

    for employeeId in range(1, 100):
        tasks = get_employee_tasks(employeeId)
        employeeName = get_employee_name(employeeId)

        employee_data = []
        for task in tasks:
            task_data = {
                "username": employeeName,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            employee_data.append(task_data)

        data_dict[str(employeeId)] = employee_data

    json_data = json.dumps(data_dict)

    filename = "todo_all_employees.json"
    with open(filename, "w") as jsonfile:
        jsonfile.write(json_data)


if __name__ == "__main__":
    export_all_to_json()
