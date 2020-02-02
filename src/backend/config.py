#!/usr/bin/python
# -*- coding: utf-8 -*-


import os



path, filename = os.path.split(os.path.abspath(__file__))


LOG = {}

LOG["log_file"] = {
	"type" : "str", 
	"values": [],
	"default" : path+"/app.log"
	}

LOG["log_level"] = {
	"type" : "str", 
	"values" : ["CRITICAL","ERROR","WARNING","INFO","DEBUG","NOTSET"],
	"default" : "DEBUG"
	}



SERVER = {}

SERVER["domain"] = {
	"type" : "str", 
	"values": [],	
	"default" : "nuraykaya.com"
	}

SERVER["server_name"] = {
	"type" : "str",
	"values": [],	 
	"default" : "server"
	}


SERVER["path"] = {
	"type" : "str", 
	"values": [],	
	"default" : path
	}

SERVER["db_ip"] = {
	"type" : "str", 
	"values": [],
	"default" : "127.0.0.1"
	}

SERVER["db_username"] = {
	"type" : "str", 
	"values": [],
	"default" : ""
	}

SERVER["db_password"] = {
	"type" : "str", 
	"values": [],
	"default" : ""
	}

SERVER["db_port"] = {
	"type" : "int", 
	"values": [],
	"range" : [],	
	"default" : 27017
	}

SERVER["outgoing_path"] = {
	"type" : "str", 
	"values": [],	
	"default" : path+"/outgoing"
	}

SERVER["template_path"] = {
	"type" : "str", 
	"values": [],	
	"default" : path+"/template"
	}

SERVER["heap_path"] = {
	"type" : "str", 
	"values": [],	
	"default" : path+"/heap"
	}

SERVER["maintenance"] = {
	"type" : "str", 
	"values" : ["yes", "no"],
	"default" : "no"
	}

SERVER["pass_key"] = {
	"type" : "str", 
	"values" : [],
	"default" : ""
	}

SERVER["cookie_key"] = {
	"type" : "str", 
	"values" : [],
	"default" : ""
	}