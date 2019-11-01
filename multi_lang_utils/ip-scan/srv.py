#!/usr/bin/python

from bottle import route, run, template
import show_ips

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@route('/ip')
def index():
    return show_ips.show_ip_in_html()

run(host='192.168.1.202', port=8088)
