from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import credentials

class Listener(StreamListener):
	def on_data(self, data):
		print(data)
		return True
	def on_error(self, data):
		print(status)

if __name__ == "__main__":
	listener = Listener()
	auth = OAuthHandler(credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET)
	auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)

	stream = Stream(auth, listener)

	stream.filter(track=["WHM","WHM2021","IWD","IWD2021"])
	
