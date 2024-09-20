from user import User
from post import Post


app_user_1 = User("mohibzahid97@gmail.com", "Mohib Shaikh", "90188d06", "Cloud Intern")
app_user_1.get_user_info()

app_user_2 = User("zahidhussain63@gmail.com", "Zahid Shaikh", "90188d06", "HR Analyst")
app_user_2.get_user_info()

new_post = Post("On a journey", app_user_2.name)
new_post.get_post_info()