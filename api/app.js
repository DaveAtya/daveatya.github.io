const button = document.querySelector(".container button");
const jokeText = document.querySelector("#setup");
const jokeText2 = document.querySelector("#punchline");

button.addEventListener('click', getJoke);

async function getJoke(){
    const res = await fetch("https://official-joke-api.appspot.com/random_joke")
    const jokedata = await res.json()
    console.log(jokedata)
    jokeText.innerHTML = jokedata.setup
    jokeText2.innerHTML = jokedata.punchline
}