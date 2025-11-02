<script>
function makeToc(container){
  const headers = container.querySelectorAll('h4[id], h5[id]');
  if(!headers.length) return;
  const toc = document.createElement('ol'); toc.className='toc';
  headers.forEach(h=>{
    const li=document.createElement('li');
    const a=document.createElement('a');
    a.href = '#'+h.id; a.textContent = h.textContent;
    li.appendChild(a); toc.appendChild(li);
  });
  const tocWrap = document.createElement('div');
  const h3 = document.createElement('h3'); h3.textContent = 'Tartalom';
  tocWrap.appendChild(h3); tocWrap.appendChild(toc);
  container.insertBefore(tocWrap, container.children[1]);
}
document.addEventListener('DOMContentLoaded', ()=>{
  document.querySelectorAll('.explain').forEach(makeToc);
});
</script>
