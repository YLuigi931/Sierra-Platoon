console.log("HELLO PAPA PLATOON!")
// Your function(s) should go here that will interact with the webpage or DOM

function msg() {
    alert("Hello world!");
}

function randomNumber() {
    console.log( Math.floor(Math.random() * 10));
}

function getInfo(){
    console.log(document.getElementById("info").innerHTML);
}

function ip(text){
    const texting = document.createTextNode(text);
    const ip = document.getElementById("ip");
    ip.appendChild(texting);
}

pTag = document.getElementById('ip')
console.log('before dom content loaded paragraph tag is ', pTag)


window.addEventListener(
    'click',
    (event) => console.log('something was clicked ', event.target.innerHTML)
)

window.addEventListener(
    'DOMContentLoaded', 
    (event) => {
        pTag = document.getElementById('output')
        console.log(pTag)

        console.log('DOM fully loaded and parsed');
        console.log(event.target.value)

        pTag.innerHTML = " THe Neweset New value set by JS!!!"

    }
);

