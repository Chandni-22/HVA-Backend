// a) Define Callback Functions:
function doubleNumber(number){
    return (number*2);
}

function squareNumber(number){
    return (number**2);
}

function incrementNumber(number){
    return (number+1);
}

// b) Define performOperation Function:
function performOperation(num,operation){
    return operation(num);
}

// c) Call performOperation with Callback Functions:
console.log(performOperation(5,doubleNumber));
console.log(performOperation(5,squareNumber));
console.log(performOperation(5,incrementNumber));