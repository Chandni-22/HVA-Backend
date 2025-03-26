// a) Define Callback Functions for Area Calculations:
function areaOfRectangle(length,width){
    return (length*width);
}
function areaOfCircle(radius,_){
    return (Math.PI*radius*radius);
} 
function areaOfTriangle(base,height){
    return (0.5*base*height);
}

// b) Define calculatePaintingCost Function:
function calculatePaintingCost(dimension1,dimension2,calculateArea){
    const area=calculateArea(dimension1,dimension2);
    const costPerUnit=2;
    const totalCost=area*costPerUnit;
    return totalCost;
}

// c) Call calculatePaintingCost with Different Callback Functions:
console.log(calculatePaintingCost(5,10,areaOfRectangle));
console.log(calculatePaintingCost(3,null,areaOfCircle));
console.log(calculatePaintingCost(6,8,areaOfTriangle));