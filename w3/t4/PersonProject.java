public class PersonProject {
    public static void main(String args[]) {
        System.out.println("Program starting.");
        System.out.println("Creating person...");
        Person my_person = new Person("John", "Doe", 30);
        System.out.println("Person created.");
        System.out.println("Name: " + my_person.getFullname());
        System.out.println("Age: " + my_person.getAge());
        System.out.println("Person has now birthday...");
        my_person.ageUp();
        int age = my_person.getAge();
        System.out.println("New age: " + age);
        System.out.println("Program ending.");
    }
}