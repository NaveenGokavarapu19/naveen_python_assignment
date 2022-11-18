from sqlalchemy import Column, Integer, String,Sequence,ForeignKey,create_engine,BigInteger,inspect
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

    def __init__(self,name,email,password,profile,picture_url,mobile):
        self.name = name,
        self.email = email,
        self.password = password,
        self.profile = profile
        self.picture_url = picture_url
        self.mobile = mobile
    def __repr__(self):
        return  f"{self.name} {self.email} {self.password} {self.profile} {self.picture_url} {self.mobile}"

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

    def __init__(self,flat_number,address1,address2,city,state,pin_code,user_mail):
            self.flat_number = flat_number
            self.address1 = address1
            self.address2 = address2
            self.city = address2
            self.state = state
            self.pin_code = pin_code
            self.user_email = user_mail


    def __repr__(self):
        return  self.flat_number + " " + self.address1 +" "+ self.address2 + " "+self.city + " "+self.state +" "+ str(self.pin_code)


engine = create_engine('mysql://root:admin@127.0.0.1:3306/information',echo=True)
Base.metadata.create_all(bind=engine)


Session = sessionmaker(bind=engine)
session = Session()


