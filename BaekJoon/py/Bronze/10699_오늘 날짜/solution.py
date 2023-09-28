import datetime
tmp = datetime.datetime.today() + datetime.timedelta(hours=-9)
# print(str(tmp)[:10])
print(tmp.strftime("%Y-%m-%d"))
#https://wikidocs.net/104836