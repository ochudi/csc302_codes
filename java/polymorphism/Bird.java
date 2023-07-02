package java.polymorphism;

class Bird {
    public void fly() {
        System.out.println("The bird is flying.");
    }

    public void fly(int height) {
        System.out.println("The bird is flying " + height + " feet high.");
    }

    public void fly(String name, int height) {
        System.out.println("The " + name + " is flying " + height + " feet high.");
    }
}

class TestBirdStatic {
    public static void main(String[] args) {
        Bird myBird = new Bird();

        myBird.fly();
        myBird.fly(10000);
        myBird.fly("eagle", 10000);
    }
}

// Dynamic Polymorphism
class Animal {
    public void eat() {
        System.out.println("This animal eats insects.");
    }
}

class Bird1 extends Animal {
    public void eat() {
        System.out.println("This bird eats seeds.");
    }
}

class TestBirdDynamic {
    public static void main(String[] args) {
        Animal myAnimal = new Animal();
        myAnimal.eat();
        Bird1 myBird = new Bird1();
        myBird.eat();
    }
}
