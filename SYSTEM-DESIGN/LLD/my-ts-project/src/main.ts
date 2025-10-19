import type { User } from "./models/user.js";
import { isValidEmail } from "./utils/validation.js";

function registerUser(user: Omit<User, "id" | "isActive">): User | null {
  if (!isValidEmail(user.email)) {
    console.error("invalid email");
    return null;
  }

  const newUser: User = {
    id: Date.now(),
    name: user.name,
    email: user.email,
    age: user.age,
    isActive: true,
  };

  console.log("user is registered:", newUser);
  return newUser;
}

console.log("✅ main.ts is running");
registerUser({
  name: "John Doe",
  email: "john.doe@example.com",
  age: 25,
});

process.stdout.write('how many user you wanna')
