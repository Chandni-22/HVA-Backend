// a) Define Callback Functions:
function addNumbers(a,b){
    return (a+b);
};
  
function multiplyNumbers(a,b){
    return (a*b);
};
  
function subtractNumbers(a,b){
    return (a-b);
};
  
function divideNumbers(a,b){
    if (b===0){
      return ('Error: Division by zero is undefined');
    };
    return (a/b);
};

// b) Define performArithmetic Function:
function performArithmetic(num1,num2,operation){
    return (operation(num1,num2));
};

// c) Call performArithmetic with Callback Functions:
console.log(performArithmetic(5,3,addNumbers));
console.log(performArithmetic(5,3,multiplyNumbers));
console.log(performArithmetic(5,3,subtractNumbers));
console.log(performArithmetic(5,3,divideNumbers));