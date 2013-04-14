data = {}
r = re.findall(r'type="(?:hidden|submit)?" name="(.+?)"\s* value="?(.+?)">', html)
for name, value in r:
    data[name] = value
    
html = net.http_POST(url, data).content

pattern = r'type="(?:hidden|submit)?" name="(.+?)"\s* value="?(.+?)">'
data = dict((key,value) for key,value in re.search(pattern, html))