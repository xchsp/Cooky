from app import db
from .model import UserModel
from app.helpers.BaseDao import BaseDao
from app.helpers.SQLMapper import SQLMapper
from app.helpers.exceptions import NotFoundException

class UserDao(BaseDao):

  def __init__(self):
    self.mapper = SQLMapper('User', UserModel)

  def getAll(self):
    query = 'SELECT * FROM User'
    results = db.select(query)
    return self.mapper.from_tuples(results)

  def getById(self, id):
    if not id:
      raise Exception("Id cannot be None")

    query = 'SELECT * FROM User WHERE id = %(id)s'
    result = db.select(query, { 'id': id }, 1)
    if result:
      return self.mapper.from_tuple(result)
    else:
      raise NotFoundException(str.format("No user found with id '%d'", id))

  def getByUsername(self, username):
    query = 'SELECT * FROM User WHERE username = %(username)s'
    result = db.select(query, {'username': username}, 1)
    if result:
      return self.mapper.from_tuple(result)
    else:
      raise NotFoundException(str.format("No user found with username '%s'", username))


  def save(self, userModel):
    if not isinstance(userModel, UserModel):
      raise ValueError("userModel should be of type UserModel")
    query = 'INSERT INTO User (id, username) VALUES (%s, %s)'
    userId = db.insert(query, self.mapper.to_tuple(userModel))
      
    if userId:
      return self.getById(userId)
    else:
      raise Exception("Could not save user")
