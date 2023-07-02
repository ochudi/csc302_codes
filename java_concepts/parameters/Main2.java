package java_concepts.parameters;

public class Main2 {
    int modelYear;
    String modelName;

    public Main2(int year, String name) {
        modelYear = year;
        modelName = name;
    }

    public static void main(String[] args) {
        Main2 myCar = new Main2(1969, "Mustang");
        System.out.println(myCar.modelYear + " " + myCar.modelName);
    }
}

// Outputs 1969 Mustang