import java.util.*;

public class main{
    public static void main(String[] args) {
        //import pacakge
        Scanner sc = new Scanner(System.in);
        Random rnd = new Random();

        //The Random number
        int randomnumber = rnd.nextInt(0,101);

        //Using how many time
        int times = 0;

        //user input
        System.out.print("\nPlease write a write a number (0-100): ");
        int userinput = sc.nextInt();

        boolean running = true;
        while(running){
            if( userinput != randomnumber){
                System.out.println("Wrong number!");
                ++times;
                if(userinput < randomnumber){
                    System.out.print("\nThe number is bigger, Try again: ");
                    userinput = sc.nextInt();
                }
                else if(userinput > randomnumber){
                    System.out.print("\nThe number is smaller, Try again: ");
                    userinput = sc.nextInt(); 
                }
            }
            else{
                ++times;
                System.out.println("\nYou are correct!");
                System.out.println("You have been using: "+ times + " times!");
                running = false;
            }
        }

    }
}