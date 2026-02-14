const Person = require('./person');

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