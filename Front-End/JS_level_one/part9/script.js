var fNamePrompt = prompt("Enter Your First Name")
var lNamePrompt = prompt("What is your Last Name")
var agePrompt= prompt("What is your age")
var heightPrompt = prompt("What is your height")
var petNamePrompt = prompt("What is your pet Name")

alert("Thank you so much for your Information")

// Four conditions





var fNameCond = false
var lNameCond = false
var ageCond  = false
var heightCond = false
var petNameCond = false

// Name condition

if (fNamePrompt[0] === lNamePrompt[0]) {
  fNameCond = true
}

// Age condition
if (agePrompt > 20 && agePrompt < 30) {
  ageCond = true
}

// Height condition
if (heightPrompt >= 170) {
  heightCond = true
}

// Pet condition
if (petNamePrompt[petNamePrompt.length - 1] === "y") {
  petNameCond = true
}

if (fNameCond && ageCond && heightCond && petNameCond){
  console.log("Welcome Spy !!");
}else {
  console.log("Pass along");
}
