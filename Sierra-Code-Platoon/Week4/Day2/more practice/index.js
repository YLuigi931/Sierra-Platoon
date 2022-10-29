pTag = document.getElementById('output')
console.log(pTag)

window.addEventListener('DOMContentLoaded',(event) => {
    console.log('DOM fully loaded and parsed');

    pTag = document.getElementById('output')
    console.log(pTag)
    pTag.innerHTML = "The newest New value set by JS!!!"
})