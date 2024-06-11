from flask import *
from database import *
import uuid



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




authority=Blueprint('authority',__name__)

@authority.route('/authority_home')
def authority_home():
	return render_template('authority_home.html')

@authority.route('/authority_view_user')
def authority_view_user():
	data={}
	q="select * from user inner join passportrequest using (user_id)"
	res=select(q)
	data['user']=res
	return render_template('authority_view_users.html',data=data)



@authority.route('/authority_add_criminal_activities',methods=['get','post'])
def authority_add_criminal_activities():
	data={}
	cid=request.args['cid']

	if 'submit' in request.form:
		cm=request.form['cm']
		det=request.form['det']
		q="insert into crimes values(NULL,'%s','%s','%s',curdate())"%(cid,cm,det)
		insert(q)
		flash("Crime Added.....!")
		return redirect(url_for('authority.authority_view_user'))
	return render_template('authority_add_criminal_activities.html',data=data)



@authority.route('/authority_view_passport_details',methods=['get','post'])
def authority_view_passport_details():
	data={}
	pid=request.args['pid']
	q="select * from passportrequest inner join user using (user_id) where prequest_id='%s'"%(pid)
	res1=select(q)
	if res1:
		pno=res1[0]['passport_num']
		print(pno)
	with open(compiled_contract_path) as file:
		contract_json = json.load(file)  # load contract info as JSON
		contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
	contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
	blocknumber = web3.eth.get_block_number()
	res = []
	try:
		for i in range(blocknumber, 0, -1):
			a = web3.eth.get_transaction_by_block(i, 0)
			decoded_input = contract.decode_function_input(a['input'])
			print(decoded_input)
			if str(decoded_input[0]) == "<Function acceptedrequest(uint256,uint256,string,string,string)>":
				# if int(decoded_input[1]['u_id']) == int(session['user_id']):
					res.append(decoded_input[1])

					
					if decoded_input[1]['passportnum']==pno:
						flash("verified")





	except Exception as e:
		print("", e)
	print(res)

	# q="select * from passportrequest inner join user using (user_id) where prequest_id='%s'"%(pid)
	# res=select(q)

	data['pass']=res1



	return render_template('authority_view_passport_details.html',data=data)



@authority.route('/authority_track_travel_history',methods=['get','post'])
def authority_track_travel_history():
	data={}
	cid=request.args['cid']
	q="select * from history inner join user using(user_id) where user_id='%s'"%(cid)
	res=select(q)
	data['his']=res
	return render_template('authority_track_travel_history.html',data=data)