  <!-- Navigation -->
  <div class="b-nav">
    % for item in navigation:
       % if item != False:
            <li><a class="b-link" href="{{item}}">{{item}}</a></li>
       % end
    % end
  </div>

  <!-- Burger-Icon -->
  <div class="b-container">
    <div class="b-menu">
      <div class="b-bun b-bun--top"></div>
      <div class="b-bun b-bun--mid"></div>
      <div class="b-bun b-bun--bottom"></div>
    </div>

<!-- Burger-Brand -->
    <a href="/" class="b-brand">{{ site_name }}</a>
  </div>
