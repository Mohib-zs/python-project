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




