#include <iostream>
using namespace std;

class Car
{
public:
    // class data
    string brand, model;
    int mileage = 0;

    // class function to drive the car
    void drive(int distance)
    {
        mileage += distance;
    }

    // class function to print variables
    void show_data()
    {
        cout << "Brand: " << brand << endl;
        cout << "Model: " << model << endl;
        cout << "Distance driven: " << mileage << " miles" << endl;
    }
};

int main()
{
    Car suv;
    Car sedan;
    Car van;
    return 0;
}
