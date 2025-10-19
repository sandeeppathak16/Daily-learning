// Type script syntax

let name: string = "sandeep";
let age: number = 123;
let isActive: boolean = true;
let nullValue: null = null;
let undefineValue: undefined = undefined;
let numbers: number[] = [1, 2, 3, 4, 5];
let string: Array<string> = ["a", "b"];
let person: [string, number] = ["sandeep", 25];
enum Color {
  Red,
  Green,
  Blue,
}
enum Status {
  Pending = "PENDING",
}
let notSure: any = 4;
let unseInput: unknown;

// void is used as the return type of functions that don't return a value.
// the never type represents values that never occure. it's used for functions that never return or always throw exception

// Function with parameter types and return type
function greet(name: string): string {
  return `Hello, ${name}!`;
}

// Function with optional parameter
function buildName(firstName: string, lastName?: string): string {
  if (lastName) {
    return `${firstName} ${lastName}`;
  }
  return firstName;
}

// Function with default parameter
function createGreeting(name: string, greeting: string = "Hello"): string {
  return `${greeting}, ${name}!`;
}

// Arrow function with type annotations
const multiply = (a: number, b: number): number => a * b;

// With inferred return type
const divide = (a: number, b: number) => a / b;

// Basic interface
interface User {
  id: number;
  name: string;
  email: string;
  isActive: boolean;
}

// Using the interface
const newUser: User = {
  id: 1,
  name: "John Doe",
  email: "john@example.com",
  isActive: true,
};

// Interface with optional properties
interface Product {
  id: number;
  name: string;
  price: number;
  description?: string; // Optional property
}

// Interface extending another interface
interface Employee extends User {
  employeeId: string;
  department: string;
}

class Person {
  // Class properties with type annotations
  name: string;
  age: number;

  // Constructor
  constructor(name: string, age: number) {
    this.name = name;
    this.age = age;
  }

  // Method with return type
  greet(): string {
    return `Hello, my name is ${this.name} and I am ${this.age} years old.`;
  }
}

// Creating an instance
const alice = new Person("Alice", 30);
console.log(alice.greet()); // Output: Hello, my name is Alice and I am 30 years old.
type Direction = "North" | "East" | "South" | "West"; // literal type

