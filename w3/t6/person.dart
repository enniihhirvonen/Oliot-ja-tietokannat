class Person {
    late String firstName;
    late String lastName;
    late int _age;
    Person(String fname, String lname, int age) {
        firstName = fname;
        lastName = lname;
        _age = age;
    }
    int getAge() {
        return _age;
    }
    void ageUp() {
        _age += 1;
    }
    String getFullname() {
        return firstName + " " + lastName;
    }
    void printFullname() {
        print(getFullname());
    }
}