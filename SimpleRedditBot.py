# importing python reddit API wrapper
import praw

# creating instances of reddit, the subreddit to check, and which user to reply to
reddit = praw.Reddit('bot')
subreddit = reddit.subreddit(input("Please enter a subreddit r/"))
user = reddit.redditor(input("Please enter a user u/"))

# iterate through the submissions in the subreddit...
for submission in subreddit.hot(limit = 10):
    # cleaning MoreComment instances in the CommentForest
    submission.comments.replace_more(limit=100)
    # and then through each comment...
    for comment in submission.comments.list():
        # checking comments author against the user
        if comment.author == user:
            # reply
            comment.reply("Hi friend!")




