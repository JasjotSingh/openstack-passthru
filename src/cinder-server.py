import os
import pdb
import socket
#pdb.set_trace()
from cinderclient import client
import json

#authurl = 'http://140.247.152.207:35357/v2.0'
#cinderurl= 'http://10.31.27.207:8776/v2/d5785e4393ba4db5871c34b6a6c3ef7b'
#ten = 'EC500-openstack-passthru'




def connect_cinder(): #########works
	con=client.Client('2', 'estherlu', '31415926', 'EC500-openstack-passthru', 'http://140.247.152.207:35357/v2.0')
	return con


from swiftclient import ClientException

def get_volumes(con,tenant):
	try:                              ###########needs modification
		vlist=con.volumes.list();
		return vlist;

              

#def Hash(something):
#	c_swift = str(container).split('-')
#	if c_swift[0] == 'MOC1':
#		#print 'in 1'
#		return preauthurl_MOC1
#	elif c_swift[0] == 'MOC2':
#		#print 'in 2'
#		return preauthurl_MOC2
#	else:
#		sm=0
#		for letters in container:
#			sm += ord(letters)
#		index = sm%Backends
#		if index == 0: 
#			#print 'in 1'
#			return preauthurl_MOC1
#		elif index == 1:
#			#print 'in 2'
#			return preauthurl_MOC2
			
##################################################################################################### flask:

from flask import Flask, request
app = Flask(__name__)



@app.route("/v2/​{tenant_id}​/volumes", methods=['GET', 'POST'])
def func2():
        if  request.method == 'GET':		
		con=connect_cinder()
		return get_volumes(con,tenant_id)
	elif request.method == "POST":
#		token=request.headers.get('X-Auth-Token');
#		url = Hash(container)
#		con=connect_cinder(token,url)
#		head = request.headers
#		headers = {}
#		for key in head:
#			headers[key[0]] = key[1]
#		
		return "Not yet"#update_containerMetaData(con,headers)
	
        else:
                return "No Such Function", 501




	




if __name__ == "__main__":
        app.run(None,5003,True)
