// Photo viewer: click a photo to open it big; arrows / Esc on the keyboard.
(function () {
  var btns = [].slice.call(document.querySelectorAll('.gal button'));
  if (!btns.length) return;
  var lb = document.getElementById('lb'), img = document.getElementById('lbimg'), cap = document.getElementById('lbcap'), cur = 0;
  function show(i) {
    cur = (i + btns.length) % btns.length;
    var b = btns[cur];
    img.src = b.dataset.big;
    var src = b.closest('.gal').nextElementSibling;
    var alt = b.querySelector('img').alt;
    cap.innerHTML = (cur + 1) + ' / ' + btns.length + (alt ? ' · ' + alt.replace(/</g, '&lt;') : '') + (src && src.classList.contains('src') ? ' · ' + src.innerHTML : '');
    lb.hidden = false;
  }
  btns.forEach(function (b, i) { b.addEventListener('click', function () { show(i); }); });
  document.getElementById('lbclose').onclick = function () { lb.hidden = true; };
  document.getElementById('lbprev').onclick = function () { show(cur - 1); };
  document.getElementById('lbnext').onclick = function () { show(cur + 1); };
  lb.addEventListener('click', function (e) { if (e.target === lb) lb.hidden = true; });
  addEventListener('keydown', function (e) {
    if (lb.hidden) return;
    if (e.key === 'Escape') lb.hidden = true;
    if (e.key === 'ArrowLeft') show(cur - 1);
    if (e.key === 'ArrowRight') show(cur + 1);
  });
})();
