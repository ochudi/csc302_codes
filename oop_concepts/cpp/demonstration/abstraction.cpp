lass Car
{
private:
    // class data
    int speed;

    // class function
    void show_car_status()
    {
        if (speed != 0)
            cout << "The car is being driven." << endl;
        else
            cout << "The car is stationary." << endl;
    }
};
