from prawcore import NotFound

from mypackage import handler


class Post:
    def __init__(self, id, title, body, url, score, subreddit,number_of_comments):
        self.id = id
        self.title = title
        self.body = body
        self.url = url
        self.score = score
        self.subreddit = subreddit
        self.number_of_comments = number_of_comments


def sub_exists(request):
    exists = True
    try:
        handler.subreddits.search_by_name(request, exact=True)
    except NotFound:
        exists = False
    return exists


class Reddit():
    def call_posts(request):
        if sub_exists(request):
            posts = []
            subreddit = handler.subreddit(request)
            hot_python = subreddit.hot(limit=20)
            for post_from_request in hot_python:
                posts.append(
                    Post(
                        post_from_request,
                        post_from_request.title,
                        post_from_request.selftext,
                        post_from_request.url,
                        post_from_request.score,
                        "/"+str(post_from_request.subreddit),
                        post_from_request.num_comments
                    )
                )
            return posts
        else:
            return []

