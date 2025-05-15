import unittest
from memory import Memory
class TestMemoryFunctions(unittest.TestCase):
    def test_memory_add_subtract(self):
        mem = Memory()
        mem.add(10)
        self.assertEqual(mem.recall(), 10)
        mem.subtract(3)
        self.assertEqual(mem.recall(), 7)
        mem.clear()
        self.assertEqual(mem.recall(), "No History")
