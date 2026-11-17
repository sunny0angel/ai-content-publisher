/* 相关文章侧栏：translateY 平滑跟随滚动。
   主题 body { overflow: hidden } 使 CSS sticky 失效，且滚动可能发生在内层容器，
   故用 JS + 捕获阶段 scroll 监听 + transform（无重排、无跳动、回顶完全复原）。 */
(function () {
  'use strict';

  function init() {
    if (!window.matchMedia('(min-width: 992px)').matches) return;

    var rail = document.querySelector('.related-rail');
    if (!rail) return;
    var col = rail.parentElement;
    if (!col) return;
    col.style.position = 'relative';

    var OFFSET = 92; // fixed-top header 高度余量
    var ticking = false;

    function update() {
      ticking = false;
      if (!window.matchMedia('(min-width: 992px)').matches) {
        rail.style.transform = '';
        return;
      }
      var colRect = col.getBoundingClientRect();
      var railH = rail.offsetHeight;
      var colH = col.offsetHeight;
      var maxDelta = colH - railH;
      var delta = -colRect.top + OFFSET;

      if (delta < 0) delta = 0;
      if (maxDelta > 0 && delta > maxDelta) delta = maxDelta;

      rail.style.transform = 'translateY(' + Math.round(delta) + 'px)';
    }

    function onScroll() {
      if (!ticking) {
        ticking = true;
        requestAnimationFrame(update);
      }
    }

    // capture=true 捕获内层滚动容器的 scroll 事件（主题可能不在 window 上滚动）
    document.addEventListener('scroll', onScroll, true);
    window.addEventListener('resize', onScroll);
    update();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
