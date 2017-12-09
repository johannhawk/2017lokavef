
<head>
  <link rel="stylesheet" type="text/css" href="css1.css">
</head>
<h3>Bæta við nýtt til listan</h3><br>
<form action="/new" method="POST">
<label>Task</label><br>
<input type="text" size="100" name="task"><br>
<label>Description</label><br>
<textarea name="desc" rows="10" cols="30"></textarea><br>
<input type="submit" name="save" value="save"><br>
<input type="button" name="Cancel" onclick="parent.location='/'">
</form>
