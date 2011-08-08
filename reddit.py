#Reddit api votes and comments
# version 1.0
# Avinash Bangar { avibangar@gmail.com}

from urllib2 import urlopen
from simplejson import loads
import sys
import html

global i
i = 0

print "Reddit Api and votes ups"
comment_id = {}; #store all comment ids
vote_ups = {};	#store all votes
comment_body = {}; #store all comments

url = sys.argv[1] + '.json'   #take url and append json
content = loads(urlopen(url).read()) #fetch data from reddit


#Function will fetch comments and vote ups recursively
def level(data,i):

	for d2 in data.items():

		if d2[0] == 'data':

			for d3 in d2[1].items():

				if d3[0] == 'children':
					for d4 in d3[1]:

						for d5 in d4['data'].items():
							
							if d5[0] == 'id':
								comment_id[i] = d5[1]
								i = i + 1

							if d5[0] == 'ups':
								vote_ups[i] = d5[1]
								
							#if d5[0] == 'body':
							#	comment_body[i] = d5[1]

							if d5[0] == 'replies' and d5[1] != '':
								i = level(d5[1],i)
	return i

#Function will check for comments and votes
def reddit(content):
	count = 0
	for data in content:

		    for d1 in data['data']:
			if count == 1:
		            	level(data,i)
			count = count + 1
			break;
	return


reddit(content)

html.print_data(comment_id,vote_ups)




		


