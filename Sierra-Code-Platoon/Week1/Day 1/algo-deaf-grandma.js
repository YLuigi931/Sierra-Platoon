function hasLower(str){
    return str.toUpperCase() != str;
};


function deafGrandma() {

    var counter = 0;

    console.log("HEY KID!");

    const prompt = require('prompt-sync')();

    let input = prompt('');
    // console.log(`Hey there ${name}`)
    
    while(input == ""){
        input = prompt("WHAT!");

        if(hasLower(input)){
            console.log("SPEAK UP, KID!");
            input = "";
        }else if(hasLower(input) == false && input != ""){
            console.log("NO, NOT SINCE 1946!");
            input = "";
        }else if(input == "GOODBYE!" && counter == 2){
            console.log("LATER, SKATER!");
        }else if(input == "GOODBYE!"){
            counter++;
            console.log("LEAVING SO SOON?");
            input = "";
        }

    };
    
    
      

};

deafGrandma();