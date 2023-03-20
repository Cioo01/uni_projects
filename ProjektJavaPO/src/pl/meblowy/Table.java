package pl.meblowy;

import java.io.Serializable;

public class Table extends Furniture implements Serializable {
    private Integer tableWeight;
    private Integer tablePrice;

    public Table(String name, String material, Integer tableWeight, Integer tablePrice) {
        super(name, material);
        this.tableWeight = tableWeight;
        this.tablePrice = tablePrice;
    }

    Integer returnTableWeight(){
        return this.tableWeight;
    }

    Integer returnTablePrice(){
        return this.tablePrice;
    }
}
