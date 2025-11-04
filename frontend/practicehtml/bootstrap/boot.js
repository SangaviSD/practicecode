let cartCount = 0; // total items in cart
const cartCounter = document.getElementById('cart-count');

document.querySelectorAll('.card-item').forEach(card => {
  const plus = card.querySelector('.plus');
  const minus = card.querySelector('.minus');
  const count = card.querySelector('.count');
  let value = 0;

  plus.addEventListener('click', () => {
    value++;
    count.textContent = value;
    cartCount++;
    cartCounter.textContent = cartCount;
  });

  minus.addEventListener('click', () => {
    if (value > 0) {
      value--;
      count.textContent = value;
      cartCount--;
      cartCounter.textContent = cartCount;
    }
  });
});
