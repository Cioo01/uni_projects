package pl.meblowy;

import java.io.Serializable;

public class Chair extends Furniture implements Serializable {
    private Integer chairWeight;
    private Integer chairPrice;

    public Chair(String name, String material, Integer chairWeight, Integer chairPrice) {
        super(name, material);
        this.chairWeight = chairWeight;
        this.chairPrice = chairPrice;
    }

    Integer returnChairWeight(){
        return this.chairWeight;
    }

    Integer returnChairPrice(){
        return this.chairPrice;
    }

}
