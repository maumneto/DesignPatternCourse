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
    protected static void TestInstace() {
        System.out.println("Method by Singleton Instance!");
    }
}

class Main {
    public static void main(String[] args) {
        Singleton singleton = Singleton.getInstance();
        System.out.println(singleton);
        singleton.TestInstace();
        
        Singleton singleton2 = Singleton.getInstance();
        System.out.println(singleton2);
        singleton2.TestInstace();
    }
}
