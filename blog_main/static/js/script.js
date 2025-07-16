const panel = document.querySelector('.panel');

console.log(panel);

panel.addEventListener('click', () => {
    panel.classList.toggle('active');
    document.body.style.overflow = panel.classList.contains('active') ? 'hidden' : 'auto';
});