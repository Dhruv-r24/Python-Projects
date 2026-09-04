class NegativeIntegerError(Exception):
  def __init__(self, message = 'Negative number are not allowed!'):
    self.message = message
    super().__init__(message)

class ZeroOrOneFilesError(Exception):
  def __init__(self, message = 'The entered number of files cannot be merged.'):
    self.message = message
    super().__init__(message)
