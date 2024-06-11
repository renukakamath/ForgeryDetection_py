from public import *




user=Blueprint('user',__name__)

@user.route('/user_home')
def user_home():
	uid=session['u_id']
	if 'action' in request.args:
		action=request.args['action']
		print(action)
	else:
		action=None


	if action=="add":
		q="select * from passportrequest where user_id='%s' and (status='pending' or status='Accepted')"%(uid)
		res=select(q)
		print(res)
	
		if res:
			flash("Request Already Send")
			return redirect(url_for('user.user_home'))
		else:
			
			 q="insert into passportrequest values(null,'%s','0',curdate(),'pending','')"%(uid)
			 insert(q)
			 flash("Requested.....!")
			 return redirect(url_for('user.user_home'))
	return render_template('user_home.html')



@user.route('/user_send_complaints',methods=['get','post'])
def user_send_complaints():
	data={}
	uid=session['u_id']

	if 'submit' in request.form:
		
		complaint=request.form['Complaint']
		q="INSERT INTO `complaints`VALUES(null,'%s','%s','pending',NOW())"%(uid,complaint)
		insert(q)

		flash("success...")

		return redirect(url_for('user.user_send_complaints'))

	q="SELECT * FROM `complaints` WHERE `user_id`='%s'"%(uid)
	res=select(q)
	data['complaints']=res
	return render_template('user_send_complaints.html',data=data)



@user.route('/user_send_enquiry',methods=['get','post'])
def user_send_enquiry():
	data={}
	uid=session['u_id']

	if 'submit' in request.form:
		
		complaint=request.form['Complaint']
		q="INSERT INTO `enquiry`VALUES(null,'%s','%s','pending',NOW())"%(uid,complaint)
		insert(q)

		flash("success...")

		return redirect(url_for('user.user_send_enquiry'))

	q="SELECT * FROM `enquiry` WHERE `user_id`='%s'"%(uid)
	res=select(q)
	data['enquiry']=res
	return render_template('user_send_enquiry.html',data=data)




@user.route('/user_view_request',methods=['get','post'])
def user_view_request():
	data={}
	uid=session['u_id']
	q="SELECT * FROM `passportrequest` WHERE user_id='%s'"%(uid)
	res=select(q)
	data['request']=res
	return render_template('user_view_request.html',data=data)



@user.route('/user_view_travel_history',methods=['get','post'])
def user_view_travel_history():
	data={}
	uid=session['u_id']
	q="SELECT * FROM `history` WHERE user_id='%s'"%(uid)
	res=select(q)
	data['his']=res
	return render_template('user_view_travel_history.html',data=data)