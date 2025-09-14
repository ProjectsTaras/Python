#testów jednostkowych korzystamy pakiet unittest
'''Polega on na pisaniu funkcji, które sprawdzają, czy napisany przez nas kod jest poprawny.
W testach zazwyczaj najpierw przedstawiamy, jaki jest stan początkowy, następnie jaka akcja
została wykonana, a ostatecznie badamy, czy nastąpiła spodziewana zmiana stanu. Dla przykładu,
stanem początkowym może być wąż w określonym miejscu i poruszający się w określonym kierunku,
akcją wywołanie funkcji step, a sprawdzeniem zbadanie, czy nowa pozycja węża jest poprawna.'''

# import unittest


# class GameStateTest(unittest.TestCase):

#     def test_example(self):
#         self.assertEqual('foo'.upper(), 'FOO')

# terminal python -m unittest game_state_test.py

import unittest
from game_state import GameState
from position import Position
from direction import Direction


class GameStateTest(unittest.TestCase):

    def test_snake_should_move_right(self):
        state = GameState(
            snake=[
                Position(1, 2),
                Position(1, 3),
                Position(1, 4)
            ],
            direction=Direction.RIGHT,
            food=Position(10, 10),
            field_size=20
        )

        state.step()

        expected_state = [
            Position(1, 3),
            Position(1, 4),
            Position(2, 4)
        ]
        self.assertEqual(expected_state, state.snake)

    def test_snake_should_move_left(self):
        state = GameState(
            snake=[
                Position(1, 2),
                Position(1, 3),
                Position(1, 4)
            ],
            direction=Direction.LEFT,
            food=Position(10, 10),
            field_size=20
        )

        state.step()

        expected_state = [
            Position(1, 3),
            Position(1, 4),
            Position(0, 4)
        ]
        self.assertEqual(expected_state, state.snake)

        #.......................

#Wyjechanie poza planszę, Następnie sprawdźmy, czy jego głowa jest już po drugiej stronie.
    def test_snake_should_move_up_on_top(self):
        state = GameState(
            snake=[
                Position(2, 2),
                Position(2, 1),
                Position(2, 0)
            ],
            direction=Direction.UP,
            food=Position(10, 10),
            field_size=20
        )

        state.step()

        expected_state = [
            Position(2, 1),
            Position(2, 0),
            Position(2, 19)
        ]
        self.assertEqual(expected_state, state.snake)


    def test_snake_should_move_right_on_edge(self):
        state = GameState(
            snake=[
                Position(17, 1),
                Position(18, 1),
                Position(19, 1)
            ],
            direction=Direction.RIGHT,
            food=Position(10, 10),
            field_size=20
        )

        state.step()

        expected_state = [
            Position(18, 1),
            Position(19, 1),
            Position(0, 1)
        ]
        self.assertEqual(expected_state, state.snake)