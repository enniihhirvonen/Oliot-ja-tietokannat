<?php
class Person
{
    public $first_name;
    public $last_name;
    private $age;
    public function __construct($first_name, $last_name, $age)
    {
        $this->first_name = $first_name;
        $this->last_name = $last_name;
        $this->age = $age;
    }
    public function getAge(): int
    {
        return $this->age;
    }
    public function ageUp(): void
    {
        $this->age++;
    }
    public function getFullname(): string
    {
        return $this->first_name . " " . $this->last_name;
    }
    public function printFullname(): void
    {
        echo $this->getFullname();
    }
}

class Main {
    public function __construct() {
        echo "Program starting.\n";
        echo "Creating person...\n";
        $person = new Person("John", "Doe", 30);
        echo "Person created.\n";
        echo "Name: " . $person->getFullname() . "\n";
        echo "Age: " . $person->getAge() . "\n";
        echo "Person has now birthday...\n";
        $person->ageUp();
        $age = $person->getAge();
        echo "New age: " . $age . "\n";
        echo "Program ending.\n";
    }
}

$main = new Main();
?>