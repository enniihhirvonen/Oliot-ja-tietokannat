#include <iostream>
#include "person.h"
using namespace std;
int main()
{
    cout << "Program starting.\n";
    cout << "Creating person...\n";
    Person p1 = Person("John", "Doe", 30);
    cout << "Person created.\n";
    cout << "Name: " << p1.getFullname() << "\n";
    cout << "Age: " << p1.getAge() << "\n";
    cout << "Person has now birthday...\n";
    p1.ageUp();
    int age = stoi(p1.getAge());
    cout << "New age: " << age << "\n";
    cout << "Program ending.\n";
    return 0;
}