<%
    import datetime
    cur_time = datetime.datetime.now()
    cur_year = cur_time.year
    logout = "http://log:out@" + str(site_host) + ":" + str(site_port)
%>
<footer>
<p>&copy; {{cur_year}} - {{ site_author }}</p>
% if user:
    <p><a href="{{logout}}">Log Out</a></p>
% else:
    <p><a href="/login">Log In</a></p>
% end
<p class="elevator-button">Back to Top</p>
</footer>
