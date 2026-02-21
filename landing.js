// Cat meow interaction
function showMeow(event) {
  const existingBubble = document.querySelector('.meow-bubble');
  if (existingBubble) {
    existingBubble.remove();
  }

  const bubble = document.createElement('div');
  bubble.className = 'meow-bubble';
  bubble.textContent = 'meow';

  const rect = event.target.getBoundingClientRect();
  bubble.style.left = rect.right + 5 + 'px';
  bubble.style.top = rect.top - 20 + 'px';

  document.body.appendChild(bubble);

  setTimeout(() => {
    bubble.remove();
  }, 2000);
}
