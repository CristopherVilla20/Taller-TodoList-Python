Feature: To-do List Management

  Scenario: Add a new task
    Given the to-do list is empty
    When I add a new task with details "Buy groceries", "2024-08-15", "3"
    Then the task list should contain one task with details "Buy groceries", "2024-08-15", "3"

  Scenario: List all tasks
    Given the to-do list contains one task with details "Buy groceries", "2024-08-15", "3"
    When I list all tasks
    Then I should see one task with details "Buy groceries", "2024-08-15", "3"

  Scenario: Edit an existing task
    Given the to-do list contains one task with details "Buy groceries", "2024-08-15", "3"
    When I edit the task to have details "Buy milk", "2024-08-16", "2"
    Then the task list should contain one task with details "Buy milk", "2024-08-16", "2"

  Scenario: Clear the entire list
    Given the to-do list contains one task with details "Buy groceries", "2024-08-15", "3"
    When I clear the list
    Then the to-do list should be empty
