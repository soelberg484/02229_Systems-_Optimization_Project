class Stream:
  def __init__(self, id, src, dest, size, period, deadline, rl):
    self.id = id
    self.src = src
    self.dest = dest
    self.size = size
    self.period = period
    self.deadline = deadline
    self.rl = rl


class Device:
  def __init__(self, name, type):
    self.name = name
    self.type = type

class Link:
  def __init__(self, src, dest, speed):
    self.src = src
    self.dest = dest
    self.speed = speed

