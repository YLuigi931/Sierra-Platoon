var hover = document.querySelector("#container")
// check the documentation on 'mouseenter' and 'mouseleave'
hover.addEventListener('mouseenter', () =>
    hover.innerHTML = "Mouse enter");

hover.addEventListener('mouseleave', () =>
    hover.innerHTML = "Mouse leave");