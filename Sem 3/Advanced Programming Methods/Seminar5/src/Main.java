import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args){
        Area<Circle> circleArea = circle -> Math.PI* Math.pow(circle.getRadius(), 2);
        List<Circle> circleList = new ArrayList<Circle>();
        circleList.add(new Circle(2));
        circleList.add(new Circle(4));
        circleList.add(new Circle(6));
        printArie(circleList,circleArea);

        Area<Square> squareArea = square -> Math.pow(square.getL(),2);
        List<Square> squareList = new ArrayList<Square>();
        squareList.add(new Square(2));
        squareList.add(new Square(3));
        squareList.add(new Square(4));
        printArie(squareList,squareArea);
    }

    public static <E> void printArie(List<E> l, Area<E> f) {
        for(E el: l){
            System.out.println(f.computeArea(el));
        }
    }

}
