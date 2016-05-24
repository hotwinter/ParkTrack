from sqlalchemy import Column, Integer, String, UniqueConstraint, Boolean, DateTime
from database import Base 
import datetime

class Park(Base):
    __tablename__ = 'park'
    id = Column(Integer, primary_key=True)
    rid = Column(Integer)
    cid = Column(Integer)
    uid = Column(String(120), unique=True)
    status = Column(Boolean)

    def __init__(self, rid, cid, uid):
        self.rid = rid
        self.cid = cid
        self.uid = uid
        self.status = False

    def __repr__(self):
        return '<Row %d, Column %d, Uid %s>' % (self.rid, self.cid, self.uid)

class NumCar(Base):
    __tablename__ = 'numcar'
    id = Column(Integer, primary_key=True)
    out_num = Column(Integer)
    in_num = Column(Integer) 
    time = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, out_num, in_num):
        self.out_num = out_num
        self.in_num = in_num

    def __repr__(self): 
        return '<Out_num %d, In_num %d>'
