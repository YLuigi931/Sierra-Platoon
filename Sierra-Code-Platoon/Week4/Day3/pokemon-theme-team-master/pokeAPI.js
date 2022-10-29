



function roll(){
    random_number = rand()
    getPokemon(random_number)
    pokeName = getName(random_number)
    console.log(pokeName)
}

function rand(){
    return Math.floor(Math.random() * 100)
}

const getName = async (id) => {
    const response = await axios.get(`https://pokeapi.co/api/v2/pokemon/${id}`)
    console.log(response.data.name)
}

const getInput = (event) => {
    event.preventDefault();
    const nameInput = document.getElementById("input-name");
    console.log(nameInput.innerText)
    const nameValue = document.createTextNode(nameInput);

    const displayName = document.getElementById("output");
    displayName.appendChild(nameValue);
}
    

const getPokemon  = async (id) => {
    const response = await axios.get(`https://pokeapi.co/api/v2/pokemon/${id}`)
    console.log(response.data.name)
    // console.log('you requested ' + response.data.name)
    // for (let item in response.data){
    //     console.log(item)
    //     console.log(typeof(item))
    // }
    console.log(response)
    imageURL = response.data.sprites.other['official-artwork'].front_default
    // console.log(imageURL)

    imageHolder = document.getElementById("pokemon_image")
    console.log(imageHolder)
    imageHolder.src = imageURL

    // ability = response.data.abilities[0].ability
    // console.log(ablity)
    // abilityURL = ability.url

    // const abilityResponse = await axios.get(abilityURL)
    // console.log(abilityResponse)
    }
let pokeName = ""



// getPokemon('ditto')
// getPokemon('charmander')