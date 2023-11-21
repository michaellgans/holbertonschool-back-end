#!/usr/bin/python3
""" Task 1 """

import requests
import sys
import csv


def employee_tasks(employeeId):
    """ Returns all tasks associated with an employee """
    url = "https://jsonplaceholder.typicode.com/"
    url += "users/{}/todos".format(employeeId)
    response = requests.get(url)
    return response.json()


def employee_name(employeeId):
    """ Returns employee name from specific ID """
    url = "https://jsonplaceholder.typicode.com/"
    url += "users/{}".format(employeeId)
    response = requests.get(url)
    return response.json().get("name")


def completed_tasks(tasks):
    """ Returns all completed tasks """
    completed_tasks = []

    for task in tasks:
        if task.get("completed"):
            completed_tasks.append(task)
    return completed_tasks


def print_report(employeeName, completedTasks, totalTasks):
    """ Prints all tasks by employee ID """
    print("Employee {} is done with tasks({}/{}):"
          .format(employeeName, len(completedTasks), totalTasks))
    for task in completedTasks:
        print("\t {}".format(task.get("title")))

    with open("{}.csv".format(eployeeID), "w") as csvfile:
        bytes_written = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for item in tasks:
            bytes_written.writerow([employeeID, employeeName,
                                    task.get("completed"), task.get("title")])


if __name__ == "__main__":
    employeeId = sys.argv[1]
    tasks = employee_tasks(employeeId)
    employeeName = employee_name(employeeId)
    completedTasks = completed_tasks(tasks)
    print_report(employeeName, completedTasks, len(tasks))
