// a) Greet Function:
function greet(name){
    return (`Hello, ${name}!`);
};
console.log(greet("Alice"));

// b) GreetDefault Function:
function greetDefault(name="Guest"){
    return (`Hello, ${name}!`);
};
console.log(greetDefault());

// c) Rewrite Greet as a Function Expression:
const greetFunction=function(name){
    return (`Hello, ${name}!`);
};
console.log(greetFunction("Chandni"));

// d) Rewrite Greet as an Arrow Function:
const greetArrow=(name)=>{
    return (`Hello, ${name}!`);
};
console.log(greetArrow("Bhawna"));