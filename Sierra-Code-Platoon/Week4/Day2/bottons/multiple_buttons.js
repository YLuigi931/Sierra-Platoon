// var oneElement = document.querySelector("#one");
// var twoElement = document.querySelector("#two");
// var threeElement = document.querySelector("#three");
// var fourElement = document.querySelector("#four");
// var fiveElement = document.querySelector("#five");

// oneElement.addEventListener("click", doSomething, false);
// twoElement.addEventListener("click", doSomething, false);
// threeElement.addEventListener("click", doSomething, false);
// fourElement.addEventListener("click", doSomething, false);
// fiveElement.addEventListener("click", doSomething, false);

// function doSomething(e) {
//     var clickedItem = e.target.id;
//     alert("Hello " + clickedItem);

// }

// ----------------------------------------------------------

var theParent = document.querySelector("#parent");

theParent.addEventListener("click", doSomething, false);

function doSomething(e){
    console.log(e.currentTarget)
    // optimization tellling us the div wasn't click
    if(e.target !== e.currentTarget)    {
        var clickedItem = e.target.id;
        alert("Hello " + clickedItem);
    }
    // we don't want to propagate
    e.stopPropagation();
}