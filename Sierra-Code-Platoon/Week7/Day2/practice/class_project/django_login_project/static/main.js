console.log('Hello there')

const userInfo={
    username: 'test4',
    email: 'test4@gmail.com',
    password: 'password',
};

axios
    .post('/signup/', userInfo)
    .then((response) => {
        console.log(response)
    })