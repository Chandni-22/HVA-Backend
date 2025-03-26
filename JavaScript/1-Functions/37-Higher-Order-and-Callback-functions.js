// a) Define Higher Order Function:
function higherOrderFunction(num,callback){
    callback(num);
}

// b) Define Callback Function and Call Higher Order Function:
function callbackFunction(number){
    console.log(number);
}
higherOrderFunction(5,callbackFunction);

// c) Call Higher Order Function with a Function Expression as Callback:
higherOrderFunction(10,function(number){
    console.log(number);
})

// d) Call higherOrderFunction with 4 and a function expression to log the square
higherOrderFunction(4, function(number){
    console.log(number**2);
})

// e) Callback to Log Sum of Two Numbers:
function newHigherOrderFunction(num1,num2,callback){
    callback(num1,num2);
}

newHigherOrderFunction(3,7,function(num1,num2){
    console.log(num1+num2);
})