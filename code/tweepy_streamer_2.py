from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import credentials


class TwitterStreamer():
	"""
	Stream and process live tweets
	"""
	def stream_tweets(self, fetched_tweets_filename, hashtag_list):
		#handles twitter auth and connection to streaming API
		listener = Listener(fetched_tweets_filename)
		auth = OAuthHandler(credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET)
		auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)

		stream = Stream(auth, listener)

		stream.filter(track=hashtag_list)
		return True

	def on_error(self, data):
		print(status)

class Listener(StreamListener):
	"""
	Basic Listener which prints received tweets to terminal
	"""
	def __init__(self, fetched_tweets_filename):
		self.fetched_tweets_filename = fetched_tweets_filename
	def on_data(self, data):
		print(data)
		with open(self.fetched_tweets_filename, 'w') as file:
			file.write(data)
		return True
	def on_error(self, data):
		print(status)

if __name__ == "__main__":
	hashtag_list = ["IWD","IWD2021","WHM","WHM2021", "PowerfulWoman"]
	fetched_tweets_filename = "tweets.json"
	twitter_streamer = TwitterStreamer()
	twitter_streamer.stream_tweets(fetched_tweets_filename, hashtag_list)