import unittest
import capitalize

class TestCapital(unittest.TestCase):

	def test_one_word(self):
		text = 'singleword'
		result = capitalize.capitilize(text)
		self.assertEqual(result,'Singleword')

	def test_multiple_words(self):
		text = 'multiple words'
		result = capitalize.capitilize(text)
		self.assertEqual(result,'Multiple words')

if __name__ =='__main__':
	unittest.main()