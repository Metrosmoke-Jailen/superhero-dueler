class Hero:
  def __init__(self, name, starting_health=100):
    '''Instance properties:
      name: String
      starting_health: Integer
      current_health: Integer
    '''

    self.name = name
    self.starting_health = starting_health
    self.current_health = starting_health