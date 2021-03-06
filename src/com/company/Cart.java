package com.company;

import java.util.ArrayList;
import java.util.List;
// Cart class
public class Cart {
    private String customer;
    private List<Item> items;

    public String getCustomer() {
        return customer;
    }

    public void setCustomer(String customer) {
        this.customer = customer;
    }

    public List<Item> getItems() {
        return items;
    }

    public Cart(String customer) {
        this.customer = customer;
        this.items = new ArrayList<>();
    }

    public void AddItem(Item i){
        items.add(i);
    }
//  Generates the cart's total
    public double Total(){
        double t = 0;
        for (Item i : this.items) {
            t += i.getTotal();
        }
        return t;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(String.format("%s's cart:\n", this.customer));
        for (Item i : this.items) {
            sb.append(i);
        }
        sb.append(String.format("\n Total: $%.2f", (float)(this.Total() / 100)));
        return sb.toString();
    }
}
