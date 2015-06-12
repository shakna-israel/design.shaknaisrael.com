% include('includes/header.tpl', title=title)
<body>
% include('includes/navigation.tpl')
<div class="content">
<h1>{{title}}</h1>
<form action="/login" method="post">
<input name="user" type="email" required placeholder="example@email.com" /><br>
<input name="auth" type="password" required placeholder="ThisIsMyPassword" /><br>
<input value="Submit" type="submit" />
</form>
</div>
<style>
% include('assets/css.tpl')
</style>
% include('assets/scripts.tpl')
</body>
% include('includes/footer.tpl')
