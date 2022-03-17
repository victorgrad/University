import java.util.ArrayList;
import java.util.List;
import java.util.function.Predicate;

public class Main {
    public static <E> void printList(List<E> list, Predicate<E> predicate){
        list.forEach(el->{
            if(predicate.test(el)){
                System.out.println(el);
            }
        });
    }

    public static void main(String[] args){
        List<Student> students = new ArrayList<Student>();
        students.add(new Student("Ana",9.8));
        students.add(new Student("Marius",10));
        students.add(new Student("Mihai",7.9));
        Predicate<Student> hasScholarship = student -> student.getGrade()>9;
        printList(students,hasScholarship);

        Predicate<Student> hasScholashipAndNameStartsWithA=hasScholarship.and(student -> student.getName().startsWith("A"));
        printList(students,hasScholashipAndNameStartsWithA);
    }

}
