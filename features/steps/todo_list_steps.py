from behave import given, when, then
from io import StringIO
import sys

# Function to simulate the user input for testing
def mock_input(inputs):
    return (input for input in inputs)

# Set up the environment for the tests
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
    from todo_list import add_task
    add_task(context.tasks)
    sys.stdout = context.original_stdout  # Restore original stdout

@when('I list all tasks')
def step_when_list_tasks(context):
    context.original_stdout = sys.stdout
    sys.stdout = StringIO()  # Redirect stdout to capture print statements
    from todo_list import list_tasks
    list_tasks(context.tasks)
    sys.stdout = context.original_stdout  # Restore original stdout

@when('I edit the task to have details "{task}", "{due_date}", "{importance}"')
def step_when_edit_task(context, task, due_date, importance):
    context.original_stdout = sys.stdout
    sys.stdout = StringIO()  # Redirect stdout to capture print statements
    input_values = ['1', task, due_date, importance]  # Mock task index as '1'
    sys.stdin = StringIO('\n'.join(input_values))  # Mock user input
    from todo_list import edit_task
    edit_task(context.tasks)
    sys.stdout = context.original_stdout  # Restore original stdout

@when('I clear the list')
def step_when_clear_list(context):
    context.original_stdout = sys.stdout
    sys.stdout = StringIO()  # Redirect stdout to capture print statements
    from todo_list import clear_list
    clear_list(context.tasks)
    sys.stdout = context.original_stdout  # Restore original stdout

@then('the task list should contain one task with details "{task}", "{due_date}", "{importance}"')
def step_then_task_list_contains(context, task, due_date, importance):
    assert len(context.tasks) == 1
    assert context.tasks[0] == [task, due_date, importance]

@then('I should see one task with details "{task}", "{due_date}", "{importance}"')
def step_then_task_list_displayed(context, task, due_date, importance):
    output = sys.stdout.getvalue()
    assert f"1. {task} (Due: {due_date}, Importance: {importance})" in output

@then('the to-do list should be empty')
def step_then_list_empty(context):
    assert len(context.tasks) == 0
