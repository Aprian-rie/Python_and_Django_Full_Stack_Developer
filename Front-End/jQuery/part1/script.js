// $('h1').click(function () {
//   console.log("There was a click");
// })

// $('li').click(function () {
//   console.log("Any list was clicked");
// })
//
// $('h1').click(function () {
//   $(this).text("I was changed")
// })


// link = https://api.jquery.com/category/events/

// Key Press

// $('input').eq(0).keypress(function () {
//   $('h3').toggleClass('turnBlue')
// })

// $('input').eq(0).keypress(function (event) {
//   if (event.which === 13) {
//     $('h3').toggleClass('turnBlue')
//   }
// })

// on() method

// $('h1').on('dblclick', function(){
//   $(this).toggleClass('turnBlue');
//   console.log('turnblue');
// })

// $('h1').on('mouseenter', function(){
//   $(this).toggleClass('turnBlue');
//   console.log('turnblue');
// })

// Animations and effects

// $('input').eq(1).on('click', function () {
//   $('.container').fadeOut(3000)
// })

$('input').eq(1).on('click', function () {
  $('.container').slideUp(3000)
})

// https://api.jquery.com/category/effects/
