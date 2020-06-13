import tweepy
import credential

auth = tweepy.OAuthHandler(credential.CONSUMER_API_KEY,credential.CONSUMER_API_SECRET_KEY)
auth.set_access_token(credential.ACCESS_TOKEN,credential.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

# try:
#     api.verify_credentials()
#     print("authentication success!")
# except:
#     print("error in authentication")

# user = api.get_user("RaulSilv3r")
# print("User details:")
# print(user.name)
# print(user.description)
# print(user.location)
# print()

# c = 1
# print("Last 20 Followers:")
# for follower in user.followers():
#     print(f"[{c}] {follower.name}")
#     c+=1

# uploading media

img = 'images\\erza_op.jpg'
msg = "Feeling nice #erza"
api.update_with_media(img,status=msg)

