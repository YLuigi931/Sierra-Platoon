
// function doSomething(){
//     return Math.random() > 0.25
// }
// console.log(doSomething())

// let myPromise = new Promise( (resolve, reject) =>{
//     let success = doSomething()
//     success ? reject("fail"): resolve("It was a success")

// })

// myPromise.then( (data) =>{
//     console.log('Ha', data)
// }).catch( (error) =>{
//     console.log('fail')
// })
//-------------------------------------------------------------------------------------------

// let washDishes = () => {
//     return new Promise( (fulfill, reject ) =>{
//         setTimeout( () => {fulfill('we washed the dishes')}, 3000)
//     })
// }

// let pourCereal = (result) =>{
//     console.log(result)
//     return new Promise( (fulfill, reject ) =>{
//         setTimeout( () => {reject('pour cereal')}, 3000)
//     })
// }

// let pourMilk = (result) =>{
//     console.log(result)
//     return new Promise( (fulfill, reject ) =>{
//         setTimeout( () => {fulfill('pour milk')}, 4000)
//     })
// }

// let eat = () =>{
//     console.log('lets eat')
// }

// let goHungry = () => {

//     console.log(`Im Hungry`)
// }

// washDishes()
//     .then( (result) => pourCereal(result))
//     .then( (result) => {pourMilk(result)})
//     .then( eat)
//     .catch(goHungry)

//---------------------------------------------------------------------------------------

const promise1 = Promise.resolve(3); console.log('pour Cereal');
const promise2 = 42;console.log('pour milk');
const promise3 = new Promise((resolve, reject) => {
  setTimeout(resolve, 100, 'foo');console.log('eat breakfast');
});

Promise.all([promise1, promise2, promise3]).then((values) => {
  console.log(values);
});

