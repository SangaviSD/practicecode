// total items in cart
let cartCount = 0;
const cartCounter = document.createElement('div');
cartCounter.className = 'cart';
cartCounter.innerHTML = '🛒 <span id="cart-count">0</span>';
document.body.appendChild(cartCounter);

const countSpan = document.getElementById('cart-count');

document.querySelectorAll('.card-item').forEach(card => {
  const plus = card.querySelector('.plus');
  const minus = card.querySelector('.minus');
  const count = card.querySelector('.count');
  let value = 0;

  plus.addEventListener('click', () => {
    value++;
    count.textContent = value;
    cartCount++;
    countSpan.textContent = cartCount;
  });

  minus.addEventListener('click', () => {
    if (value > 0) {
      value--;
      count.textContent = value;
      cartCount--;
      countSpan.textContent = cartCount;
    }
  });
});
