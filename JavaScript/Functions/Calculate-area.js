// a) Calculate Area Function:
function calculateArea(width,height){
    return (width*height);
};
console.log(calculateArea(width=5,height=10));

// b) Modify Calculate Area Function with Default Values:
function calculateAreaWithDefaults(width=1,height=1){
    return (width*height);
};
console.log(calculateAreaWithDefaults());
console.log(calculateAreaWithDefaults(width=5,height=10));

// c) Rewrite Calculate Area as a Function Expression:
const calculateAreaFunction = function (width=1,height=1){
    return (width*height);
}
console.log(calculateAreaFunction(5,10));

// d) Rewrite Calculate Area as an Arrow Function:
const calculateAreaArrow = (width=1,height=1)=>{
    return (width*height);
}
console.log(calculateAreaArrow(5,10));