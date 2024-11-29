Feature: Generation of DCR graph

  Scenario: Generating a DCR graph from an event log
    Given an event log is successfully loaded into the application
    When the process miner selects the "Generate DCR Graph" option
    Then the application should process the event log
    And display a DCR graph that accurately represents the process model derived from the event log data
