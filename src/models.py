from sqlalchemy import Column, Integer, String,Sequence,ForeignKey,create_engine,BigInteger
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
Base = declarative_base()
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    name = Column(String(50))
    email =  Column(String(50)) 
    password =  Column(String(50)) 
    profile = Column(String(50))
    picture_url = Column(String(50))
    mobile = Column(BigInteger)

    def __repr__(self):
        return "<User(name='%s', email='%s',password='%s',profile='%s',picture_url='%s',mobile='%d')>" %(
            self.name,
            self.email,
            self.password,
            self.profile,
            self.picture_url,
            self.mobile
        )

class Address(Base):
    __tablename__ = "users"
    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    flat_number = Column(String(50))
    address1 =  Column(String(50)) 
    address2 =  Column(String(50)) 
    city = Column(String(50))
    state = Column(String(50))
    pin_code = Column(BigInteger)

    def __repr__(self):
        return "<User(name='%s', flat_number = '%s',address1='%s',address2='%s',city='%s',state='%s',pin_code='%d')>" %(
            self.flat_number,
            self.address1,
            self.address2,
            self.city,
            self.state,
            self.pin_code
        )


engine = create_engine('mysql://root:admin@127.0.0.1:3306/information',echo=True)
Base.metadata.create_all(bind=engine)


Session = sessionmaker(bind=engine)
session = Session()


