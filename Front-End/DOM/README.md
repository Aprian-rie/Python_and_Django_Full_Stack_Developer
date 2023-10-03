### Document Object Model
The DOM will allow us to interface our Javascript code to interact our Javascript
code to interact with HTML and CSS

Browsers will construct the DOM, which basically means storing all the HTML tags as
Javascript objects

We can see he DOM of any website. Go to a website and in the console type:
document

That will return the HTML text of the page. To see the actual objects use:
console.dir(document).

This DOM will allow us to use Javascript to interact with the web page.

The DOM is enormous, most developers won't use all the properties.

The common objects used will be covered.

### Events 
Listening for an event looks like this:

``myvariable.addEventListener(event, func);``

Example

```text
var head = document.querySelector('h1');
head.addEventListener("click", changeColor);
```
There are many possible events!

- Clicks
- Hovers
- Double Clicks
- Drags
- etc !

<a href="https://developer.mozilla.org/en-US/docs/Web/Events">Mozilla Link to the events</a>


