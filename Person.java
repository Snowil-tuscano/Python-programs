public class Person {
    private String name;
    private int age;

    // Constructor
    public  Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Getter for name
    public String getName() {
        return name;
    }

    // Getter for age
    public int getAge() {
        return age;
    }

    public static void main(String[] args) {
        // Creating an instance of Person
        Person person = new Person("John", 30);

        // Accessing fields using getters
        System.out.println("Name: " + person.getName());
        System.out.println("Age: " + person.getAge());
    }
}