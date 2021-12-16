class user:
    def __init__(self, user_id, username) -> None:
        self.id = user_id
        self.username = username
        self.followers = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = user("001", "taka")

print(user_1.followers)
