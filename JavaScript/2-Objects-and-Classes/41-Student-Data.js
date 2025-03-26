// a) Define and Populate the student Object:
let student={};
student.name="Chandni Vishwakarma";
student.email="chandni22@navgurukul.org";
student.age=21;

console.log(student.name);

// b) Update the student Object:
student.age=10;
console.log(student.age);

// c) Add Method and Nested Object to student:
student.greet=function(){
    return(`Hello, ${this.name}!`);
};
console.log(student.greet());

student.address={
    country:"India",
    city:"Delhi",
    pin_code:110076,
};
console.log(student.address.country);
student.address.pin_code = 400002;
console.log(student.address);

// d) Create and Populate the friend Object:
let friend={
    name:"Sangeeta",
    email:"Sangeeta22@navgurukul.org",
    age: 25,
    greet:function(){
        return(`Hello, ${this.name}!`);
    },
    address:{
        country:"India",
        city:"Agra",
        pin_code:110043,
    },
};
console.log(friend.greet());
console.log(friend);

// e) Create and Populate the topper Object:
let topper={
    name:"Bhawna",
    email:"bhawna22@navgurukul.org",
    age: 22,
    greet:function(){
        return(`Hello, ${this.name}!`);
    },
    address:{
        country:"India",
        city:"Delhi",
        pin_code:110076,
    },
};
console.log(topper.greet());
console.log(topper);

// f) Define and Use the Student Class:
class Student{
    constructor(name,email,age,country,city,pin_code){
        this.name=name;
        this.email=email;
        this.age=age;
        this.address={
            country:country,
            city:city,
            pin_code:pin_code,
        };
    }
    greet(){
      console.log(`Hello, ${this.name}!`);
    }
    getFullAddress(){
      console.log(`${this.address.country}, ${this.address.city}-${this.address.pin_code}`);
    }
}

// g) Create and Log Student Objects:
let student_1=new Student("Chandni","chandni22@navgurukul.org",21,"India","Delhi",110076);
let student_2=new Student("Sangeeta","sangeeta22@navgurukul.org",25,"India","Agra",110043);
let student_3=new Student("Bhawna","bhawna22@navgurukul.org",22,"India","Delhi",110076);
console.log(student_1);
console.log(student_2);
console.log(student_3);

// h) Call the greet Method and getFullAddress Method on Student Objects:
student_1.greet();
student_1.getFullAddress();

student_2.greet();
student_2.getFullAddress();

student_3.greet();
student_3.getFullAddress();