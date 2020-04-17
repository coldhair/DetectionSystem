from operator import attrgetter


class User:
    def __init__(self,user_id):
        self.user_id=user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)

def sort_notcompare():
    users=[User(23),User(2),User(8),User(45)]
    print(users)
    print(sorted(users,key=lambda u:u.user_id))

if __name__ == '__main__':
    sort_notcompare()
    # 也可以使用attrgetter函数替代lambda
    users = [User(23), User(2), User(8), User(45)]
    print(sorted(users,key=attrgetter('user_id')))