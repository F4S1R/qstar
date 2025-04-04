# tests/test_pipeline.py
import unittest
from qstar.core import QStarPipeline

class TestQStarPipeline(unittest.TestCase):

    def test_numeric_input(self):
        pipeline = QStarPipeline()
        result = pipeline.run(10)
        self.assertIsInstance(result, (int, float))

    def test_string_input(self):
        pipeline = QStarPipeline()
        result = pipeline.run("test")
        self.assertIsInstance(result, str)

    def test_pipeline_logs(self):
        pipeline = QStarPipeline()
        pipeline.run(5)
        logs = pipeline.get_logs()
        self.assertTrue(any("Initial" in log for log in logs))

if __name__ == '__main__':
    unittest.main()