// exports.toRoman = function(num) {

exports.toRoman = function(num) {
    let sample = num;
    let result = "";
    // make a map of the roman numeral
    const roman_data = {
        1 : "I",
        5 : "V",
        10 : "X",
        50 : "L",
        100 : "C",
        500 : "D",
        1000 : "M"
    };
    // console.log(roman_data[1000]);
    while(sample != 0){

        // one digit numbers
        if(getLength(sample) == 1){
            if(sample >= 5 && sample != 9){
                result += roman_data[5];
                sample -= 5;
            }else if(sample == 4){
                result += "IV";
                sample -= 4;
            }else if(sample >= 9){
                result += "IX";
                sample -= 9;
            }else{
                result += "I";
                sample -= 1;
            }
        }
        // two digit numbers
        else if(getLength(sample) == 2){
            if(sample >= 90){
                result += "XC";
                sample -= 90;
            }else if(sample >= 50){
                result += roman_data[50];
                sample -= 50;
            }else if(sample >= 40){
                result += "XL";
                sample -= 40;
            }else{
                result += "X";
                sample -= 10;
            }
        }
        // three digit numbers
        else if(getLength(sample) == 3){
            if(sample >= 900){
                result += "CM";
                sample -= 900;
            }else if(sample >= 500){
                result += "D";
                sample -= 500;
            }else if(sample >= 400){
                result += "CD";
                sample -= 400; 
            }else{
                result += "C";
                sample -= 100;
            }
        }
        else if(getLength(sample) == 4){
            if(sample >= 9000){
                result += "I̅X̅"
                sample -= 9000; 
            }else if(sample >= 5000){
                result += "V̅";
                sample -= 5000;
            }else if(sample >= 4000){
                result += "I̅V̅";
                sample -= 4000;
            }else{
                result += "M";
                sample -= 1000;
            }
                
        }

    }
    return result;
};

function getLength(num){
    return num.toString().length;
}


// console.log(getLength(444));
// console.log(toRoman(4));
