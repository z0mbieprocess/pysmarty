"""Pysmarty Exceptions."""


class PysmartyBaseException(Exception):
    """Base Exception for pysmarty."""


class PysmartyException(PysmartyBaseException):
    """Pysmarty Exception."""

    def __init__(self, message, errors):
        """Exception Init."""
        super().__init__(message)
        self.errors = errors
