<h1>{{title}}</h1>
<div class="container">
% for item in portfolio:
    <a href="/{{item['page']}}">
    <div class="portfolio-container">
    <img class="img-portfolio" src="/img/{{item['url']}}" alt="{{item['alt']}}"/>
    </div>
    </a>
% end
</div>
