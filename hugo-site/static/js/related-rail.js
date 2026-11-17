/* 相关文章侧栏：JS 显式 fixed 定位跟随滚动（left/top/width 每帧重算，绝不横向漂移） */
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

    function reset() {
      rail.style.position = '';
      rail.style.top = '';
      rail.style.left = '';
      rail.style.width = '';
    }

    function update() {
      ticking = false;
      if (!window.matchMedia('(min-width: 992px)').matches) {
        reset();
        return;
      }
      var cr = col.getBoundingClientRect();
      var rh = rail.offsetHeight;

      if (cr.top <= OFFSET && cr.bottom >= OFFSET + rh) {
        // 跟随：fixed 定位，水平位置每帧取自列，保证不漂移
        var top = OFFSET;
        if (cr.bottom < OFFSET + rh) {
          top = cr.bottom - rh; // 文章末尾：钳制在列底部
        }
        rail.style.position = 'fixed';
        rail.style.top = Math.round(top) + 'px';
        rail.style.left = Math.round(cr.left) + 'px';
        rail.style.width = Math.round(cr.width) + 'px';
      } else {
        // 回到原位（文档流），与初始状态完全一致
        reset();
      }
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
