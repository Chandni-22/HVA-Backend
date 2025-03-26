// a) Define the Employee Class:
class Employee{
    constructor(name,email,age,department,position,salary){
        this.name=name;
        this.email=email;
        this.age=age;
        this.department=department;
        this.position=position;
        this.salary=salary;
    }

// b) Add Methods to the Employee Class:
    introduce(){
        console.log(`Hello, I am ${this.name}, a ${this.position}.`);
    }

    displaySalary(){
        console.log(`Salary: $${this.salary}`);
    }
}

// c) Create and Log employee Objects:
let newEmployee=new Employee("Chandni","chandni22@navgurukul.org",21,"Engineering","Software Developer",50000);
console.log(newEmployee);

let manager=new Employee("Bhawna","bhawna22@navgurukul.org",22,"Management","Project Manager",80000);
console.log(manager);

// d) Call Methods on employee Objects:
newEmployee.introduce();
newEmployee.displaySalary();

manager.introduce();
manager.displaySalary();