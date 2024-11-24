class ConformanceCheckingViewModel:
    def __init__(self):
        self.event_log_loaded = False

    def perform_rule_checking(self):
        # Implement the logic for rule-based conformance checking
        print("Rule-based conformance checking performed")

    def perform_alignment_checking(self):
        # Implement the logic for alignment-based conformance checking
        print("Alignment-based conformance checking performed")

    def is_event_log_loaded(self):
        return self.event_log_loaded

    def set_event_log_loaded(self, loaded):
        self.event_log_loaded = loaded
