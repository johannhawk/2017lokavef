%#template for the form for a new task
<head>
  <link rel="stylesheet" type="text/css" href="css1.css">
</head>
<body>
<a href="http://localhost:8080/todo">Listi</a>

<a href="http://localhost:8080/new">Nytt</a>



<h3>Bæta við nýtt til listan</h3><br>
<form action="/new" method="POST">
<label>Task</label><br>
<input type="text" size="100" name="task"><br>
<label>Description</label><br>
<textarea name="desc" rows="10" cols="30"></textarea><br>
<input type="submit" name="save" value="save"><br>
<input type="button" name="Cancel" value="cancel" onclick="parent.location='/'">
</form>
</body>