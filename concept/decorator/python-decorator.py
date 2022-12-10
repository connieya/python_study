
class User:
    def __init__(self , name):
        self.name = name
        self.is_logged_in= False

def is_authenticated_decorator(function):
    def wrapper():
        function()
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog posts.")


new_user = User("cony")
create_blog_post(new_user)
