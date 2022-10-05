var rn = require("./romanNumerals");

const test1 = [1,4,5,6,9];
const ans1 = ['I', 'IV', 'V', 'VI', 'IX'];
const test2 = [11,14,44,99];
const ans2 = ['XI', 'XIV', 'XLIV', 'CMXLIV'];
const test3 = [150,944];
const ans3 = ['CL', 'CMXLIV'];
const test4 = [1000,4000,9999];
const ans4 = ['M','I̅V̅','I̅X̅CMXCIX'];


console.log("ONE DIGIT NUMBERS");
console.log("=================");
for(let x = 0 ; x < test1.length; x++){
    let result = rn.toRoman(test1[x]) === ans1[x];
    if(result == false){
        console.log("Fail at " + test1[x] + " result should be " + ans1[x]);
    }else{
        console.log("PASS " + test1[x] );
    }
}

console.log("TWO DIGIT NUMBERS");
console.log("=================");



console.log("THREE DIGIT NUMBERS");
console.log("===================");



console.log("FOUR DIGIT NUMBERS");
console.log("==================");

console.log(rn.toRoman(1) === 'I');
console.log(rn.toRoman(3) === 'III');
console.log(rn.toRoman(4) === 'IV');
