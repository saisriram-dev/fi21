Polymorphism is a core concept in object oriented programming where the same interface or method name can behave in different ways depending on the object that uses it. 
The word comes from Greek roots meaning “many forms,” which is fitting because one action can take multiple shapes in execution.
In practice, polymorphism allows different classes to define their own version of a method with the same name. 

For example, a base class called Shape might define a method named area(). A Circle class and a Rectangle class can both implement area(), but each calculates the result using a different formula. 
When the program calls area(), the correct version runs based on the object type, not just the reference name.
There are two common types of polymorphism. 

Compile time polymorphism is achieved through method overloading, where multiple methods share the same name but differ in parameters. Runtime polymorphism is achieved through method overriding, where a subclass provides a specific implementation of a method already defined in its parent class.
Polymorphism improves flexibility and scalability. It lets developers write code that works with general types while allowing specific behavior underneath. This reduces conditional logic and makes systems easier to extend, like adding new instruments to an orchestra without rewriting the entire score.