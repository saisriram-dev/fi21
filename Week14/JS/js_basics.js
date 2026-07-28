// JS BASICS — var / let / const, scoping, hoisting, typeof
// (Corrected so the whole file actually runs top to bottom)

// ---- 1. var vs let vs const ----

// var: Function-scoped (avoid using in modern JavaScript)
var age = 20;

// let: Block-scoped (preferred when the value changes)
let score = 95;

// const: Block-scoped (preferred when the value won't be reassigned)
const PI = 3.14159;

console.log(age); // 20
console.log(score); // 95
console.log(PI); // 3.14159

// ---- 2. Scoping behavior ----

// var ignores block scope
var x = 5;

if (true) {
  var x = 10; // Same variable — overwrites the outer x
}

console.log(x); // 10

// let respects block scope
let y = 5;

if (true) {
  let y = 10; // Different variable — shadows the outer y, doesn't touch it
}

console.log(y); // 5

// ---- 3. const prevents reassignment, not modification ----

const person = {
  name: "John",
  age: 20,
};

// Allowed — mutating a property of the object
person.age = 21;

// Not allowed — reassigning the binding itself
// person = {}; // TypeError: Assignment to constant variable.

console.log(person); // { name: "John", age: 21 }

// ---- 4. Hoisting ----
// Declaration is hoisted, initialization is not

console.log(a); // undefined (declaration hoisted, value not yet assigned)

var a = 10;

console.log(a); // 10

var a; // redeclaring var is a no-op — 'a' keeps its current value

console.log(a); // 10 (NOT reset to undefined)

a = 10;

console.log(a); // 10

// Note: let/const are hoisted too, but land in the "Temporal Dead Zone" (TDZ).
// Accessing them before their declaration line throws a ReferenceError instead
// of returning undefined. Try this in its own scope to see it:
//
// console.log(b); // ReferenceError: Cannot access 'b' before initialization
// let b = 5;

// ---- 5. typeof with primitive types ----
// (renamed from 'age'/'name' to avoid re-declaring let/const identifiers above)

let age2 = 20;
let name2 = "Alice";
let isStudent = true;
let value = null;
let data;
let id = Symbol("id");
let bigNumber = 12345678901234567890n;

console.log(typeof age2); // "number"
console.log(typeof name2); // "string"
console.log(typeof isStudent); // "boolean"
console.log(typeof value); // "object"  <- historical bug, null is NOT an object
console.log(typeof data); // "undefined"
console.log(typeof id); // "symbol"
console.log(typeof bigNumber); // "bigint"

// ---- 6. typeof with reference types ----
// (renamed 'person' -> 'person2' to avoid re-declaring the const above)

const person2 = {
  name: "John",
};

const numbers = [1, 2, 3];

function greet() {
  console.log("Hello");
}

console.log(typeof person2); // "object"
console.log(typeof numbers); // "object"  <- arrays are objects; use Array.isArray() to check for arrays specifically
console.log(typeof greet); // "function"

// Array.isArray(numbers) -> true
// Array.isArray(person2) -> false
