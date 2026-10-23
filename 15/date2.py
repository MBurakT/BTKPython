from datetime import datetime, timedelta

birthday = datetime(1990, 1, 1, 12, 30, 0)

print(birthday)

result = datetime.timestamp(birthday) # datetime to second
result = datetime.fromtimestamp(result) # second to datetime

result = datetime.fromtimestamp(0)

result = datetime.today() - birthday #timedelta

result = result.days

result = datetime.now() + timedelta(days = 10, minutes = 10)

print(result)

