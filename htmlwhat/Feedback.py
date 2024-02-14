from protowhat.Feedback import Feedback as BaseFeedback
from protowhat.Feedback import FeedbackComponent
from jinja2 import Template
from typing import List


class Feedback(BaseFeedback):
    def get_message(self) -> str:
        msgs = [*filter(lambda x: x is not None, self.context_components)]
        
        conclusion = self.describe(self.conclusion)
        if not self.conclusion.append:
            return conclusion

        prev = self.describe(msgs.pop()) if msgs else ""
        return prev + self.get_path(msgs) + (". " if prev else "") + conclusion

    @staticmethod
    def describe(msg: FeedbackComponent) -> str:
        return Template(msg.message.replace("__JINJA__:", "")).render(msg.kwargs)
    
    def get_path(self, msgs: List[FeedbackComponent]) -> str:
        if not msgs:
            return ""
        return " with in `" + " > ".join([msg.kwargs.get("index", "") + msg.kwargs.get("tag") for msg in msgs]) + "`"
    