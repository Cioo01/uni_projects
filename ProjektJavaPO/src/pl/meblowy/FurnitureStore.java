package pl.meblowy;

import java.io.Serializable;
import java.util.ArrayList;

public class FurnitureStore implements Serializable {
    public ArrayList<Chair> chairs;
    public ArrayList<Table> tables;
    //public ArrayList<Object> ChairsAndTables;
    public FurnitureStore(){
        chairs = new ArrayList<Chair>();
        tables = new ArrayList<Table>();
        //ChairsAndTables = new ArrayList<Object>();
    }

    public void createFurniture(Object furniture, String name, String material, Integer weight, Integer price){
        String strFurniture = furniture.toString();

        if (strFurniture.equals("Chair")){
            Chair createdChair = new Chair(name, material, weight, price);
            chairs.add(createdChair);
            //ChairsAndTables.add((Object) createdChair);
        }
        else if(strFurniture.equals("Table")){
            Table createdTable = new Table(name, material, weight, price);
            tables.add(createdTable);
            //ChairsAndTables.add((Object) createdTable);
        }
    }
}
