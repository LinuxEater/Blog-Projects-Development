const panel = document.querySelector('.carousel-item');

console.log(panel);

panel.addEventListener('click', () => {
    panel.classList.toggle('active');
    document.body.style.overflow = panel.classList.contains('active') ? 'hidden' : 'auto';
});