def convert_time(time):
  # write your code here
	hours = int(time[0:time.index(":")])
	mints = time[time.index(":") + 1:time.index(':') + 3]
	zone = [" am"," pm"]
	if time[-1].isalpha():
	    if time[-2] == 'p':
	        if hours < 12:
	            hours += 12
	        else:
	            hours = 12
	    elif time[-2] == 'a':
	        if hours == 12:
	            hours = 0
	elif int(time[0:time.index(":")]) <= 12:
	    hours = int(time[0:time.index(":")])
	    mints += zone[0]
	elif int(time[0:time.index(":")]) == 0:
	    hours = 0
	    mints += zone[0]
	else:
	        hours -= 12
	        mints += zone[1]

	return str(hours)+ ":" + mints
