from sqlalchemy import Column, Integer, String,Sequence,ForeignKey,create_engine,BigInteger
from sqlalchemy.orm import sessionmaker,declarative_base,relationship


Base = declarative_base()
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    name = Column(String(50))
    email =  Column(String(50),unique=True) 
    password =  Column(String(50)) 
    profile = Column(String(50))
    picture_url = Column(String(50))
    mobile = Column(BigInteger,unique=True)
    child = relationship("Address", back_populates="parent",uselist=False)

    def __repr__(self):
        return str("name=" + self.name + "email=" + self.email + "password=" + self.password + "profile=" +self.profile + "picture_url=" +self.picture_url + "mobile =" + self.mobile)

class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, Sequence("address_id_seq"), primary_key=True)
    flat_number = Column(String(50))
    address1 =  Column(String(50)) 
    address2 =  Column(String(50)) 
    city = Column(String(50))
    state = Column(String(50))
    pin_code = Column(BigInteger)
    user_mail = Column(String(50), ForeignKey("users.email"))
    parent = relationship("User", back_populates="child")


    def __repr__(self):
        return "<Address(flat_number = '%s',address1='%s',address2='%s',city='%s',state='%s',pin_code='%d',user_mail='%s')>" %(
            self.flat_number,
            self.address1,
            self.address2,
            self.city,
            self.state,
            self.pin_code,
            self.user_email
        )


engine = create_engine('mysql://root:admin@127.0.0.1:3306/information',echo=True)
Base.metadata.create_all(bind=engine)


Session = sessionmaker(bind=engine)
session = Session()


