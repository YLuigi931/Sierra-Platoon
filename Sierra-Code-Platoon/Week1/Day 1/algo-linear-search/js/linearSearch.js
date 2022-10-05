const arrayToSearchThrough = [];
for (let i = 1; i <= 5; i++) {
    arrayToSearchThrough.push(i);
}
//  console.log(arrayToSearchThrough);
exports.linearSearch = function(valueToFind, arrayToSearchThrough) {
    
    for(let index = 0; index < arrayToSearchThrough.length; index++){
        console.log(index);
        if(valueToFind == arrayToSearchThrough[index]){
            return index;
        }
    };
    return undefined
}

// console.log(linearSearch(2, arrayToSearchThrough));

// exports.linearSearchGlobal = function(valueToFind, arrayToSearchThrough) {

exports.linearSearchGlobal = function (valueToFind, arrayToSearchThrough) {
    // your code here

    var result = [];

    for(let index = 0; index < arrayToSearchThrough.length; index++){
        if(arrayToSearchThrough[index] == valueToFind){
            result.push(index);
        }
    }
    
    if(result.length == 0){
        return undefined;
    }else{
        return result;
    }
    
};

// console.log(linearSearchGlobal('a',['b','a','n','a','n','a']));