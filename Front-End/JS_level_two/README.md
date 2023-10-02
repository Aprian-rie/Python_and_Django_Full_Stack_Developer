## JavaScript Level Two
So far we covered only the basics of Javascript, time for some advanced concepts

I'll be covering 

- Functions
- Arrays
- Objects

### Functions
We use the function keyword to indicate that we have a function
The General sytax for a function

```commandline
function name(parameter1, parameter2){
    // code to be executed
}
```
### Arrays
Arrays will allow us to store various basic data types in a sequence, so we can then later access
them as needed.

```commandline
var countries = ["Tanzania", "Kenya", "Rwanda"]

var countries = ["USA",
                 "Germany",
                 "China"]
```
Accessing elements in an array:

Each element in an array is in a fixed sequence position, they are in order and can be called by
their position.

```python
countries[2] gives me a value of Rwanda for the first case and for the second case 
    it will be China
    
```
#### Immutability vs Mutability
Immutable means the value can not change, in our case strings are immutable that is they can
not change

While mutable means the value can be reassigned, that is change upon being reassigned to a new
value, in our case arrays are mutable

In Javascript an array can take mixed data types

``var mixed = [true,20,"string"]`` is allowed

pop and push are the common array methods used to delete and add elements of an array respectively
they add or delete the last element.

##### Iterating an array
for loop way
```markdown
for(var i = 0; i<arr.length;i++)
    {
        console.log(arr[i]);
    }
```

```javascript
for (letter of arr){
    console.log(letter);
}
```

calling  a function for every element in an array
```javascript
arr.forEach(alert);
// Calls alert 3 times for every element there
```
### Objects
JS Objects are hash-tables, they store information in a key-value pair.

In other languages this is sometimes also called a dictionary. Unlike an array JS Object does
NOT retain any ordering.

The name "Object" can sometimes be confusing when coming from another language because it sounds
so generic, so keep that in mind.

The typical JS object is in the form

``{key1: "Value one", key2: "value two", .....}``

You then can access values through their corresponding key.

#### Object Methods
Object methods are essentially functions that are inside of an Object.

Example
```python
var carInfo = {
    make: "Toyota",
    year: 1990,
    model: "Camry",
    carAlert: function(){
        alert("We've got a car here!")
    }
};
```

More realistically you will want to use key value pais from the object itself, in that case
you use the special <strong>this</strong> keyword.

The this keyword acts differently depending on the situation. For a JS Object, the this is set
to the object the method is called on.

For example:
```javascript
var myObj = {
    prop: 37,
    reportProp: function(){
        return this.prop;
    }
};
console.log(myObj.reportProp()); //logs 37
```




