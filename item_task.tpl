<head>
  <link rel="stylesheet" type="text/css" href="css1.css">
</head>
<div class="task_title">
<h2>{{todotitle}}</h2>
</div>
<div class="task_date">posted: {{tododate}}</div>
<div class="task_desc"><p>{{tododesc}}</p></div>
<button type="button" onClick="goBack">Back</button><button type="button" onClick="location.href='/edit{{todoid}}'">Edit</button>
<script type="text/javascript">
	function goBack() {
		window.history.back();
	}
</script>

