# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.conf.urls import url, include
from bs4 import BeautifulSoup
from sendgrid.helpers.mail import *
import sendgrid
import urllib2
import os

def send_email(live_price):
    sg = sendgrid.SendGridAPIClient(apikey=process.env.API_KEY)
    from_email = Email("aakash21696@gmail.com")
    to_email = Email("aakash21696@gmail.com")
    subject = "Kindle price change"
    message = "Kindle price has changed. New price is: " + live_price
    content = Content("text/plain", message)
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body = mail.get())
def get_live_price(url):
    page =  urllib2.urlopen(url).read()
    soup = BeautifulSoup(page, 'html.parser')
    element = soup.find("span", {"id" : "priceblock_ourprice"})
    live_price = element.text.strip()
    return live_price

def check_price(request):
   
    url = "https://amazon.in/dp/B00QJDOEAO"
    live_price = str(get_live_price(url))
    print type(live_price)
    module_dir = os.path.dirname(__file__)
    filename = os.path.join(module_dir, 'price.txt')
    price_file = open(filename, "r+")
    last_price = str(price_file.read().strip())
    if(live_price != last_price):
        
	price_file.seek(0)
	price_file.write(live_price)
	price_file.truncate()
	send_email(live_price)

    return HttpResponse("Success")

    
    
