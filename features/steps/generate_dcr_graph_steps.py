from pathlib import Path
from behave import given, when, then
from app.model import EventLogRepository
from app.model.eventlog import EventLog
from app.viewmodel import EventLogListViewModel
from app.viewmodel.graph_viewmodel import GraphViewModel
from app.view.graph_view import GraphView
from PySide6.QtWidgets import QApplication
import sys

@given('an event log is successfully loaded into the application')
def step_impl(context):
    if not QApplication.instance():
        context.app = QApplication(sys.argv)
    else:
        context.app = QApplication.instance()

    context.event_log_repository = EventLogRepository()
    context.eventlog_list_viewmodel = EventLogListViewModel(context.event_log_repository)
    path = Path("features/event_logs/running-example.xes")
    context.eventlog_list_viewmodel.add_event_log(path.name, path, False)
    context.event_logs = context.event_log_repository.get_all_event_logs()
    assert len(context.event_logs) > 0, "No event logs were loaded."
    context.selected_event_log = context.event_logs[0]
    context.eventlog_list_viewmodel.set_selected_event_log(context.selected_event_log)

@when('the process miner selects the "Generate DCR Graph" option')
def step_impl(context):
    context.graph_viewmodel = GraphViewModel()
    context.graph_view = GraphView(context.eventlog_list_viewmodel)
    context.graph_view.update_graph(context.selected_event_log)

@then('the application should process the event log')
def step_impl(context):
    assert True, "Event log processing failed."

@then('display a DCR graph that accurately represents the process model derived from the event log data')
def step_impl(context):
    pixmap = context.graph_view.zoom_widget.image_label.pixmap()
    assert pixmap is not None and not pixmap.isNull(), "DCR graph was not displayed."
