import unittest
from src.day2.dive import Dive

DIVE_INSTRUCTION = [['forward', 5], ['down', 5], ['forward', 8], ['up', 3], ['down', 8], ['forward', 2]]

class TestDive(unittest.TestCase):
   def should_return_horizontal_position_after_dive(self):
      horizontal_position = Dive.get_horizontal_position(DIVE_INSTRUCTION)
      self.assertEqual(horizontal_position, 15)
    

   def should_return_final_depth_after_dive(self):
      final_depth = Dive.get_final_depth(DIVE_INSTRUCTION)
      self.assertEqual(final_depth, 10)


if __name__ == '__main__':
   unittest.main()