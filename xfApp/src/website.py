#!/usr/bin/python
from flask import request

from xfApp.server import proflask
from xfApp.xfMysql.createEngine import session
from xfApp.xfMysql.website import Website
import json

@proflask.route("/save/website", methods=["POST"])
def saveWebsite():
    data = request.get_data()
    print('data::',data)
    json_data = json.loads(data.decode('utf-8'))
    print('json_data:',json_data)
    name = json_data.get('name')
    url = json_data.get('url')
    print('name::',name)
    print('url::', url)

    new_web = Website()
    new_web.name = name
    new_web.url = url
    session.add(new_web)
    session.commit()
    session.close()

    return '保存成功'

@proflask.route("/website/list", methods=["GET", "HEAD"])
def getWebsiteList():
    web_list = session.query(Website).all()
    webs = []
    for item in web_list:
        webs.append({"id":item.id,"name":item.name,'url':item.url})
    web_list_json = json.dumps(webs)
    return web_list_json


