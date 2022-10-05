// exports.factorial = function(num) {

exports.factorial = function(num) {
    let result = 1;
    for(let x = 1 ; x <= num; x++){
        result *= x;
    }
    return result;
};

// console.log(factorial(4));
