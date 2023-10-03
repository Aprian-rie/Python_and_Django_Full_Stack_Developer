// Restart Game button
var restart = document.querySelector("#rbtn")

// Grabs all the squares
var squares = document.querySelectorAll('td')

// Clear all the squares
function clearBoard() {
  for (var i = 0; i < squares.length; i++) {
    squares[i].textContent = ''
  }
}


restart.addEventListener('click', clearBoard);

// Check the square marker
function changeMarker(){
  if(this.textContent === ''){
    this.textContent = 'X'
  }else if (this.textContent === 'X') {
    this.textContent = 'O'
  }else {
    this.textContent = '';
  }
}


// For Loop to add event listeners to all the squares
for (var i = 0; i < squares.length; i++) {
  squares[i].addEventListener('click', changeMarker)
}