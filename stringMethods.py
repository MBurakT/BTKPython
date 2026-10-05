message = ' Hello there. My name is Burak Turhan'

# message = message.upper()
# message = message.lower()
# message = message.title()
# message = message.capitalize()

# message = message.strip()
message = message.split()
# message = message.split('.')
message = '*'.join(message)

index = message.find('Burak')
print(index)

message = message.replace('ç', 'c').replace('ö', 'o')

print(message)
print(message[0])