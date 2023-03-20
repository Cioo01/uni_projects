package pl.meblowy;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class FStoreFileManager {
    final String cPath;
    final String tPath;
    public FStoreFileManager(String cPath, String tPath){
        this.cPath = cPath;
        this.tPath = tPath;
    }

    public void saveToFile(FurnitureStore FStore) throws IOException{
        ObjectOutputStream outputStream = null;
        try{
            outputStream = new ObjectOutputStream(new FileOutputStream(cPath));
            outputStream.writeObject(FStore.chairs);
            outputStream = new ObjectOutputStream(new FileOutputStream(tPath));
            outputStream.writeObject(FStore.tables);
        } finally{
            if(outputStream != null){
                outputStream.close();
            }
        }

    }
    public FurnitureStore readFromFile() throws IOException, ClassNotFoundException{
        ObjectInputStream inputStream = null;
        try{
            inputStream = new ObjectInputStream(new FileInputStream(cPath));
            FurnitureStore inputFS = new FurnitureStore();
            inputFS.chairs = (ArrayList<Chair>) inputStream.readObject();
            inputStream = new ObjectInputStream(new FileInputStream(tPath));
            inputFS.tables = (ArrayList<Table>) inputStream.readObject();
            return inputFS;
        }finally {
            if(inputStream != null){
                inputStream.close();
            }
        }
    }
}
