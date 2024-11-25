# Created by daniel at 11/25/24
Feature: Loading of event logs
  # Enter feature description here

  Scenario: Loading a valid event log
    Given the process miner has successfully opened the application
    When they select the "Load Event Log" option and choose a valid XES file
    Then the application should load the event log data and display it in rows and columns with in the user interface.