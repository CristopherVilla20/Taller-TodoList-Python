from behave import given, when, then
from io import StringIO
import sys
import importlib

# Importa el script con las funciones de la lista de tareas
todo_list = importlib.import_module('todo_list')

@given('the to-do list is empty')
def step_given_empty_list(context):
    context.tasks = []

@given('the to-do list contains one task with details "{task}", "{due_date}", "{importance}"')
def step_given_list_with_task(context, task, due_date, importance):
    context.tasks = [[task, due_date, importance]]

@when('I add a new task with details "{task}", "{due_date}", "{importance}"')
def step_when_add_task(context, task, due_date, importance):
    context.original_stdout = sys.stdout
    sys.stdout = StringIO()  # Redirect stdout to capture print statements
    input_values = [task, due_date, importance]
    sys.stdin = StringIO('\n'.join(input_values))  # Mock user input
    todo_list.add_task(context.tasks)
    sys.stdout = context.original_stdout  # Restore original stdout

@when('I list all tasks')
def step_when_list_tasks(context):
    context.original_stdout = sys.stdout
    sys.stdout = StringIO()  # Redirect stdout to capture print statements
    todo_list.list_tasks(context.tasks)
    context.output = sys.stdout.getvalue()  # Capture the output
    sys.stdout = context.original_stdout  # Restore original stdout

@when('I edit the task to have details "{task}", "{due_date}", "{importance}"')
def step_when_edit_task(context, task, due_date, importance):
    context.original_stdout = sys.stdout
    sys.stdout = StringIO()  # Redirect stdout to capture print statements
    input_values = ['1', task, due_date, importance]  # Mock task index as '1'
    sys.stdin = StringIO('\n'.join(input_values))  # Mock user input
    todo_list.edit_task(context.tasks)
    sys.stdout = context.original_stdout  # Restore original stdout

@when('I clear the list')
def step_when_clear_list(context):
    context.original_stdout = sys.stdout
    sys.stdout = StringIO()  # Redirect stdout to capture print statements
    todo_list.clear_list(context.tasks)
    sys.stdout = context.original_stdout  # Restore original stdout

@then('the task list should contain one task with details "{task}", "{due_date}", "{importance}"')
def step_then_task_list_contains(context, task, due_date, importance):
    assert len(context.tasks) == 1
    assert context.tasks[0] == [task, due_date, importance]

@then('I should see one task with details "{task}", "{due_date}", "{importance}"')
def step_then_task_list_displayed(context, task, due_date, importance):
    expected_output = f"1. {task} (Due: {due_date}, Importance: {importance})"
    assert expected_output in context.output, f"Expected '{expected_output}' but got '{context.output}'"

@then('the to-do list should be empty')
def step_then_list_empty(context):
    assert len(context.tasks) == 0
