package pl.meblowy;

import java.io.Serializable;

public class Furniture implements Serializable {
    protected String name;
    protected String material;

    public Furniture(String name, String material) {
        this.name = name;
        this.material = material;
    }

    public String returnName() {
        return this.name;
    }

    public String returnMaterial() {
        return this.material;
    }

}
