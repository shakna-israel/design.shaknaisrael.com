<%
    import datetime
    cur_time = datetime.datetime.now()
    cur_year = cur_time.year
%>
<footer>
<p>&copy; {{cur_year}} - {{ site_author }}</p>
% if user:
    <p>Logged In</p>
% else:
    <p>Cookies are used for logins.</p>
% end
<p class="elevator-button">Back to Top</p>
</footer>
