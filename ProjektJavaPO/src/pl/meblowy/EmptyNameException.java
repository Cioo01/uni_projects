package pl.meblowy;

abstract class EmptyNameException extends Exception{}

class EmptyBoxException extends EmptyNameException{
    @Override
    public String toString(){
        return "You cannot leave empty box in name or material";
    }
}
