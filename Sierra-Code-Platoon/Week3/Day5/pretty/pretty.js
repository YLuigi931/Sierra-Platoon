// Home hover
var hover1 = document.querySelector("#one")

// check the documentation on 'mouseenter' and 'mouseleave'
hover1.addEventListener('mouseenter', () => {
    // hover.innerHTML = "Mouse enter"
    hover1.style.color = "black";
    hover1.style.backgroundColor = "red";
});

hover1.addEventListener('mouseleave', () => {
    // hover.innerHTML = "Mouse leave"
    hover1.style.color = "white",
    hover1.style.backgroundColor = "black"
});

hover1.removeEventListener('mouseenter', hover1)

// About hover
var hover2 = document.querySelector("#two")

hover2.addEventListener('mouseenter', () => {
    // hover.innerHTML = "Mouse enter"
    hover2.style.color = "black";
    hover2.style.backgroundColor = "red";
});

hover2.addEventListener('mouseleave', () => {
    // hover.innerHTML = "Mouse leave"
    hover2.style.color = "white",
    hover2.style.backgroundColor = "black"
    
});

// Services hover

// Contact hover

// Feedback hover


