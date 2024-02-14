from htmlwhat.sct_context import get_checks_dict, create_sct_context
from htmlwhat import checks

SCT_CTX = create_sct_context(get_checks_dict(checks))

globals().update(SCT_CTX)

__all__ = list(SCT_CTX.keys())
