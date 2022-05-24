class Jumper:
  """PUT COMMENT HERE"""
  def __init__(self):
    """PUT COMMENT HERE"""
    self.jumper = [
    '   ___',
    '  /   \\',
    '  -----',
    '  \\   /',
    '   \\ /',
    '    O',
    '   /|\\',
    '   / \\',
    '',
    '^^^^^^^^^'
    ]

  def print_jumper(self):
    """PUT COMMENT HERE"""
    for x in range(0, len(self.jumper)):
      print(self.jumper[x])

  def remove_line(self):
    """PUT COMMENT HERE"""
    self.jumper.remove(self.jumper[0])