from flask_app.database import db, ma

class User(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  username = db.Column(db.String(50), nullable=False)
  email = db.Column(db.String(100), nullable=False)
  password = db.Colum(db.string(100),nullable=False)

  def __repr__(self):
    return '<User %r>' % self.username

  def getUserList():

    # select * from users
    user_list = db.session.query(User).all()

    if user_list == None:
      return []
    else:
      return user_list

  def registUser(user):
    record = User(
      name = user['username'],
      mail = user['email'],
      password = user['password']
    )
   
    # insert into users(name, address, tel, mail) values(...)
    db.session.add(record)
    db.session.commit()

    return user

class UserSchema(ma.ModelSchema):
    class Meta:
      model = User
      fields = ('id', 'username', 'email', 'password')