#!/usr/local/bin/python


#############
# script to connect/link from docker python container 
# to a mongodb container
#############

import pymongo
import os

mon_host = os.environ['DB_PORT_27017_TCP_ADDR']
mon_port = int(os.environ['DB_PORT_27017_TCP_PORT'])

client = pymongo.MongoClient(mon_host, mon_port)
db = client.some_veg
fresh = db.fresh_veg #collection
frozen = db.frozen_veg #collection

vcolor = raw_input('color of veg: ')
vtype = raw_input('type of veg: ')
vname = raw_input('name of veg: ')
vcountry = raw_input('country of origin: ')

the_veg = {"color":vcolor, "type":vtype, "name":vname, "country":vcountry}

fresh_id = fresh.insert(the_veg)
for veg in fresh.find():
  print veg


#print client.database_names()
#print client.server_info()


