import unittest

from predict import predict_text

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



if __name__ == '__main__':
    unittest.main()