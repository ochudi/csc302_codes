#include <iostream>
using namespace std;

// base class
class Vehicle
{
public:
    string brand;

    void show_brand()
    {
        cout << "Brand: " << brand << endl;
    }
};

// derived class
class Car : public Vehicle
{
public:
    string model;

    void show_model()
    {
        cout << "Model: " << model << endl;
    }
};

int main()
{
    // create an object of Car class
    Car my_car;

    // initialize variables of my_car
    my_car.brand = "Honda";
    my_car.model = "Accord";

    // display variables of my_car
    my_car.show_brand();
    my_car.show_model();

    return 0;
}
