package com.company;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.*;

import static java.lang.System.exit;

public class Main {

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        System.out.print("What is your name? ");
        String name = sc.nextLine();
        Cart cart1 = new Cart(name);
        long startTime = System.nanoTime();
        Database db = new Database("db.csv");
        long endTime = System.nanoTime();

        long duration = (endTime - startTime);  //divide by 1000000 to get milliseconds.
        System.out.println("Read file: " + duration / 1000000 + "ms");

        printMenu();
        String input;
        while (!(input = sc.nextLine()).toLowerCase().equals("q")){
            switch(input.toLowerCase()){
                case "a":
                    AddItem(cart1, db, sc);
                    System.out.println("_________________________");
                    break;
                case "b":
                    ModCart(cart1, db, sc);
                    System.out.println("_________________________");
                    break;
                case "c":
                    System.out.println(cart1);
                    System.out.println("_________________________");
                    break;
                case "d":
                    System.out.println(db);
                    System.out.println("_________________________");
                    break;
                case "e":
                    System.out.println(cart1);
                    System.out.println(String.format("Thank you, %s! Have a nice day!", cart1.getCustomer()));
                    startTime = System.nanoTime();
                    db.writeDatabase("db.csv");
                    endTime = System.nanoTime();
                    duration = (endTime - startTime);  //divide by 1000000 to get milliseconds.
                    System.out.println("Write file: " + duration / 1000000 + "ms");
                    exit(0);
                    break;
                default:
                    System.out.println("Please enter one of the above options");
                    break;
            }
            System.out.println();
            printMenu();
        }
    }

    private static void PrintDatabase(Database db) {
        Enumeration<Item> it = db.getItems().elements();
        while (it.hasMoreElements()) {
            Item i = it.nextElement();
            System.out.println(i);
        }
    }

    private static void ModCart(Cart cart1, Database db, Scanner sc) {
        System.out.println(cart1);
        System.out.println("What item would you like to modify?");
        String iName = sc.nextLine();
        Item i = null;
        int iter;
        for (iter = 0; iter < cart1.getItems().size(); iter++){
            if (cart1.getItems().get(iter).getName().equals(iName.toLowerCase())) {
                i = cart1.getItems().get(iter);
                break;
            }
        }
        if (i == null){
            System.out.println("Sorry, that item is not in the cart.");
        }
        else{
            System.out.println("How many would you like to remove from your cart?");
            int iQuan = Integer.parseInt(sc.nextLine());
            while (iQuan > i.getQuantity()){
                System.out.println(String.format("Sorry, you do not have that many in the cart)",
                        iQuan, i.getQuantity()));
                iQuan = Integer.parseInt(sc.nextLine());
            }
            if (iQuan == i.getQuantity())
                cart1.getItems().remove(i);
            else
                cart1.getItems().get(iter).setQuantity(i.getQuantity() - iQuan);
            db.getItems().get(iName.toLowerCase()).setQuantity(db.getItems().get(iName.toLowerCase()).getQuantity() + iQuan);
        }

    }

    private static void AddItem(Cart cart, Database db, Scanner sc) {
        System.out.println("Please enter the name of the object you would like to purchase: ");
        String iName = sc.nextLine();
        Item i = db.getItems().get(iName.toLowerCase());
        if (i == null){
            System.out.println("Sorry, that item is not in the database.");
        }
        else{
            System.out.println(i);
            System.out.println("How many would you like buy?: ");
            int iQuan = Integer.parseInt(sc.nextLine());
            while (iQuan > i.getQuantity()){
                System.out.println(String.format("Sorry, we do not have enough stock of that (you wanted %d, we have %d in stock)",
                        iQuan, i.getQuantity()));
                iQuan = Integer.parseInt(sc.nextLine());
            }

            db.getItems().get(iName.toLowerCase()).setQuantity(i.getQuantity() - iQuan);
            cart.AddItem(new Item(iName, iQuan, i.getPrice()));
        }
    }

    public static void printMenu(){
        System.out.println("Please select an option: ");
        System.out.println("a) Add an item to the cart\tb) Modify cart contents");
        System.out.println("c) Get cart total\td) View stock counts");
        System.out.println("e) Checkout\tq) Quit");
    }
}
