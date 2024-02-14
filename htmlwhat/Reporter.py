from protowhat.Reporter import Reporter as BaseReporter
from htmlwhat.Feedback import Feedback


class Reporter(BaseReporter):
    def build_failed_payload(self, feedback: Feedback):
        return {
            "correct": False,
            "message": Reporter.to_html(feedback.get_message()),
        }