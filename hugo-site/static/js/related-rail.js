/* 相关文章侧栏：随滚动吸附（因主题 body { overflow: hidden } 使 CSS sticky 失效，用 JS 模拟） */
(function () {
  'use strict';

  function init() {
    // 仅桌面端（lg 以上，侧栏与正文并排）
    if (!window.matchMedia('(min-width: 992px)').matches) return;

    var rail = document.querySelector('.related-rail');
    if (!rail) return;
    var col = rail.parentElement;
    if (!col) return;
    col.style.position = 'relative';

    var OFFSET = 92; // fixed-top header 高度余量

    function reset() {
      rail.style.position = '';
      rail.style.top = '';
      rail.style.bottom = '';
      rail.style.width = '';
    }

    function update() {
      if (!window.matchMedia('(min-width: 992px)').matches) {
        reset();
        return;
      }
      var cr = col.getBoundingClientRect();
      var rh = rail.offsetHeight;

      if (cr.top <= OFFSET && cr.bottom > OFFSET + rh) {
        // 吸附：跟随滚动，始终可见
        rail.style.position = 'fixed';
        rail.style.top = OFFSET + 'px';
        rail.style.bottom = 'auto';
        rail.style.width = cr.width + 'px';
      } else if (cr.bottom <= OFFSET + rh && cr.top <= OFFSET) {
        // 滚到文章末尾：停靠在侧栏底部，随内容自然滚走
        rail.style.position = 'absolute';
        rail.style.top = 'auto';
        rail.style.bottom = '0';
        rail.style.width = '100%';
      } else {
        // 侧栏顶部还在视口下方：保持原位
        reset();
      }
    }

    window.addEventListener('scroll', update, { passive: true });
    window.addEventListener('resize', update);
    update();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
