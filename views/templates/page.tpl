% include('includes/header.tpl', title=title)
<body>
% include('includes/navigation.tpl')
<div class="content">
% include('content/' + title + '.tpl', title=title)
</div>
<style>
% include('assets/css.tpl')
</style>
% include('assets/scripts.tpl')
</body>
% include('includes/footer.tpl')
