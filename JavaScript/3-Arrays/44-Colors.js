// a) Define and Log the colors Array:
let colors=["red","green","blue"];
console.log(colors[0]);

// b) Modify and Add color elements:
colors[1]="yellow";
console.log(colors[1]);

colors.push("purple"); // Push add a new element to the end of the array and returns the new length.
console.log(colors[colors.length-1]);

// c) Iterate using Loops over the colors Array:
console.log("Using for loop:");
for (let i=0;i<colors.length;i++){
    console.log(colors[i]);
}

console.log("Using while loop:");
let index=0;
while (index<colors.length){
  console.log(colors[index]);
  index++;
}

console.log("Using for...of loop:");
for (let color of colors) {
  console.log(color);
}

// d) Check Array Properties:
console.log(typeof colors);
console.log(colors.length);

// e) Array Methods:
colors.push("orange");
console.log(colors);

colors.pop(); // Pop remove the last element of the array and returns the removed element.
console.log(colors);

let blueIndex=colors.indexOf("blue"); // indexOf finds index of an element.
console.log(`Index of blue is ${blueIndex}.`);

// f) Add and Iterate Over Properties:
colors.owner="Chandni Vishwakarma"; 
console.log(colors);

console.log("Using for...in loop to iterate over properties:");
for (let property in colors){
  console.log(`${property}: ${colors[property]}`);
}