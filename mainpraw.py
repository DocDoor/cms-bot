import praw
from praw.reddit import Subreddit

reddit = praw.Reddit(
    client_id="my client id",
    client_secret="my client secret",
    user_agent="my user agent",
)

subreddit = reddit.subreddit("CryptoMoonShots")

for post in subreddit.hot(limit=100): # what ever you want
  # print(post.selftext) -> self text
  # print(post.url) -> url
  # print(post.score) -> number of upvote
  cnt = 0
  for i in range(0, len(post.selftext)-10):
    if cnt:
      break
    if post.selftext[i]=='t' and post.selftext[i+1]=='.' and post.selftext[i+2]=='m':
      for j in range(i+3, min(i+30, len(post.selftext))):
        if post.selftext[j]==')' or post.selftext[j]==']' or post.selftext[j]==' ':
          print(post.selftext[i:j-1])
          cnt = 1
          break
