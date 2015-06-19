% include('includes/header.tpl', title=title)
<body>
% include('includes/navigation.tpl')
<div class="content">
<h1>Error {{title}}</h1>
<p>Sorry! Looks like something went very wrong.</p>
<p>We've been sent a crash report, and will try and fix it as soon as possible.</p>
</div>
<style>
% include('assets/css.tpl')
</style>
% include('assets/scripts.tpl')
</body>
% include('includes/footer.tpl')
