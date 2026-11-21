(function () {
  'use strict';

  var libPromise = null;
  var jsPromise = null;

  function loadScript(src) {
    return new Promise(function (resolve, reject) {
      var s = document.createElement('script');
      s.src = src;
      s.async = true;
      s.onload = function () { resolve(); };
      s.onerror = function () { reject(new Error('Failed to load ' + src)); };
      document.head.appendChild(s);
    });
  }

  var AFW = window.AFW = window.AFW || {};

  // Loaded on first interaction, not on page load: pdf-lib is ~500 KB.
  AFW.loadPdfLib = function () {
    if (window.PDFLib) return Promise.resolve(window.PDFLib);
    if (!libPromise) {
      libPromise = loadScript('/js/vendor/pdf-lib.min.js').then(function () {
        if (!window.PDFLib) throw new Error('PDFLib unavailable');
        return window.PDFLib;
      });
    }
    return libPromise;
  };

  // PDF.js is only needed by the render-based tools (PDF to JPG, compress).
  AFW.loadPdfJs = function () {
    if (window.pdfjsLib) {
      window.pdfjsLib.GlobalWorkerOptions.workerSrc = '/js/vendor/pdf.worker.min.js';
      return Promise.resolve(window.pdfjsLib);
    }
    if (!jsPromise) {
      jsPromise = loadScript('/js/vendor/pdf.min.js').then(function () {
        if (!window.pdfjsLib) throw new Error('pdfjsLib unavailable');
        window.pdfjsLib.GlobalWorkerOptions.workerSrc = '/js/vendor/pdf.worker.min.js';
        return window.pdfjsLib;
      });
    }
    return jsPromise;
  };

  var FILE_WARN = {
    en: 'Large file ({size} MB). It is processed in this tab and may be slow or exceed mobile memory. Use a desktop browser for files over 100 MB.',
    ja: '大きいファイル（{size} MB）。このタブ内で処理するため時間がかかるか、モバイルのメモリを超える可能性があります。100MBを超える場合はデスクトップブラウザを使ってください。',
    zh: '文件较大（{size} MB）。处理在本标签页内进行，可能较慢或超出手机内存。超过 100 MB 建议使用桌面浏览器。'
  };

  function warnIfLarge(input) {
    var files = input.files;
    if (!files || !files.length) return;
    var total = 0;
    for (var i = 0; i < files.length; i++) total += files[i].size || 0;
    var mb = total / 1048576;
    if (mb < 50) return;

    var root = input.closest('.afw-tool');
    var lang = (root && root.getAttribute('data-lang')) || 'en';
    var text = (FILE_WARN[lang] || FILE_WARN.en).replace('{size}', mb.toFixed(1));

    var next = input.nextElementSibling;
    if (next && String(next.className).indexOf('afw-filewarn') > -1) {
      next.textContent = text;
      return;
    }
    var note = document.createElement('div');
    note.className = 'afw-filewarn';
    note.textContent = text;
    input.insertAdjacentElement('afterend', note);
  }

  function initGuards() {
    var inputs = document.querySelectorAll('.afw-tool input[type=file]');
    for (var i = 0; i < inputs.length; i++) {
      var input = inputs[i];
      if (input.accept && input.accept.toLowerCase().indexOf('pdf') === -1) continue;
      input.addEventListener('change', function () { warnIfLarge(this); });
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initGuards);
  } else {
    initGuards();
  }
})();
