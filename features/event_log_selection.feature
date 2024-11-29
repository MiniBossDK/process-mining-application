Feature: Event log selection

  Scenario: Selecting an event log
    Given the process miner has loaded at least one event log
    When they select an event log
    Then the application should display the details of the selected event log
