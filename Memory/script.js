const grid_container = document.querySelector('.grid-container');
const input = document.querySelector('#input');
const button = document.querySelector('.button');
const clock = document.querySelector('.time');
const taken = document.querySelector('.cards');
let grid_items = [];
let selectedButtons = 0;
let cardstaken = 0;
let interval;
let s = 0;

function shuffleArray(array) {
    for (var i = array.length - 1; i > 0; i--) {
        var j = Math.floor(Math.random() * (i + 1));
        var temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
    return array;
}

let click = false;

function handleClick(e) {
    if (e.target.classList.contains('active') && !click) {
        if (selectedButtons < 1) {
            e.target.classList += ' selected-grid-item';
            selectedButtons++;
        } else if (selectedButtons == 1) {
            e.target.classList += ' selected-grid-item';
            var selected_items = document.querySelectorAll('.selected-grid-item');

            if (selected_items[0].innerHTML == selected_items[1].innerHTML) {
                for (let i = 0; i < selected_items.length; i++) {
                    selected_items[i].classList.remove('active');
                    selected_items[i].removeEventListener('click', handleClick);
                }
                cardstaken += 2;
                taken.innerHTML = `Cards taken: ${cardstaken}`;
            }
            click = true;
            setTimeout(function () {
                for (let i = 0; i < selected_items.length; i++) {
                    selected_items[i].classList.remove('selected-grid-item');
                    click = false;
                }
            }, 700);
            selectedButtons = 0;
            if (cardstaken == input.value * 2) {
                clearInterval(interval);
                let score = 0;
                let t;
                if (s <= 500) t = 1000 / Math.pow(1000, s/ 500);
                score = (t * (input.value / 5)) / 20;
                alert(`You earned: ${Math.round(score)} points`);
            }
        }
    }
}

function flipInterval(array) {
    for (let i = 0; i < array.length; i++) {
        array[i].classList.remove('selected-grid-item');
    }
}

function FilterFound(element) {
    return element != selected_items[0] && element != selected_items[1];
}

function AddButtons() {
    clearInterval(interval);
    s = 0;
    interval = setInterval(Clock, 1000);
    while (grid_container.firstChild) {
        grid_container.removeChild(grid_container.lastChild);
    }
    grid_items = [];
    for (let i = 0; i < input.value; i++) {
        var item = document.createElement('div');
        item.textContent = i + 1;
        item.classList += "grid-item active";
        item.style.width = `${15 / Math.sqrt(input.value)}vw`;
        item.style.height = `${15 / Math.sqrt(input.value)}vw`;
        item.style.lineHeight = `${15 / Math.sqrt(input.value)}vw`;

        var item2 = document.createElement('div');
        item2.textContent = i + 1;
        item2.classList += "grid-item active";
        item2.style.width = `${15 / Math.sqrt(input.value)}vw`;
        item2.style.height = `${15 / Math.sqrt(input.value)}vw`;
        item2.style.lineHeight = `${15 / Math.sqrt(input.value)}vw`;

        grid_items.push(item, item2);
    }

    shuffleArray(grid_items).forEach(element => {
        grid_container.appendChild(element);
        element.addEventListener('click', handleClick);
    });
}
function Clock() {
    s++;
    clock.innerHTML = `Elapsed time: ${timedisplay(parseInt(s / 60))}:${timedisplay(s % 60)}`;
}
function timedisplay(time) {
    var timeString = time + "";
    if (timeString.length < 2) {
        return "0" + timeString;
    } else {
        return timeString;
    }
}
input.addEventListener('change', main);
button.addEventListener('click', main)
function main() {
    AddButtons();
    grid_items = [];
    selectedButtons = 0;
    click = false;
    cardstaken = 0;
    taken.innerHTML = `Cards taken: ${cardstaken}`;
    s = 0;
    clock.innerHTML = `Elapsed time: ${timedisplay(parseInt(s / 60))}:${timedisplay(s % 60)}`;
}