public class Person {
    public String firstName;
    public String lastName;
    private int age;
    public Person(String fname, String lname, int age) {
        this.firstName = fname;
        this.lastName = lname;
        this.age = age;
    }
    public int getAge() {
        return this.age;
    }
    public void ageUp() {
        this.age++;
    }
    public String getFullname() {
        return this.firstName + " " + this.lastName;
    }
    public void printFullname() {
        System.out.println(this.getFullname());
    }
}