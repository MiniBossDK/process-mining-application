from pathlib import Path
from behave import given, when, then
from app.model import EventLogRepository, EventLog
from app.viewmodel import EventLogListViewModel
from app.view.event_log_table_view import EventLogDataTableView

@given('the process miner has loaded at least one event log')
def given_loaded_event_log(context):
    # Initialize the EventLogRepository and EventLogListViewModel
    context.event_log_repository = EventLogRepository()
    context.eventlog_list_viewmodel = EventLogListViewModel(context.event_log_repository)
    # Load an event log into the repository
    path = Path("features/event_logs/running-example.xes")
    context.eventlog_list_viewmodel.add_event_log(path.name, path, False)
    # Retrieve the added event log
    context.event_logs = context.event_log_repository.get_all_event_logs()
    assert len(context.event_logs) > 0, "No event logs were loaded."

@when('they select an event log')
def when_select_event_log(context):
    # Simulate selecting the first event log
    context.selected_event_log = context.event_logs[0]
    context.eventlog_list_viewmodel.set_selected_event_log(context.selected_event_log)
    # Store a flag to indicate selection
    context.event_log_selected = True

@then('the application should display the details of the selected event log')
def then_display_event_log_details(context):
    assert context.event_log_selected, "No event log was selected."
    # Initialize the EventLogDataTableView with the viewmodel
    event_log_table_view = EventLogDataTableView(context.eventlog_list_viewmodel)
    # The table data should have been updated via the selected_event_log_changed signal
    # Access the table widget to verify the displayed data
    table_widget = event_log_table_view.table_view
    expected_data = context.selected_event_log.data  # pandas DataFrame
    # Verify the number of rows and columns
    assert table_widget.rowCount() == len(expected_data.index), \
        f"Expected {len(expected_data.index)} rows, got {table_widget.rowCount()}."
    assert table_widget.columnCount() == len(expected_data.columns), \
        f"Expected {len(expected_data.columns)} columns, got {table_widget.columnCount()}."
    # Optionally, verify the column headers
    headers = [table_widget.horizontalHeaderItem(i).text() for i in range(table_widget.columnCount())]
    expected_headers = list(expected_data.columns)
    assert headers == expected_headers, f"Expected headers {expected_headers}, got {headers}."
    # Verify that some sample data matches
    for i in range(min(5, table_widget.rowCount())):  # Check first 5 rows
        for j in range(table_widget.columnCount()):
            item = table_widget.item(i, j)
            expected_value = str(expected_data.iloc[i, j])
            actual_value = item.text() if item else ""
            assert actual_value == expected_value, \
                f"At cell ({i}, {j}), expected '{expected_value}', got '{actual_value}'."
