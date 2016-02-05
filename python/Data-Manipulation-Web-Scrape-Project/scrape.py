#!/usr/bin/env python
import urllib2
from bs4 import BeautifulSoup as BS
import re
import codecs
import time
import csv
import json




isis = re.compile(r'Islamic State')
www = re.compile(r'//(.+?)/')
header1 = ['Dates:','Feb 22','', 'Feb 23','' ]
header2 = ['Newspaper Title', 'IS References on Website', 'Wikipedia References to Newspaper','IS References on Website', 'Wikipedia References to Newspaper']

wsj_freq = ['Wall Street Journal']
nyt_freq = ['New York Times']
guard_freq = ['The Guardian']
alj_freq = ['AlJazeera']
top_ten = ['Top Ten External References']

def the_whole_thing():
    wsj_html = urllib2.urlopen('http://www.wsj.com/public/page/news-global-world.html?refresh=on', timeout = 90)
    wsj = BS(wsj_html)
    headlines = wsj.find_all('p')
    count = 0
    for line in headlines:
        if line.string != None:
            #print line
            #print line.string.encode('utf-8')
            key_word = isis.findall(line.string.encode('utf-8'))
            #print key_word
            if key_word:
             count = count + 1
        else: continue
    wsj_freq.append(count)
    
    nyt_html = urllib2.urlopen('http://www.nytimes.com/pages/world/index.html', timeout = 90)
    nyt = BS(nyt_html)
    headlines = nyt.find_all('p')
    count = 0
    for line in headlines:
        if line.string != None:
            #print line
            #print line.string.encode('utf-8')
            key_word = isis.findall(line.string.encode('utf-8'))
            #print key_word
            if key_word:
             count = count + 1
        else: continue
    nyt_freq.append(count)
    
    guard_html = urllib2.urlopen('http://www.theguardian.com/world', timeout = 90)
    guard = BS(guard_html)
    headlines = guard.find_all('p')
    count = 0
    for line in headlines:
        if line.string != None:
            #print line
            #print line.string.encode('utf-8')
            key_word = isis.findall(line.string.encode('utf-8'))
            #print key_word
            if key_word:
             count = count + 1
        else: continue
    guard_freq.append(count)
    
    alj_html = urllib2.urlopen('http://america.aljazeera.com/topics/topic/categories/international.html', timeout = 90)
    alj = BS(alj_html)
    headlines = alj.find_all('p')
    count = 0
    for line in headlines:
        if line.string != None:
            #print line
            #print line.string.encode('utf-8')
            key_word = isis.findall(line.string.encode('utf-8'))
            #print key_word
            if key_word:
             count = count + 1
        else: continue
    alj_freq.append(count)

    wiki_raw = urllib2.urlopen('http://en.wikipedia.org/w/api.php?format=json&action=query&titles=Islamic_State_of_Iraq_and_the_Levant&prop=revisions&rvprop=content&continue=')
    wiki = unicode(wiki_raw.read(), 'utf-8')
    #print wiki
    web_addresses ={}
    web_address=www.findall(wiki)
    for item in web_address:
        web_addresses[item] = web_addresses.get(item,0)+1
    hist = []
    for k,v in web_addresses.iteritems():
         x = (k,v)
         hist.append(x)
    wsj_freq.append(web_addresses['www.wsj.com'])
    nyt_freq.append(web_addresses['www.nytimes.com'])
    guard_freq.append(web_addresses['www.theguardian.com'])
    alj_freq.append(web_addresses['www.aljazeera.com'])
    
for i in [1]:
    the_whole_thing()
    print 'Done', i
    time.sleep(86400)


the_whole_thing()


sheet = open('final_project_output_jlwohlf.csv', 'wb')
w = csv.writer(sheet)
w.writerow(header1)
w.writerow(header2)
w.writerow(wsj_freq)
w.writerow(nyt_freq)
w.writerow(guard_freq)
w.writerow(alj_freq)


sheet.close()
