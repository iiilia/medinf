def save(x):
    import urllib
    logo = urllib.urlopen(x).read()
    f = open(".//temp.tmp", "wb")
    f.write(logo)
    f.close()