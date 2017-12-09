%#template for editing a task
%#the template expects to receive a value for "no" as well a "old", the text of the selected ToDo item
<head>
  <link rel="stylesheet" type="text/css" href="css1.css">
</head> 
<body><a href="http://localhost:8080/todo">Listi</a>

<a href="http://localhost:8080/new">Nytt</a>


<p>Edit the task with ID = {{no}}</p>
<form action="/edit/{{no}}" method="get">
  <input type="text" name="task" value="{{old[0]}}" size="100" maxlength="100">
  <select name="status">
    <option>open</option>
    <option>closed</option>
  </select>
  <br>
  <input type="submit" name="save" value="save">
</form>
</body>
