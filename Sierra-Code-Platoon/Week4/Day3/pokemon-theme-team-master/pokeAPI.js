


 const getPokemon  = async (id) => {
        const response = await axios.get(`https://pokeapi.co/api/v2/pokemon/${id}`)
        console.log('you requested ' + response.data.name)
    
        ability = response.data.abilities[0].ability
        abilityURL = ability.url
    
        const abilityResponse = await axios.get(abilityURL)
        console.log(abilityResponse)
    }


getPokemon('ditto')
// getPokemon('charmander')