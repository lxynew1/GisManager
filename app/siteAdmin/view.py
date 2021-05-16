from . import siteAdmin
from flask import Flask,request
import requests
import urllib.request, urllib.parse, urllib.error
import http.client
import json
from .serviceOperator import run


@siteAdmin.route('/')
def restartServer():
    # print((serviceEdit()))
    return '<h1>This is index page</h1>'


@siteAdmin.route('/restart', methods=['POST'])
def restart():
    res = run()
    # res = {"status":"success"}
    return json.dumps(res, ensure_ascii=False, indent=4)


