class ToolsNotFound(Exception):
    def __init__(self, arg):
        self.args = (arg,)