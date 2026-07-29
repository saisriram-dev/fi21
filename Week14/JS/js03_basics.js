// 1. CLASSES & SUPER
class Product {
  constructor(name, price) {
    this.name = name;
    this.price = price;
  }
}

class SaleProduct extends Product {
  constructor(name, price, discountRate) {
    super(name, price); // Passes name and price to Product constructor
    this.discountRate = discountRate;
  }

  // Arrow function method to compute discounted price
  calculateSalePrice = () => this.price * (1 - this.discountRate);
}

// 2. REST & SPREAD OPERATORS
// Rest operator (...items) gathers all individual arguments into an array
function createOrder(...items) {
  return items;
}

const phone = new Product("Smartphone", 800);
const charger = new SaleProduct("Fast Charger", 40, 0.25); // 25% off = $30
const caseCover = new Product("Phone Case", 20);

const baseOrder = createOrder(phone, charger);

// Spread operator (...) expands baseOrder into a new array with caseCover added
const completeOrder = [...baseOrder, caseCover];

// 3. ARRAY REDUCE & ARROW FUNCTIONS
// reduce iterates through completeOrder using an arrow callback
const orderTotal = completeOrder.reduce((runningTotal, item) => {
  // Use discounted price if available, otherwise regular price
  const finalPrice = item.calculateSalePrice
    ? item.calculateSalePrice()
    : item.price;

  return runningTotal + finalPrice;
}, 0); // 0 is the starting runningTotal

console.log("Ordered Items Count:", completeOrder.length);
console.log("Final Order Total: $" + orderTotal); // Output: $850
