const form = document.getElementById("folder-name-form");
const input = document.getElementById("folder-name");
const ul = document.getElementById("folder-ul");

function add() {
	const li = document.createElement("li");
	li.innerText = input.value;
	li.classList.add("list-group-item");
	ul.appendChild(li);
	input.value = "";
}

form.addEventListener("submit", function (event) {
	event.preventDefault();
	console.log(input.value);
	add();
})