// a) Define and Initialize the Array:
let numbers=[1,2,3,4,5];

// b) Iterate and Log Using forEach():
// The forEach() method does not modify the original array but iterates over each element in the array, performing the specified operation provided in the callback function.
numbers.forEach(function(number){
    console.log(number);
});

numbers.forEach(function(number){
    console.log(number*2);
});

// c) Iterate and Create a New Modified Array Using map():
// The map() does not modify the original array but instead returns a new array containing the results of the transformation.
let squaredNumbers=numbers.map(function(number){
    return(number*number);
});
console.log(squaredNumbers);

squaredNumbers=numbers.map(number=>(number*number));
console.log(squaredNumbers);

// d) Iterate and Create a New Filtered Array Using filter():
// The filter() function in JavaScript is an array method that creates a new array containing only the elements of the original array that meet a specified condition.
let evenNumbers=numbers.filter(function(number){
    return(number%2===0);
});
console.log(evenNumbers);

evenNumbers=numbers.filter(number=>(number%2===0));
console.log(evenNumbers);