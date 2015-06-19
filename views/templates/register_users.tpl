% include('includes/header.tpl', title=title)
<body>
% include('includes/navigation.tpl')
<div class="content">
<h1>{{title}}</h1>
% if user != False:
     <form action="/register" method="post">
     <input name="email" type="email" required placeholder="example@email.com" /><br>
     <input name="pass" type="password" required placeholder="Password" /><br>
     <input value="Submit" type="submit" />
     </form>
     <p><strong>Warning:</strong> If you use an email aready in the database, this will reset their password.</p>
% else:
    <p>Sorry, only logged in users can do that.</p>
% end
</div>
<style>
% include('assets/css.tpl')
</style>
% include('assets/scripts.tpl')
</body>
% include('includes/footer.tpl')
