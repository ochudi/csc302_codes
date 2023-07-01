// C++ Program to show the syntax/working of Objects as a part of Object Oriented Programming
#include <iostream>
using namespace std;

class Person
{
    char name[20];
    int id;

public:
    void getdetails()
    {
        cout << "Name: " << name << endl;
    }
};

int main()
{
    Person p1; // p1 is a object

    return 0;
}