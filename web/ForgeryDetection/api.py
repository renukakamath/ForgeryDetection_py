from flask import *
from database import *
import uuid


api=Blueprint('api',__name__)


@api.route('/login',methods=['get','post'])
def login():
    data={}
    uname=request.args['username']
    pwd=request.args['password']
    q="SELECT * FROM `login` WHERE `username`='%s' AND `password`='%s'"%(uname,pwd)
    res=select(q)
    if res:
        data['data']=res
        data['status']='success'
    else:
        data['status']='failed'
    return str(data)

@api.route('/user_registration',methods=['get','post'])
def user_registration():
	
    data={}
    fn=request.form['fname']
    ln=request.form['lname']
    pl=request.form['place']
    img=request.files['image']
    path='static/'+str(uuid.uuid4())+img.filename
    img.save(path)

    ph=request.form['phone']
    em=request.form['email']

    uname=request.form['uname']
    psw=request.form['psw']

    q="select * from login where username='%s' and password='%s'"%(uname,psw)
    res=select(q)
    if res:
        flash('THIS USER IS ALREADY EXIST')
    else:
        q="insert into login values(NULL,'%s','%s','user')"%(uname,psw)
        lid=insert(q)
        q="insert into user values(NULL,'%s','%s','%s','%s','%s','%s','%s')"%(lid,fn,ln,pl,ph,em,path)
        insert(q)
        flash("Registration Completed.....!")
        data['status']='success'
    return str(data)


@api.route('/userreq',methods=['get','post'])
def userreq():
    data={}
    uid=request.args['lid']
    q="select * from passportrequest where user_id=(select user_id from user where login_id='%s') and (status='pending' or status='Accepted')"%(uid)
    res=select(q)
    print(res)
    if res:
        data['status']='already'
        data['method']='userreq'
    else:
        q="insert into passportrequest values(null,(select user_id from user where login_id='%s'),'0',curdate(),'pending','')"%(uid)
        insert(q)
        data['status']='success'	
        data['method']='userreq'	
    return str(data)

@api.route('/viewreq')
def viewreq():
    data={}
    lid=request.args['lid']
    q="select * from passportrequest where user_id=(select user_id from user where login_id='%s')"%(lid)
    res=select(q)
    print(res)
    data['status']=res[0]['status']
 
    data['method']='viewreq'
    return str(data)


@api.route('/viewcomplaints')
def viewcomplaints():
    data={}
    lid=request.args['lid']
    q="select * from complaints where user_id=(select user_id from user where login_id='%s')"%(lid)
    res=select(q)
    data['data']=res
    data['status']='success'	
    data['method']='viewcomplaints'
    return str(data)

@api.route('/usercomplaints',methods=['get','post'])
def usercomplaints():
    data={}
    uid=request.args['lid']
    comp=request.args['complaint']


    q="insert into complaints values(null,(select user_id from user where login_id='%s'),'%s','pending',curdate())"%(uid,comp)
    insert(q)
    data['status']='success'	
    data['method']='usercomplaints'	
    return str(data)




@api.route('/viewenq')
def viewenq():
    data={}
    lid=request.args['lid']
    q="select * from enquiry where user_id=(select user_id from user where login_id='%s')"%(lid)
    res=select(q)
    data['data']=res
    data['status']='success'	
    data['method']='viewenq'
    return str(data)

@api.route('/userenq',methods=['get','post'])
def userenq():
    data={}
    uid=request.args['lid']
    comp=request.args['enq']


    q="insert into enquiry values(null,(select user_id from user where login_id='%s'),'%s','pending',curdate())"%(uid,comp)
    insert(q)
    data['status']='success'	
    data['method']='userenq'	
    return str(data)

@api.route('/travelhistory')
def travelhistory():
    data={}
    lid=request.args['lid']
    q="select * from history where user_id=(select user_id from user where login_id='%s')"%(lid)
    res=select(q)
    data['data']=res
    data['status']='success'	
   
    return str(data)


@api.route('/viewpassport')
def viewpassport():
    data={}
    pid=request.args['pid']
    q="select * from passportrequest where prequest_id='%s'"%(pid)
    res=select(q)
    data['pno']=res[0]['passport_num']
    data['status']='success'	
   
    return str(data)
