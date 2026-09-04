class NegativeIntegerError(Exception):
  def __init__(self, message = 'Negative number are not allowed!'):
    self.message = message
    super().__init__(message)
