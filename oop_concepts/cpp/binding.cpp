// C++ Program to Demonstrate the Concept of Dynamic binding with the help of virtual function
#include <iostream>
using namespace std;

class Base
{
public:
    void call_Function() // function that call print
    {
        print();
    }
    void print() // the display function
    {
        cout << "Printing the Base class Content" << endl;
    }
};

class Derived : public Base // Derived inherit a publicly
{
public:
    void print() // Derived's display
    {
        cout << "Printing the Derived class Content" << endl;
    }
};

int main()
{
    Base object;             // Creating Base's pbject
    object.call_Function();  // Calling call_Function
    Derived object2;         // creating Derived object
    object2.call_Function(); // calling call_Function for Derived object
    return 0;
}