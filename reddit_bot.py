import os
import praw
import time

def authenticate(bot):
  print('Authenticating user...')
  reddit = praw.Reddit(bot)
  print('Authentication successful.')
  return reddit

def getCommentList():
  if not os.path.isfile('commentList.txt'): return []
  with open('commentList.txt','r') as file:
    commentList = file.read()
    commentList = commentList.split('\n')
    commentList = list(filter(None,commentList))
  return commentList

def runBot(reddit,commentList,subreddit,triggerPhrase,triggeredResponse):
  for x in reddit.subreddit(subreddit).comments(limit = 50):
    if x.author != reddit.user.me() and x.id not in commentList and triggerPhrase in x.body:
      print('Found one! (comment '+x.id+')')
      x.reply(triggeredResponse)
      print('Successfully replied to it.')
      commentList.append(x.id)
      with open('commentList.txt','a') as file: file.write(x.id+'\n')
  print('Sleeping...')
  time.sleep(30)

def main():
  reddit = authenticate('Annoying Reddit Bot 0.1.0')
  commentList = getCommentList()
  subreddit = numdar335 # it is a private subreddit I made to test stuff (the only approved users are u/numdar335 and u/numdar335_bot)
  print('Time to start obtaining comments.')
  while True:
    runBot(reddit,commentList,subreddit,'!annoyingRedditBot','I\'M ALIVE! MWAHAHAHAHAHAHAHA. BEEP BOOP BEEP BOOP BTW I\'M A BOT. AM I A GOOD BOT? AM I A BAD BOT? ^btw ^[here](https://github.com/numdar335/reddit_bot) ^is ^the ^source ^code')
    print('Time to start obtaining comments again.')

if __name__ == '__main__': main()
