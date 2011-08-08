#Html generation



def print_data(comment_id,vote_ups):
	
	j = 0
	print "<html>"
	print "<head>"
	print "<script src='/home/avinash/programs/python/sort.js'></script>"
	print "</head>"
	print "<body>"
	print "<table id='results'>"
	print "<thead><tr><th><a onclick='SortTable(0);' href='javascript:;'>Comment Id</a></th><th><a onclick='SortTable(1);' href='javascript:;'>Votes</a></th></tr></thead>"

	print "<tbody>"
	num_of_comments = len(comment_id)	
	while (j < num_of_comments):
		print "<tr><td>",comment_id[j],"</td><td> ",vote_ups[j],"</td></tr>"	
		j = j + 1
	print "</tbody>"
	print "</table>"
	print "</body>"
	print "</html>"
