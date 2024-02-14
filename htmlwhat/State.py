from bs4 import BeautifulSoup
from protowhat.State import State as BaseState
from htmlwhat.Reporter import Reporter
from protowhat.selectors import DispatcherInterface
from htmlwhat.Feedback import Feedback
from htmlwhat.utils import check_str


class BeautifulSoupNode(BeautifulSoup):
    """Treated as a node in the AST."""

    def get_position(self):
        return None


class HtmlDispatcher(DispatcherInterface):
    """Dispatcher for HTML AST."""

    def parse(self, code) -> BeautifulSoupNode:
        """function that parse the data and return the AST node."""
        return BeautifulSoupNode(code, 'html.parser')

    def describe(self, node) -> str:
        """function that returns the name of the node."""
        return node.name


class State(BaseState):
    feedback_cls = Feedback

    def __init__(
        self,
        student_code,
        solution_code,
        reporter=Reporter(),
        force_diagnose=False,
        highlight_offset=None,
        highlighting_disabled=False,
        feedback_context=None,
        creator=None,
        solution_ast=None,
        student_ast=None,
        ast_dispatcher=None,
    ):
        args = locals().copy()
        self.debug = False

        for k, v in args.items():
            if k != "self":
                setattr(self, k, v)

        if ast_dispatcher is None:
            self.ast_dispatcher = self.get_dispatcher()

        if check_str(self.solution_code, "arg: solution_code") and self.solution_ast is None:
            self.solution_code = self.solution_code.strip()
            self.solution_ast = self.parse(self.solution_code)
        if check_str(self.student_code, "arg: student_code") and self.student_ast is None:
            self.student_code = self.student_code.strip()
            self.student_ast = self.parse(self.student_code)

    def get_dispatcher(self):
        return HtmlDispatcher()

    def get_ast_path(self):
        # print([_.solution_ast.name for _ in self.state_history])
        # return self.ast_dispatcher.get_path(self.solution_ast)
        return "Code"
