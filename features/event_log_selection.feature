# Created by daniel at 11/28/24
Feature: Event log selection

  Scenario: Selecting an eventlog
    Given the process miner has loaded at least one event log
    When they select an event log
    Then the application should