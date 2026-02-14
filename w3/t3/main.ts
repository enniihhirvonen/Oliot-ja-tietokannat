class Person {
    public first_name: string;
    public last_name: string;
    private age: number;
    constructor(fname: string, lname: string, age: number) {
        this.first_name = fname;
        this.last_name = lname;
        this.age = age;
    }
    getAge() {
        return this.age;
    }
    ageUp() {
        this.age++;
    }
    getFullname() {
        return this.first_name + " " + this.last_name;
    }
    printFullname() {
        console.log(this.getFullname())
    }
}

class Main {
    constructor() {
        console.log('Program starting.');
        console.log('Creating person...');

        var person = new Person('John', 'Doe', 30);
        console.log('Person created.');
        console.log('Name: ' + person.getFullname());
        console.log('Age: ' + person.getAge());

        console.log('Person has now birthday...');
        person.ageUp();
        var age = person.getAge();
        console.log('New age: ' + age);

        console.log('Program ending.');
    }
}

const app = new Main();