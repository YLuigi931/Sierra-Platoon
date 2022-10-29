

const showGreeting = (event) => {
    event.preventDefault();
    const nameInput = document.getElementById("input-name");
    const nameValue = nameInput.value;
    // console.log(nameInput);
    const anotherChild = document.createElement("div");
    anotherChild.innerText = nameValue
    // console.log(nameValue);
    
    const displayName = document.getElementById("output");
    // displayName.innerHTML = nameValue;
    displayName.appendChild(anotherChild);
    
  };