# from twitter import Twitter
import json
import twitter

from credentials import Credentials

CRED_FILE_NAME = "dontpush.json"


def gather_credentials(cred_file):
  try:
    cred_file = open(CRED_FILE_NAME, 'r')
  except FileNotFoundError:
    print("No credential json file")
    exit(1)

  json_creds = json.load(cred_file)

  return Credentials(
    json_creds["consumer_key"],
    json_creds["consumer_secret"],
    json_creds["access_token"],
    json_creds["access_token_secret"]
  )


def setup_api(credentials):
  return twitter.Api(consumer_key=credentials.consumer_key,
                     consumer_secret=credentials.consumer_secret,
                     access_token_key=credentials.access_token,
                     access_token_secret=credentials.access_token_secret)


def main():
  credentials = gather_credentials(CRED_FILE_NAME)
  api = setup_api(credentials)
  followers = api.GetFriends()
  for follower in followers:
    print(follower.screen_name + ", " + follower.name)
  print("Total:", len(followers))


if __name__ == '__main__':
  main()
