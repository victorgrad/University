import domain.Nota;
import domain.NotaDto;
import domain.Student;
import domain.Tema;

import java.lang.reflect.Array;
import java.time.LocalDate;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.Map;
import java.util.function.Predicate;
import java.util.stream.Collectors;

///[5:06 PM] GEORGE GIOSAN
//    6. Temele de la o anumita grupa (parametru), sortate descrescator in functie de numarul studentilor care au primit nota la acea materie

public class Main {
    private static List<Student> getAllStundets(){
        Student st1 = new Student(123,"Gion");
        Student st2 = new Student(124,"Maguna");
        Student st3 = new Student(124,"Duio");
        st1.setId(1l);
        st2.setId(2l);
        st3.setId(3l);
        return Arrays.asList(st1,st2,st3);
    }

    private static List<Tema> getAllTeme(){
        Tema t1 = new Tema("21","dudu");
        Tema t2 = new Tema("22","dada");
        Tema t3 = new Tema("23","dede");
        return Arrays.asList(t1,t2,t3);
    }

    private static List<Nota> getAllNote(List<Student> studenti, List<Tema> teme){
        return Arrays.asList(new Nota("profesor1",studenti.get(0),teme.get(0),8d, LocalDate.of(2021,12,1)),
                new Nota("profesor1",studenti.get(1),teme.get(0),9d, LocalDate.of(2021,11,2)),
                new Nota("profesor2",studenti.get(2),teme.get(0),7d, LocalDate.of(2021,12,2)),
                new Nota("profesor2",studenti.get(0),teme.get(1),8.5d, LocalDate.of(2021,10,1)),
                new Nota("profesor1",studenti.get(0),teme.get(2),5d, LocalDate.of(2021,12,1)),
                new Nota("profesor3",studenti.get(1),teme.get(2),7d, LocalDate.of(2021,12,11)),
                new Nota("profesor3",studenti.get(1),teme.get(1),9d, LocalDate.of(2021,11,12)),
                //new Nota("profesor2",studenti.get(2),teme.get(2),6d, LocalDate.of(2020,4,11)),
                new Nota("profesor3",studenti.get(2),teme.get(1),7d, LocalDate.of(2021,12,11))
                );
    }

    /**
     * creati/afisati o lista de obiecte NotaDto apoi filtrati dupa un anumit profesor
     * (toate notele acordate de un anumit profesor)
     * (toate notele acordate de un anumit profesor, la o anumita grupa)
     * GENERALIZARE: FILTRU COMPUS
     */
    private static void afisare(List<Nota> note,String profesor,int grupa){
        Predicate<Nota> pGrupa= x->x.getStudent().getGroup()==grupa;
        Predicate<Nota> pProfesor=x->x.getProfesor().equals(profesor);
        Predicate<Nota> pGrupaProfesor=pGrupa.and(pProfesor);
        note.stream().filter(pGrupaProfesor)
                .map(x->new NotaDto(x.getValue(),x.getStudent().getName(),x.getTema().getId(),x.getProfesor()))
                .forEach(x-> System.out.println(x));
    }



    public static void main(String[] args){
        List<Student> studenti = getAllStundets();
        List<Tema> teme = getAllTeme();
        List<Nota> note = getAllNote(studenti,teme);
        //afisare(note,"profesor1",123);
        ex_seminar9(note,124);

    }

    private static void ex_seminar9(List<Nota> grades, int group){
        List<Nota> filteredGrades = grades.stream().filter(x -> x.getStudent().getGroup() == group).collect(Collectors.toList());
        filteredGrades.stream().
                collect(Collectors.groupingBy(Nota::getTema, Collectors.counting()))
                .entrySet()
                .stream()
                .sorted(Map.Entry.comparingByValue(Comparator.reverseOrder()))
                .forEach(System.out::println);
    }
}
