class User:
    def __init__(self, email, user_name, password, job_title):
        self.email = email
        self.name = user_name
        self.password = password
        self.job_title = job_title

    def change_password(self, new_password):
        self.password = new_password

    def change_job_title(self, new_job_title):
        self.job_title = new_job_title

    def get_user_info(self):
        print(f"User {self.name} currently work as a {self.job_title} and you can contact them at {self.email}")


app_user_1 = User("mohibzahid97@gmail.com", "Mohib Shaikh", "90188d06", "Cloud Intern")
app_user_1.get_user_info()
app_user_2 = User("zahidhussain63@gmail.com", "Zahid Shaikh", "90188d06", "HR Analyst")
app_user_2.get_user_info()

