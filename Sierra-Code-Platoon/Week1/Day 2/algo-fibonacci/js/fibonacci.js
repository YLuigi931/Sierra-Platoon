const fibonacci = (num) => {
    if (num == 1) return 1;
    let current = 0;
    let previous = 1;
    let holder = 0;
    
    while(num != 0){
        holder = current;
        current += previous;
        // console.log(current);
        previous = holder;
        num--;
    }
    return current;
}

// function fibonacci(num){
//     let current = 0;
//     let previous = 1;
//     let holder = 0;
    
//     while(num != 0){
//         holder = current;
//         current += previous;
//         // console.log(current);
//         previous = holder;
//         num--;
//     }
//     return current;
// }

// console.log(fibonacci(3));

module.exports = {fibonacci}
