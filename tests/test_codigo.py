import unittest
import codigo
import os


class CodigoTest(unittest.TestCase):
    def test_adjust_creation_datetime_from_pictures_in_dir(self):

        current_directory = os.getcwd()
        codigo.adjust_creation_datetime_from_pictures_in_dir(current_directory)

        self.assertEqual(True, True)  # add assertion here


