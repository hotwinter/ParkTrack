from models import Park, NumCar
from database import db_session
from sqlalchemy import desc, and_

def update_slot(uid, status): 
    park = Park.query.filter(Park.uid == uid).first()
    if park:
        park.status = status

def insert(rid, cid, uid):
    park = Park.query.filter(and_(Park.rid == rid, Park.cid == cid)).first()
    if park:
        park.uid = uid
    else:
        db_session.add(Park(rid, cid, uid))
    db_session.commit()

def delete(rid, cid):
    park = Park.query.filter(and_(Park.rid == rid, Park.cid == cid)).first()
    db_session.delete(park)
    db_session.commit()

def update_uid(rid, cid, uid):
    park = Park.query.filter(and_(Park.rid == rid, Park.cid == cid)).first()
    if park:
        park.uid = uid
    db_session.commit()

def get_all_entry():
    return Park.query.all() 

def insert_summary(out_num, in_num):
    db_session.add(NumCar(out_num, in_num))
    db_session.commit()

def get_num():
    result = NumCar.query.order_by(desc('id')).first()
    if result:
        return {"out": result.out_num, "in": result.in_num, "num":result.in_num-result.out_num}
    else:
        return {"out": 0, "in": 0, "num": 0}
