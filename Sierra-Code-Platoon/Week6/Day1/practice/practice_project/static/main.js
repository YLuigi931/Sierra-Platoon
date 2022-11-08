console.log('HI there')

function add_student(event){
    // don't forget to add .value
    const first_name = document.getElementById('first_name').value
    const last_name = document.getElementById('last_name').value
    const email = document.getElementById('email').value

    // sender pass the info to back end. look at views.py
    // this makes a request to the backend to add this info
    axios
        .post('student/', {'first': first_name, 'last': last_name, 'email': email})
        .then( (response) => {
                console.log(response)
            }
        )

}

