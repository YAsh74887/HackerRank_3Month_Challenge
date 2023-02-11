
time = "11:21:30PM"
t = time[:-2]
print(t)


from datetime import datetime

def convert24(time):
	# Parse the time string into a datetime object
	t = datetime.strptime(time, '%I:%M:%S%p')
	# Format the datetime object into a 24-hour time string
	return t.strftime('%H:%M:%S')

print(convert24('11:21:30PM')) # Output: '23:21:30'
# print(convert24('12:12:20AM')) # Output: '00:12:20'
