import webbrowser

#url = "www.google.com"
#webbrowser.register('chrome')

#webbrowser.get()



#url = 'www.google.com'
#webbrowser.register('chrome',
#	None,
#	webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))
#webbrowser.get('chrome').open(url)

url = 'www.google.com'
webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))
webbrowser.get('chrome').open_new(url)

#new window thing didnt work as quite expected