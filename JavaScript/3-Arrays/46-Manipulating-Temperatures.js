// a) Define and Initialize the Array:
const temperatures=[-3,14,22,5,-10];

// b) Iterate and Log Using forEach():
temperatures.forEach(function(temp){
    console.log((temp*9/5)+32);
});

temperatures.forEach((temp)=>{
    console.log((temp*9/5)+32);
});

// c) Iterate and Create a New Modified Array Using map():
let temperaturesInFahrenheit;

temperaturesInFahrenheit=temperatures.map(function(temp){
    return ((temp*9/5)+32);
});
console.log(temperaturesInFahrenheit);

temperaturesInFahrenheit=temperatures.map((temp)=>{
    return ((temp*9/5)+32);
});
console.log(temperaturesInFahrenheit);

// d) Iterate and Create a New Filtered Array Using filter():
let belowFreezing;

belowFreezing=temperatures.filter(function(temp){
    return (temp<0);
});
console.log(belowFreezing);

belowFreezing=temperatures.filter((temp)=>{
    return (temp<0);
});
console.log(belowFreezing);