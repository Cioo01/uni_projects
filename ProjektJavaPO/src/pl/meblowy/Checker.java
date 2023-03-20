package pl.meblowy;

public class Checker {
    static String returnBoxText(String text) throws EmptyBoxException{
        if (text.equals("")){
            throw new EmptyBoxException();
        }
        return text;
    }
}
