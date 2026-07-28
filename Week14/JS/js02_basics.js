// JS BASICS — Object references & Functions as first-class values
// (This code was already correct/runnable — comments added for clarity)

// ---- 1. Objects are assigned/passed by reference ----

const person1 = {
  age: 20,
};

// person2 doesn't copy the object — it points to the SAME object in memory
const person2 = person1;

person2.age = 50;

// Because both variables reference the same object, changing it through
// either name affects what you see through the other name too.
console.log(person1.age); // 50
console.log(person2.age); // 50

// Note: const still applies here — you can't do person1 = {} or person2 = {},
// but mutating the object's properties is fine (see previous file, section 3).

// ---- 2. Functions are objects too — they can hold properties ----

function greet() {
  console.log("Hello");
}

// Add a custom property directly onto the function object
greet.language = "English";

console.log(greet.language); // "English"

// greet() still works normally as a function call
greet(); // "Hello"

// ---- 3. Function expressions (function stored in a variable) ----

const sayHello = function () {
  console.log("Hello");
};

sayHello(); // "Hello"

// ---- 4. Functions passed as arguments (callbacks) ----

function execute(fn) {
  fn();
}

execute(sayHello); // "Hello" — sayHello is passed in and invoked inside execute

// ---- 5. Functions returned from other functions (closures) ----

function createGreeting() {
  return function () {
    console.log("Welcome!");
  };
}

const greeting = createGreeting();

greeting(); // "Welcome!"

// Why this works: createGreeting() runs once, returns a new function.
// That inner function is stored in 'greeting' and can be called later,
// independent of createGreeting itself having already finished running.
