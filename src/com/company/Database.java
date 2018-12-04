package com.company;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Dictionary;
import java.util.Hashtable;
import java.util.List;

public class Database {
    private Dictionary<String, Item> items;

    public Dictionary<String, Item> getItems() {
        return items;
    }

    public void setItems(Dictionary<String, Item> items) {
        this.items = items;
    }

    public Database(String fileName) throws FileNotFoundException {
        this.items = new Hashtable<>();
        BufferedReader br = new BufferedReader(new FileReader(fileName));
        try {
            String cur;
            br.readLine();
            while ((cur = br.readLine()) != null){
                String split[] = cur.split(",");
                this.items.put(split[0].toLowerCase(),new Item(split[0].toLowerCase(), Integer.parseInt(split[1]),Integer.parseInt(split[2])));
            }
        }
        catch (IOException ex){
            System.out.println(ex.getLocalizedMessage());
        }
    }

    public void RemoveItem(String name) throws NullPointerException{
        this.items.remove(name);
    }
}
