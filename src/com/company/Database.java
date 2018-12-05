package com.company;

import java.io.*;
import java.util.*;
// database class
public class Database {
    private Dictionary<String, Item> items;

    public Dictionary<String, Item> getItems() {
        return items;
    }

    public void setItems(Dictionary<String, Item> items) {
        this.items = items;
    }
//    Constructor. Reads in the database information from the file specified
    public Database(String fileName) throws FileNotFoundException {
        this.items = new Hashtable<>();
        BufferedReader br = new BufferedReader(new FileReader(fileName));
        try {
            String cur;
            br.readLine();
            while ((cur = br.readLine()) != null){
                String split[] = cur.split(",");
                this.items.put(split[0].toLowerCase(),new Item(split[0].toLowerCase(),
                        Integer.parseInt(split[1].trim()),Integer.parseInt(split[2].trim())));
            }
        }
        catch (IOException ex){
            System.out.println(ex.getLocalizedMessage());
        }
    }

    public void RemoveItem(String name) throws NullPointerException{
        this.items.remove(name);
    }
// to string method
    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        Enumeration<Item> it = this.items.elements();
        while (it.hasMoreElements()) {
            Item i = it.nextElement();
            sb.append(i + "\n");
        }
        return sb.toString();
    }
//  Writes the database to the file
    public void writeDatabase(String fileName) throws IOException {
        BufferedWriter br = new BufferedWriter(new FileWriter(fileName));
        try {
            br.write("item_name,quantity,price\n");
            Enumeration<Item> it = this.items.elements();
            while (it.hasMoreElements()) {
                Item i = it.nextElement();
//                System.out.println(i);
                br.write(i.getName() + "," + i.getQuantity()
                        + "," + i.getPrice() + "\n");
            }
        }
        catch (IOException ex){
            System.out.println(ex.getLocalizedMessage());
        }
        br.close();
    }
}
