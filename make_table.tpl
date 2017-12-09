%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<head>
  <link rel="stylesheet" type="text/css" href="css1.css">
</head> 
<body>
<a href="http://localhost:8080/todo">Listi</a>

<a href="http://localhost:8080/new">Nytt</a>




<table border="1">
%for row in rows:
<tr>
  <td><a href="/item{{row[0]}}">{{row[1]}}</a></td>
</tr>
%end
</table>
<form>
	<input type="button" value="Add New Task" onclick="parent.location='/new'">
</form>
</body>