from pathlib import Path

from behave import *

from app.model import EventLogRepository
from app.viewmodel import EventLogListViewModel


@given('the process miner has successfully opened the application')
def setup_event_log_model(context):
    context.event_log_repository = EventLogRepository()
    context.eventlog_list_viewmodel = EventLogListViewModel(context.event_log_repository)


@when('they select the "Load Event Log" option and choose a valid XES file')
def user_selected_event_log(context):
    path = Path("features/event_logs/running-example.xes")
    context.eventlog_list_viewmodel.add_event_log(path.name, path, False)

@then('the application should load the event log data and display it in the list of event logs')
def verify_loaded_event_log(context):
    assert context.event_log_repository.get_all_event_logs()[0].name == "running-example.xes"

