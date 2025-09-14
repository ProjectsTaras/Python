#GameState będzie reprezentować cały stan naszej gry
#snake - lista przechowująca pozycję elementów węża (gdzie pierwszy element to sam koniec, a ostatni element jest głową),
#food - pozycja jedzenia,
#direction - w którym kierunku wąż się kieruje,
#field_size - jaka jest wielkość planszy

class GameState:
    def __init__(self,
                 snake,
                 direction,
                 food,
                 field_size):
        self.snake = snake
        self.direction = direction
        self.food = food
        self.field_size = field_size
#Funkcja next_head powinna zwracać nową pozycję głowy węża.
def next_head(self, direction):
    pos = self.snake[-1]
    if direction == Direction.UP:
        return Position(pos.x, pos.y - 1)
    elif direction == Direction.DOWN:
        return Position(pos.x, pos.y + 1)
    elif direction == Direction.RIGHT:
        return Position(pos.x + 1, pos.y)
    elif direction == Direction.LEFT:
        return Position(pos.x - 1, pos.y)
    
def step(self):
    new_head = self.next_head(self.direction)
    self.snake.append(new_head)
    self.snake = self.snake[1:]

#.............................

def next_head(self, direction):
    pos = self.snake[-1]
    if direction == Direction.UP:
        return Position(
            pos.x,
            (pos.y - 1) % self.field_size
        )
    elif direction == Direction.DOWN:
        return Position(
            pos.x,
            (pos.y + 1) % self.field_size
        )
    elif direction == Direction.RIGHT:
        return Position(
            (pos.x + 1) % self.field_size,
            pos.y
        )
    elif direction == Direction.LEFT:
        return Position(
            (pos.x - 1) % self.field_size,
            pos.y
        )