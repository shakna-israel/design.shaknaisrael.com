% include('includes/header.tpl', title=title)
<body>
% include('includes/navigation.tpl')
<div class="content">
<h1>{{title}}</h1>
<form action="/Contact" method="post">
<input name="email" type="email" required placeholder="example@email.com" /><br>
<textarea name="message" required placeholder="Your email message"></textarea><br>
<input value="Submit" type="submit" />
</form>
</div>
<style>
% include('assets/css.tpl')
</style>
% include('assets/scripts.tpl')
</body>
% include('includes/footer.tpl')
