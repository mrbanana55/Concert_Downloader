class ConcertError(Exception):
    def __init__(self, message, file=None):
        self.file = file
        super().__init__(message)