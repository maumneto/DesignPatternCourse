import java.util.ArrayList;
import java.util.List;
/**
 * @author Maurício Moreira Neto.
 * @version 1.0.0
 * This example presents a design pattern called Observer. 
*/

/**
 * Abstract class of Observer
 * attribute: an object of Subject
 * abstract method: update
*/
abstract class Observer {
    protected Subject subject;
    public abstract void update();
}

/**
     * Class Subject
     * This class receives the Observer objects the emails of each object
     * it is responsable to notify all abservers attached
*/
class Subject {
    private List<Observer> observers = new ArrayList<Observer>();

    public boolean isEven(int number) {
        boolean is_even = true;
        if (number % 2 != 0) {
            is_even = false;
        }
        return is_even;
    }

    public void attach(Observer observer) {
        observers.add(observer);
    }

    public void detach(Observer observer) {
        observers.remove(observer);
    }

    public void notifyAllAttached() {
        for (Observer observer: observers) {
            observer.update();
        }
    }
}

/**
 * Class ObserverSenderEmail
 * This class extends the Observer and implement the update method.
*/
class ObserverSenderEmail extends Observer {
    private List<String> listEmails = new ArrayList<String>();
    // constructor
    public ObserverSenderEmail(Subject subject) {
        this.subject = subject;
        this.subject.attach(this);
    }

    public void getEmail() {
        for (String email: listEmails) {
            System.out.println(email);
        }
    }

    public void addEmail(String email) {
        listEmails.add(email);
    }

    @Override
    public void update() {
        System.out.println("A new event occured!");
        System.out.println("Sending e-mails to: ");
        getEmail();
        System.out.println(" ");
    }
}

/**
 * Class ObserverSenderSMS
 * This class extends the Observer and implement the update method.
*/
class ObserverSenderSMS extends Observer {
    private List<String> listOfNumbers = new ArrayList<String>();
    // constructor
    public ObserverSenderSMS(Subject subject) {
        this.subject = subject;
        this.subject.attach(this);
    }

    public void getNumbers() {
        for (String telNumber: listOfNumbers) {
            System.out.println(telNumber);
        }
    }

    public void addTelNumber(String telNumber) {
        listOfNumbers.add(telNumber);
    }

    @Override
    public void update() {
        System.out.println("A new event occured!");
        System.out.println("Sending SMS to: ");
        getNumbers();
        System.out.println(" ");
    }
}

/**
 * ObserverExample1
*/
class ObserverExample1 {
    public static void main(String[] args) {
        Subject subject1 = new Subject();
        // create the object 1 e 2
        ObserverSenderEmail ob1 = new ObserverSenderEmail(subject1);
        ObserverSenderSMS ob2 = new ObserverSenderSMS(subject1);
        // add email in ob1
        ob1.addEmail("mauricio@provedor.com");
        ob1.addEmail("joao@provedor.com");
        // add SMS in ob2
        ob2.addTelNumber("0418599887766");
        ob2.addTelNumber("0418599112233");

        for (int i = 0; i < 5; i++) {
            if (subject1.isEven(i) == true) {
                subject1.notifyAllAttached();
                System.out.println("----");
                System.out.println(" ");
            }
        }
    }    
}
