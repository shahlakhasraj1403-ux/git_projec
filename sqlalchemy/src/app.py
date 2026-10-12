from sqlalchemy import create_engine, Column, INTEGER, String, Float 
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///digishop.db')
engine.connect()

Base = declarative_base()

class User(Base):
    __tablename__ = 'userInfo'

    id = Column(INTEGER, primary_key= True)
    name = Column(String)
    address= Column(String)
    # score = Column(Float)

Base.metadata.create_all(engine)

class Product(Base):
    __tablename__ = 'productInfo'

    id = Column(INTEGER, primary_key= True)
    name = Column(String)
    price = Column(String)
    description = (Float)
    
Base.metadata.create_all(engine)

session = sessionmaker(bind=engine)
sessionLocal = session()
###########################################################################
# user1 = User(name = 'Ali', address= 'Ahwaz', score= 4.9)
# user2 = User(name = 'Morteza', address= 'Tehran', score= 4.95)

# sessionLocal.add(user1)
# sessionLocal.add(user2)
# sessionLocal.commit()

# user3 = User(name = 'AliReza', address= 'Ahwaz', score= 4.9)
# user4 = User(name = 'Nima', address= 'Isfahan', score= 4.95)
# sessionLocal.add_all([user3,user4])
# sessionLocal.commit()

Users = sessionLocal.query(User).all()
print(Users)
for item in Users :
    print('name:', item.name)
    print('add:',item.address)
    # print('score:',item.score)

# product1 = Product(name="earphone", price=2000.0, description="not")
# product2 = Product(name="phone", price=9000.0, description="best")
# product3 = Product(name="airpods", price=1000.0, description="not")
# product4 = Product(name="charger cable", price=2000.0, description="not")

# sessionLocal.add(product1)
# sessionLocal.add(product2)
# sessionLocal.add(product3)
# sessionLocal.add(product4)

# sessionLocal.commit()


# products = sessionLocal.query(Product).all()
# for item in products:
#     print("name: ", item.name)
#     print("price: ", item.price)
#     print("description: ", item.description)
###############################################
# temp_user = sessionLocal.query(User).filter_by(address='Ahwaz', name= 'Ali').all()
# print(temp_user[-1].name)
# print(temp_user[-1].address)
###########################################################################################
# temp_user = sessionLocal.query(Product).filter(Product.price > 1000).all()
# print(temp_user)
# for item in temp_user:
#     print(item.name)
#     print(item.price)

# temp_user = sessionLocal.query(User).filter(User.name.like('%Ali')).all()
# print(temp_user)
# for item in temp_user:
#     print(item.name)
#     print(item.address)

# temp_user = sessionLocal.query(Product).filter(Product.price > 1000).all()
# print(temp_user)
# for item in temp_user:
#     print(item.name)
#     print(item.price)

# temp_user = sessionLocal.query(Product).filter(Product.name.like('%phone')).all()
# print(temp_user)
# for item in temp_user:
#     print(item.name)
#     print(item.price)

# User = sessionLocal.query(User).filter_by(id=1).first()

# User.name = 'Saeed'
# User.address = 'Tbriz'
# sessionLocal.commit()
# ##############################################################
# if User !=None:
#     sessionLocal.delete(User)
#     sessionLocal.commit()


temp_user = sessionLocal.query(Product).filter(Product.price > 1000).first()
if temp_user !=None:
    sessionLocal.delete(temp_user)
    sessionLocal.commit()
