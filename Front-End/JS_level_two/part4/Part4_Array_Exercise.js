// PART 4 ARRAY EXERCISE
// This is  a .js file with commented hints, its optional to use this.

// Create Empty Student Roster Array
// This has been done for you!
var roster = []

// Create the functions for the tasks

// ADD A NEW STUDENT

// Create a function called addNew that takes in a name
// and uses .push to add a new student to the array
function addNew(name) {
  roster.push(name);
}


// REMOVE STUDENT

// Create a function called remove that takes in a name
// Finds its index location, then removes that name from the roster

// HINT: http://stackoverflow.com/questions/5767325/how-to-remove-a-particular-element-from-an-array-in-javascript
//
function remove(name) {
  nameIndex = roster.indexOf(name)
  roster.splice(nameIndex, 1)
}

// DISPLAY ROSTER

// Create a function called display that prints out the roster to the console.
function display() {
  console.log(roster);
}


// Start by asking if they want to use the web app
var useWebApp = prompt("Would you like to use the web app ? y/n ")
var wantToUse = false
if (useWebApp === "y"){
  wantToUse = true
}
// Now create a while loop that keeps asking for an action (add,remove, display or quit)
while (wantToUse) {
  // Use if and else if statements to execute the correct function for each command.
  var action = prompt("Please select an action add, remove, display or quit")
  if (action === "add"){
    var addName = prompt("What name would you like to add?")
    addNew(addName)
  }else if (action === "display") {
    display()
  }else if (action === "remove") {
    remove(addName)
  }else if (action === "quit") {
    wantToUse = false
  }else{
    alert("Wrong Input !!")
  }
}
