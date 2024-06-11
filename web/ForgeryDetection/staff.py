from flask import *
from database import *
import uuid

staff=Blueprint('staff',__name__)

@staff.route('/staff_home')
def staff_home():
	return render_template('staff_home.html')


@staff.route('/staff_view_users')
def staff_view_users():
	data={}
	q="select * from user"
	res=select(q)
	data['user']=res
	return render_template('staff_view_users.html',data=data)



@staff.route('/staff_add_travel_history',methods=['get','post'])
def staff_add_travel_history():
	data={}
	uid=request.args['uid']
	if 'submit' in request.form:
		fp=request.form['fp'] 
		tp=request.form['tp']
		date=request.form['date']
		q="select * from passportrequest where user_id='%s'"%(uid)
		res=select(q)
		if res:
			q="insert into history values(null,'%s','%s','%s','%s',now())"%(uid,fp,tp,date)
			insert(q)
			flash("Added...!")
			return redirect(url_for('staff.staff_view_users'))
		else:
			flash("Check Your Passport Details........!")
			return redirect(url_for('staff.staff_view_users'))
	return render_template('staff_add_travel_history.html',data=data)


@staff.route('/staff_view_enquiry',methods=['get','post'])
def staff_view_enquiry():
	data={}
	q="SELECT *,CONCAT(`fname`,' ',`lname`) AS `name` FROM `enquiry` INNER JOIN `user` USING(`user_id`)"
	res=select(q)
	data['enquiry']=res

	j=0
	for i in range(1,len(res)+1):
		print('submit'+str(i))
		if 'submit'+str(i) in request.form:
			reply=request.form['reply'+str(i)]
			print(reply)
			print(j)
			print(res[j]['enquiry_id'])
			q="update enquiry set reply='%s' where enquiry_id='%s'" %(reply,res[j]['enquiry_id'])
			print(q)
			update(q)
			flash("success")
			return redirect(url_for('staff.staff_view_enquiry')) 	
		j=j+1
	return render_template('staff_view_enquiry.html',data=data)