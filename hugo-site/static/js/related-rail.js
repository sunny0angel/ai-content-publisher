/* 相关文章侧栏：纯 translateY 跟随滚动。
   不使用 fixed/absolute（祖先 transform 会破坏其参照系导致横向漂移），
   translateY 只有垂直分量，任何情况下都不会横向移动。 */
(function () {
  'use strict';

  function init() {
    if (!window.matchMedia('(min-width: 992px)').matches) return;

    var rail = document.querySelector('.related-rail');
    if (!rail) return;
    var col = rail.parentElement;
    if (!col) return;

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

      var delta = -colRect.top + OFFSET;
      var maxDelta = Math.max(0, colH - railH);
      if (delta < 0) delta = 0;
      if (delta > maxDelta) delta = maxDelta;

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
