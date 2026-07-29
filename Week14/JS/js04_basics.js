// 1. CLASSES & SUPER
class Employee {
  constructor(name, baseSalary) {
    this.name = name;
    this.baseSalary = baseSalary;
  }

  getPay = () => this.baseSalary;
}

class Manager extends Employee {
  constructor(name, baseSalary, bonus) {
    super(name, baseSalary); // Sets up base Employee properties
    this.bonus = bonus;
  }

  // Overrides getPay to include bonus
  getPay = () => this.baseSalary + this.bonus;
}

// 2. SPREAD & REST OPERATORS
const dev1 = new Employee("Alice", 7000);
const dev2 = new Employee("Bob", 6500);
const lead = new Manager("Carol", 9000, 2000);

// Rest operator gathers team members into an array
function assembleTeam(teamLead, ...teamMembers) {
  // Spread operator merges teamLead and teamMembers into one list
  return [teamLead, ...teamMembers];
}

const engineeringTeam = assembleTeam(lead, dev1, dev2);

// 3. ARRAY REDUCE & ARROW FUNCTIONS
// Calculates total monthly expense for the team
const totalPayroll = engineeringTeam.reduce((accumulatedPayroll, member) => {
  return accumulatedPayroll + member.getPay();
}, 0);

console.log(
  "Team Members:",
  engineeringTeam.map((m) => m.name),
);
console.log("Total Monthly Payroll: $" + totalPayroll); // Output: $24500
