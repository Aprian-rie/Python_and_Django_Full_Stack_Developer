var fName = "Jose"
var lName = "Johnson"
var age  = "26"
var height = "175"
var petName = "Sammy"

var fNamePrompt = prompt("Enter Your First Name")
var lNamePrompt = prompt("What is your Last Name")
var agePrompt= prompt("What is your age")
var heightPrompt = prompt("What is your height")
var petNamePrompt = prompt("What is your pet Name")

if (fName === fNamePrompt  && lName === lNamePrompt  && age === agePrompt && height === heightPrompt && petName === petNamePrompt) {
  console.log("Welcome Comrade! You've passed the Spy Test");
}else {
  console.log("Sorry, nothing to see here");
}
