from public import *
import qrcode
import random
import uuid

import string


import json
from web3 import Web3, HTTPProvider

# truffle development blockchain address
blockchain_address = 'http://127.0.0.1:9545'
# Client instance to interact with the blockchain
web3 = Web3(HTTPProvider(blockchain_address))
# Set the default account (so we don't need to set the "from" for every transaction call)
web3.eth.defaultAccount = web3.eth.accounts[0]
compiled_contract_path = 'C:/Users/renuk/Downloads/Musilar/web/ForgeryDetection/node_modules/.bin/build/contracts/forgerydetection.json'
# compiled_contract_path = 'F:/NGO/node_modules/.bin/build/contracts/medicines.json'
# Deployed contract address (see `migrate` command output: `contract address`)
deployed_contract_address = '0xA7BBe41BCa5606342D92D6Da0E3db2CCb1aE1055'



def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))



admin=Blueprint('admin',__name__)

@admin.route('/admin_home')
def admin_home():
	return render_template('admin_home.html')



@admin.route('/admin_manage_staff',methods=['get','post'])
def admin_manage_staff():
	data={}
	if 'manage' in request.form:
		fn=request.form['fn']
		ln=request.form['ln']
		pl=request.form['pl']
		phone=request.form['ph']
		email=request.form['em']
		des=request.form['des']
		uname=request.form['uname']
		password=request.form['pass']
		q="select * from login where username='%s' and password='%s'"%(uname,password)
		res=select(q)
		if res:
			flash('THIS USERNAME AND PASSWORD IS ALREADY EXIST')
		else:
			q="insert into login values(NULL,'%s','%s','staff')"%(uname,password)
			lid=insert(q)
			q="insert into staff values(NULL,'%s','%s','%s','%s','%s','%s','%s')"%(lid,fn,ln,pl,phone,email,des)
			insert(q)
			flash("Registered Successfully...!")
		return redirect(url_for('admin.admin_manage_staff'))

	q="select * from staff"
	res=select(q)
	if res:
		data['office']=res
		print(res)

	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None

	if action=='delete':
		q="delete from staff where login_id='%s'"%(id)
		delete(q)
		q="delete from login where login_id='%s'"%(id)
		delete(q)
		flash("deleted.....!")
		return redirect(url_for('admin.admin_manage_staff'))

	if action=='update':
		q="select * from staff where login_id='%s'"%(id)
		data['dir']=select(q)

	if 'update' in request.form:
		fn=request.form['fn']
		ln=request.form['ln']
		pl=request.form['pl']
		phone=request.form['ph']
		email=request.form['em']
		des=request.form['des']
		q="update staff set fname='%s',lname='%s',phone='%s',place='%s',email='%s',designation='%s' where login_id='%s'"%(fn,ln,phone,pl,email,des,id)
		update(q)
		flash("updated")
		return redirect(url_for('admin.admin_manage_staff'))
	return render_template("admin_manage_staff.html",data=data)



