# Cherry

import xbmcgui
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen
import json

publicip = None
publiccountry = None

if publicip == None:
	try:
		result = json.load(urlopen('http://ip-api.com/json'))
		publicip = result['query']
		publiccountry = result['country']
	except: pass

if publicip == None:
	try:
		result = json.load(urlopen('http://freegeoip.net/json/'))
		publicip = result['ip']
		publiccountry = result['country_name']
	except: pass
	
if publicip == None:
	try:
		result = json.load(urlopen('https://tools.keycdn.com/geo.json'))
		publicip = result['data']['geo']['ip']
		publiccountry = result['data']['geo']['country_name']
	except: pass
	
if publicip == None:
	try:
		result = json.load(urlopen('http://extreme-ip-lookup.com/json/'))
		publicip = result['query']
		publiccountry = result['country']
	except: pass
	
if publicip == None:
	try: publicip = urlopen('http://ip.42.pl/raw').read()
	except: pass

if publicip == None:
	try: publicip = json.loads(urlopen('http://httpbin.org/ip'))['origin']
	except: pass
	
if publicip == None:
	try: publicip = json.loads(urlopen('https://api.ipify.org/?format=json'))['ip']
	except: pass

if publicip == None: publicip = ''
if publiccountry == None: publiccountry = ''

xbmcgui.Window(10000).setProperty('publicnetwork', '%s %s' % (publicip, publiccountry))
xbmcgui.Window(10000).setProperty('publicnetworkformat', '%s ||[COLOR FF73FFDE] %s[/COLOR]' % (publicip, publiccountry))
xbmcgui.Window(10000).setProperty('publicip', publicip)
xbmcgui.Window(10000).setProperty('publiccountry', publiccountry)