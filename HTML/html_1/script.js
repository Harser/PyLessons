let counter = null;
let num_row = null;
let k = 0;
let numbers = null;

window.onload = function() {
    counter = document.getElementById("counter");
    numbers = document.getElementById("numbers");
    num_row = document.getElementById("num_row");
};

function increase() {
    counter.innerText = ++k;
}

function decrease() {
    counter.innerText = --k;
}

function print_numbers() {
    let result = "";
    for (let i = 1; i <= 10; i++) {
        result += i.toString() + " ";
    }
    numbers.innerText = result;
}

function get_number(e) {
    e.preventDefault();
    let result = "";
    let val = +document.getElementById("num").value;
    for (let i = 1; i <= val; i++) {
        result += i.toString() + " ";
    }
    num_row.innerText = result;
}