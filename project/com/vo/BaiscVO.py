from project import db


class BasicVO(db.Model):
    __tablename__ = 'baiscmaster'
    UserId = db.Column('userId', db.Integer, primary_key=True, autoincrement=True)
    UserName = db.Column('userName', db.String(100), nullable=False, unique=True)
    UserSalary = db.Column('userSalary', db.String(100), nullable=False)
    UserRoom = db.Column('userRoom', db.Integer, nullable=False)
    UserMobile = db.Column('userMobile', db.Integer, nullable=False)
    UserPicture = db.Column('userPicture', db.String(100), nullable=False)
    UserKeywords = db.Column('userKeywords', db.String(100), nullable=False)

    def as_dict(self):
        return {
            'userId': self.userId,
            'userName': self.userName,
            'userSalary': self.userSalary,
            'userRoom': self.userRoom,
            'userMobile': self.userMobile,
            'userPicture':self.userPicture,
            'userKeywords':self.userKeywords
        }


db.create_all()
