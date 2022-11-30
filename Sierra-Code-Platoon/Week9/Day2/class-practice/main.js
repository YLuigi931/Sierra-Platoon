
function wait(wait_time_in_ms){
    let startTime = new Date().getTime()
    console.log(startTime)

    while(new Date().getTime() < startTime + wait_time_in_ms);
}

// console.log('hi')

// wait(5000)
// console.log('hello')
// wait(6000)
// console.log('world')

// timer1 = setTimeout(() => console.log('Hello', 7000))
// timer2 = setTimeout(() => console.log('world', 5000))

intervalID = setInterval(() => {console.log('in interval')}, 3000)

setTimeout(() => clearInterval(intervalID),4000)

