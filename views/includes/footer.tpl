<%
    import datetime
    cur_time = datetime.datetime.now()
    cur_year = cur_time.year
%>
<footer>
<p>&copy; {{cur_year}} - {{ site_author }}</p>
% if user:
    <p><a href="/logout">Log Out</a></p>
% else:
    <p><a href="/login">Log In</a></p>
% end
<p class="elevator-button">Back to Top</p>
</footer>
