from PySide6.QtCore import Qt, QModelIndex
from behave import *

import pm4py
from app.model import EventLogListModel, EventLog


@given('the process miner has successfully opened the application')
def setup_event_log_model(context):
    context.event_log_model = EventLogListModel([])

@when('they select the "Load Event Log" option and choose a valid XES file')
def user_selected_event_log(context):
    event_log = pm4py.read_xes("features/event_logs/running-example.xes")
    context.event_log_model.add_event_log(EventLog("running-example.xes", event_log))

@then('the application should load the event log data and display it in the list of event logs')
def verify_loaded_event_log(context):
    event_log_name = context.event_log_model.data(QModelIndex(), Qt.ItemDataRole.DisplayRole)
    assert event_log_name == "running-example.xes"

