from constants import *
import tweepy as tw

auth = tw.OAuthHandler(API_KEY, API_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tw.API(auth)

tweet = api.update_status("Esse Sofrimento do Caralho ano que vem é o Vasco")
