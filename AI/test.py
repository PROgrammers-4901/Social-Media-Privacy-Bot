import unittest

from predict import predict_text
from get_tweet import getTweet, getUser, getHashtag

class test_test_Test(unittest.TestCase):

    def test_predict(self):
        """in this test we are determining that the predictions are consistent and returning expected results"""
        tweet_text = [['Everyone who turns on my notis will get a follow back no cap 😤🙏 #Fortnite #Fortniteleaks #FixFortnite #FortniteArt #FortniteSeason6 #FortnitePrimal #FortniteNews #fortnitecommunity #follow #followme #fortnitegfx']]
        tweet_id = ['1381942812086796288']
        self.assertEqual("""{"tweet": "1381942812086796288", "prediction": "1", "probability": 0.788406195966992}""", str(predict_text(tweet_text, tweet_id)))

    def test_empty(self):
        """in this test we are determining that when inputted with no text, error handling is correct"""
        tweet_text = [[]]
        tweet_id = ['1381942812086796288']
        self.assertEqual("""None""", str(predict_text(tweet_text, tweet_id)))

    def test_empty_tweet(self):
        """in this test we are determining that when inputted with no tweet, error handling is correct"""
        tweet = ""
        self.assertEqual("""None""", str(getTweet(tweet)))

    def test_empty_hash(self):
        """in this test we are determining that when inputted with no hashtag, error handling is correct"""
        tag = ""
        self.assertEqual("""None""", str(getHashtag(tag)))

    def test_empty_user(self):
        """in this test we are determining that when inputted with no username, error handling is correct"""
        user = ""
        self.assertEqual("""None""", str(getUser(user)))

if __name__ == '__main__':
    unittest.main()