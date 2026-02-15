#include <iostream>
#include <string>
using namespace std;
class Person
{
private:
    int age;

public:
    string first_name;
    string last_name;
    Person(string fname, string lname, int age)
    {
        this->first_name = fname;
        this->last_name = lname;
        this->age = age;
    }
    string getAge()
    {
        return to_string(this->age);
    }
    void ageUp()
    {
        this->age++;
    }
    string getFullname()
    {
        return this->first_name + " " + this->last_name;
    }
    void printFullname()
    {
        cout << getFullname();
    }
};