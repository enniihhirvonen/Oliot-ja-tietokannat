import 'person.dart';

class Main {
    Main() {
        print("Program starting.");
        print("Creating person...");
        var p1 = Person("John", "Doe", 30);
        print("Person created.");
        print("Name: ${p1.getFullname()}");
        print("Age: ${p1.getAge()}");
        print("Person has now birthday...");
        p1.ageUp();
        var age = p1.getAge();
        print("New age: ${age}");
        print("Program ending.");
    }
}

void main() {
    var app = Main();
}