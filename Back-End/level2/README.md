Learning the advanced topics of python for Django application

## Scope
Python scope follows the LEGB Rule:

* Local
* Enclosing Function Locals
* Global
* Built In

*** 
Maelezo
****
## Object Oriented Programming
Is a way to use Python to create our own Objects.

### Adding Attributes and methods to a class
Attributes are characteristics of an objects while 
methods are the operations we can perform on the object.

```python
class Dog():
    def __init__(self):
        pass
```
Is the most basic special method you can have.
The self keyword is it tells that this method refers to itself
itself being the actual class object.

we add more attributes
```python
class Dog():
    def __init__(self, breed):
        self.breed = breed
```
This means whenever I create an instance of the dog class
I should add the breed argument
```python
mydog = Dog(breed = "Lab")
print(mydog.breed)
```
The output

```text
Lab
```
Just a recap
We have the init method that is called automatically
right after the object has been created

Once we initialize the object we call this method
automatically

Each attribute in the class definition begins with a
reference to the instance object which is the
``self`` keyword

The value is passed during the instatiation or the
initialization of the class itself.

Adding another attribute
```python
class Dog():
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name
        
mydog = Dog(breed="lab", name="Sam")
print(mydog.breed)
print(mydog.name)
        
```

output
```text
lab
Sam
```
The name on the right hand side of the equal sign of the ``self.name``
refers to the input name.

### Class Object Attributes
They are always the same for any instance
of the class

For a particular dog you may have different breeds or name
but all are mammals regardless of their breed or name.

What we can do in this case is add a ``class object attribute``
ity goes outside of the normal methods up top
```python
class Dog():
    # Class Object Attribute
    species = "mammal"
    
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name
mydog = Dog("lab", "Sammy")
print(mydog.species)
```
output
```text
mammal
```

### methods
Are functions defined inside the body of a class
they are used to perform operations with the
attribute of our objects.

They are essential in the encapsulation concept.
```python
class Circle():
    pi = 3.14

    def __init__(self, radius=1):
        # We initialize with the
        # default value of the raidus
        # If it is not provided it will be 1
        self.radius = radius
    # Method that calculates area
    def area(self):
        return self.radius * self.radius * Circle.pi
    # SELF key word is important as it tells the method
    # look at the objects radius and call it self.radius
    # Because pi is an object level attribute so we say Circle.pi
    
        
myc = Circle(3)
print(myc.area())
```
output
```text
28.26
```
We can redefine the radius as the attributes
can be changed
```text
myc.radius = 100
```
### Inheritance
Is a way to form new classes using older classes
that have already been defined


The newly formed classes are called derived classes
and the one derived from are called the base class

The importance of inheritance is code reuse and reduction
of complexity of a program.

Example
```python
class Animal():
    def __init__(self):
        print("Animal Created")
    
    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")

        
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")



mydog = Dog()
mydog.whoAmI()
mydog.eat()
```

You can add, override methods in the derived class