@admin.route('/admin_manage_security_authority',methods=['get','post'])
def admin_manage_security_authority():
	data={}
	if 'manage' in request.form:
		fn=request.form['fn']
		ln=request.form['ln']
		pl=request.form['pl']
		phone=request.form['ph']
		email=request.form['em']
		des=request.form['des']
		uname=request.form['uname']
		password=request.form['pass']
		q="select * from login where username='%s' and password='%s'"%(uname,password)
		res=select(q)
		if res:
			flash('THIS USERNAME AND PASSWORD IS ALREADY EXIST')
		else:
			q="insert into login values(NULL,'%s','%s','security authority')"%(uname,password)
			lid=insert(q)
			q="insert into security_authority values(NULL,'%s','%s','%s','%s','%s','%s','%s')"%(lid,fn,ln,pl,phone,email,des)
			insert(q)
			flash("Registered Successfully...!")
		return redirect(url_for('admin.admin_manage_security_authority'))

	q="select * from security_authority"
	res=select(q)
	if res:
		data['office']=res
		print(res)

	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None

	if action=='delete':
		q="delete from security_authority where login_id='%s'"%(id)
		delete(q)
		q="delete from login where login_id='%s'"%(id)
		delete(q)
		flash("deleted.....!")
		return redirect(url_for('admin.admin_manage_security_authority'))

	if action=='update':
		q="select * from security_authority where login_id='%s'"%(id)
		data['dir']=select(q)

	if 'update' in request.form:
		fn=request.form['fn']
		ln=request.form['ln']
		pl=request.form['pl']
		phone=request.form['ph']
		email=request.form['em']
		des=request.form['des']
		q="update security_authority set fname='%s',lname='%s',phone='%s',place='%s',email='%s',designation='%s' where login_id='%s'"%(fn,ln,phone,pl,email,des,id)
		update(q)
		flash("updated")
		return redirect(url_for('admin.admin_manage_security_authority'))
	return render_template("admin_manage_security_authority.html",data=data)




@admin.route('/admin_view_complaints',methods=['get','post'])
def admin_view_complaints():
	data={}
	q="SELECT *,CONCAT(`fname`,' ',`lname`) AS `name` FROM `complaints` INNER JOIN `user` USING(`user_id`)"
	res=select(q)
	data['complaints']=res

	j=0
	for i in range(1,len(res)+1):
		print('submit'+str(i))
		if 'submit'+str(i) in request.form:
			reply=request.form['reply'+str(i)]
			print(reply)
			print(j)
			print(res[j]['complaint_id'])
			q="update complaints set reply='%s' where complaint_id='%s'" %(reply,res[j]['complaint_id'])
			print(q)
			update(q)
			flash("success")
			return redirect(url_for('admin.admin_view_complaints')) 	
		j=j+1
	return render_template('admin_view_complaints.html',data=data)



@admin.route('/admin_view_passport_request')
def admin_view_passport_request():
	data={}
	q="SELECT * FROM `passportrequest` INNER join user using(user_id)"
	res=select(q)
	data['request']=res

	n=id_generator(10, "6793YUIO")
	print(n)

	if 'action' in request.args:
		action=request.args['action']
		pid=request.args['pid']
		uid=request.args['uid']
	else:
		action=None

	if action=="accept":
		s=qrcode.make(str(pid))
		path="static/qrcode/"+str(uuid.uuid4())+".png"
		s.save(path)
		q="select * from crimes where user_id='%s'"%(uid)
		res=select(q)
		if res:
			flash("Your Application is Rejected....!")
			q="update passportrequest set status='Rejected' where prequest_id='%s'"%(pid)
			update(q)
			return redirect(url_for('admin.admin_view_passport_request'))
		else:
			q="update passportrequest set status='Accepted',qr='%s',passport_num='%s' where prequest_id='%s'"%(path,n,pid)
			update(q)
			import datetime
			d=datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
			with open(compiled_contract_path) as file:
				contract_json = json.load(file)  # load contract info as JSON
				contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
				contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
				id=web3.eth.get_block_number()
			message = contract.functions.acceptedrequest(id,int(pid),str(n),d,'Accepted').transact()
			flash("Your Application is Accepted....!")
			return redirect(url_for('admin.admin_view_passport_request'))

	return render_template('admin_view_passport_request.html',data=data)



@admin.route('/admin_view_criminal_activities')
def admin_view_criminal_activities():
	data={}
	cid=request.args['cid']
	q="select * from crimes where user_id='%s'"%(cid)
	res=select(q)
	data['crime']=res
	return render_template('admin_view_criminal_activities.html',data=data)



@admin.route('/admin_view_travel_history')
def admin_view_travel_history():
	data={}
	q="select * from history inner join user using(user_id)"
	res=select(q)
	data['his']=res
	return render_template('admin_view_travel_history.html',data=data)