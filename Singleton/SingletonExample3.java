class Singleton {
    private static Singleton instance = null;
    // constructor
    private Singleton() {}
    // verifying the unique instance
    public static synchronized Singleton getInstance() {
        if (instance == null) {
            instance = new Singleton();
        }
        return instance;
    }
    // method created to test the singleton instance
    protected static void TestInstance() {
        System.out.println("Method by Singleton Instance!");
    }
}

class Main {
    public static void main(String[] args) {
        Singleton sing = Singleton.getInstance();
        Singleton sing2 = Singleton.getInstance();
        if (sing == sing2) {
            System.out.println("Same Instance!");
            Singleton.TestInstance();
        } else {
            System.out.println("Different Instance!");
        }
    }
}
