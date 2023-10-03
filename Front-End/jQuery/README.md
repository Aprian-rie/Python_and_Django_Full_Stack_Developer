### jQuery
Learning Javascript and jQuery is learned in order to use them with Django on the next
lessons.

jQuery is a Javascript Library. It is just a large single .js file that has many pre-built methods
and objects that simplify the workflow.

Specifically interacting with the DOM and making HTTP requests (AJAX)

Previously we've learned how to interact with the DOM using "vanilla" javascript.
We used methods such as ``document.getElementById()`` and later we used methods such as 
``document.querySelector()``.

When jQuery was created, the more robust and convenient methods such as .querySelector() didn't
exist !

jQuery was created as a way to help simplify interactions with the DOM. One of its main
features is the use of ``$``

So how to get jquery? We have two options:

- Link a CDN hosted file (Like bootstrap)
- Download the .js file from jQuery's official website

Once you've connected the jQuery using the ``<script>`` tags in your HTML, then you can call
the specialized jQuery calls, to interact with the DOM.

#### How JQuery differs from "vanilla" javascript

```markdown
//jQuery
var divs = $('div');

$(el).css('border-width', '20px');

$(document).ready(function(){ //code });
```

```markdown
//Vanilla
var divs = document.querySelectorAll('div);

el.style.borderWidth = '20px';

if (document.readyState != 'loading'){
    fn();
} else {
    document.addEventListener('DOMContentLoaded', fn);
}
```
As it can be seen some situations are helped tremendously by jQuery while others may not
necessitate it.

Due to its massive popularity, it is still very important to understand it, because you will
run to it a lot in the real world!

### Basic jQuery
How to interact with the DOM with jQuery!


### jQuery Events

