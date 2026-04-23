class InterviewSession:

    def __init__(self, role_applied):
        self.role_applied = role_applied
        self.count = 0
        self.history = []

    def add_message(self, role, message):
        self.history.append({"role": role, "parts": [{"text": message}]})

    def increment_count(self):
        self.count += 1

    def is_complete(self):
        return self.count == 5
