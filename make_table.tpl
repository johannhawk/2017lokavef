%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<head>
  <link rel="stylesheet" type="text/css" href="css1.css">
</head> 
<body>
<a href="http://localhost:8080/todo">Listi</a>

<a href="http://localhost:8080/new">Breyta</a>

<a href="http://localhost:8080/edit">Nytt</a>

<p>The open items are as follows:</p>
<table border="1">
%for row in rows:
  <tr>
  %for col in row:
    <td>{{col}}</td>
  %end
  </tr>
%end
</table>
</body>