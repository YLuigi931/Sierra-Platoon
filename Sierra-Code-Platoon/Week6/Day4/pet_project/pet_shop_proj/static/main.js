console.log('Hello')
// make sure to disable cache on browser developer to see axios

function addToCart(productID){
    console.log("added this item " + productID)

    console.log('axios')

    axios.post(`add-product/${productID}/`)
            .then((response) => {
                console.log(response.request.responseURL)
                newURL = response.request.responseURL
                // this allows the redirect to a another location(basicly manually adding href loaction)
                window.location.href = newURL
            })
}

