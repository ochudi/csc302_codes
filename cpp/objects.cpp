// C++ Program to show the syntax/working of Objects as a part of Object Oriented Programming
#include <iostream>
using namespace std;

class Person
{
public:
    string name;
    int id;

public:
    void getdetails()
    {
        cout << "Name: " << name << endl;
        cout << "Id: " << id << endl;
    }
};

int main()
{
    Person p1; // p1 is a object
    p1.name = "John Doe";
    p1.id = 1234;
    p1.getdetails();
    return 0;
}