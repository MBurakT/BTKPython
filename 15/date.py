from datetime import datetime

result = datetime.now()
result = datetime.today()

result = datetime.now().year
result = datetime.now().month
result = datetime.now().day
result = datetime.now().hour
result = datetime.now().minute
result = datetime.now().second

result = datetime.ctime(datetime.now())
result = datetime.strftime(datetime.today(), "%Y")
result = datetime.strftime(datetime.today(), "%X")
result = datetime.strftime(datetime.today(), "%d")
result = datetime.strftime(datetime.today(), "%A")
result = datetime.strftime(datetime.today(), "%B")
result = datetime.strftime(datetime.today(), "%Y %B %A")

t = "15 April 2026 hour 10:12:30"
result = datetime.strptime(t, "%d %B %Y hour %H:%M:%S")

print(result)
