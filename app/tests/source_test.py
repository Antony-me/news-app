import unittest
from app.models import Sources


class SourcesTest(unittest.TestCase):
    
    def setUp(self):
        self.sources = Sources('bbc_news','BBC_news','The world Today, Is a continuesly changing, New technology is taking over,Catch all of this here at BBCNews.com.','https://bbcnews.com','general','en','us')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_sources,Sources))
        
        
if __name__ == '__main__':
    unittest.main() 