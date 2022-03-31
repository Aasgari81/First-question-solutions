class User:

    user_count = 0
    
    def __init__ (self, username):
        self.username = username
        User.user_count += 1


user1 = User("alnsdns")
user2 = User("slvnsoibnwo")
user3 = User("rdsbnoreib")
user4 = User("sdvowhgpiwghnp")
print(User.user_count)
print(user4.username)