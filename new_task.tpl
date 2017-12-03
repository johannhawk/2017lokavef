%#template for the form for a new task
<head>
  <link rel="stylesheet" type="text/css" href="css1.css">
</head>
<body>
<a href="http://localhost:8080/todo">Listi</a>

<a href="http://localhost:8080/new">Breyta</a>

<a href="http://localhost:8080/edit">Nytt</a>
<p>Add a new task to the ToDo list:</p>
<form action="/new" method="GET">
  <input type="text" size="100" maxlength="100" name="task">
  <input type="submit" name="save" value="save">
</form>
</body>