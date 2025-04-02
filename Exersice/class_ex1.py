class Comment:
    def __init__(self, username, content, likes=0 ):
        self.username = username
        self.content = content
        self.likes = likes



comment = Comment("user 1", "I like this book", )

print(comment.username)
print(comment.content)
comment.likes += 100 #модификация на параметър
print(comment.likes)
