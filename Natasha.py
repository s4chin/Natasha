#!/usr/bin/env python
import string
import sys

import cleverbot
import requests
import wikipedia

from lxml import etree

# Fix to remove requests error, saw on SO url
# http://stackoverflow.com/questions/19105255/praw-failed-to-parse-cpython-sys-version-when-creating-reddit-object
sys.version = '2.7.3 (default, Apr 12 2012, 14:30:37) [MSC v.1500 32 bit (Intel)]'

def dictionary(word):
	print "Idk"

def movie(title):
	url = "http://www.omdbapi.com/?t=" + title + "&y=&plot=full&r=json"
	url = url.replace(" ", "+")
	r = requests.get(url)
	data = r.json()
	if not data['Response']:
		print "Movie not found"
	else:
		print "Title: " + data["Title"] + " Year: " + data["Year"]
		print "\nMetascore: " + data["Metascore"] + " IMDB Rating: " + data["imdbRating"] + " IMDB votes: " + data["imdbVotes"]
		print "\nPlot: " + data["Plot"] + "\n"

def weather(place):
	url = "api.worldweatheronline.com/free/v2/weather.ashx?q=" + place + "&format=json&num_of_days=5&key=e4f2a94c501636c69782bf90269bd"
	r = requests.get(url)
	data = r.json()

def wiki(title):
	try:
		print (wikipedia.summary(title)).encode('ascii', 'ignore')
	except:
		print "Sorry, I could not find a summary, make sure your spelling is correct and please try again."

def yomomma():
	try:
		print ((requests.get("http://api.yomomma.info")).json())['joke']
	except:
		print "Sorry, no yo momma jokes at this moment."

def chuck():
	try:
		response = requests.get("http://api.icndb.com/jokes/random")
		data = response.json()
		if data['type'] == 'success':
			print data['value']['joke']
		else:
			print "Sorry, no Chuck Norris jokes at this moment"
	except:
		print "Sorry, no Chuck Norris jokes at this moment"

def chat():
	print "Talk to me"
	
	while True:
		string = raw_input()
		bot = cleverbot.Cleverbot()
		if string:
			if string[0] == '#':
				if string[1:5] == 'dict':
					dictionary(string[6:])
				elif string[1:6] == 'movie':
					movie(string[7:])
				elif string[1:5] == 'wiki':
					wiki(string[6:])
				elif string[1:8] == 'yomomma':
					yomomma()
				elif string[1:6] == 'chuck':
					chuck()
			else:
				try:
					print bot.ask(string)
				except:
					print "Can't talk now. Try again later."
		else:
			continue


if __name__ == '__main__':
	chat()

# TODO weather
# dict