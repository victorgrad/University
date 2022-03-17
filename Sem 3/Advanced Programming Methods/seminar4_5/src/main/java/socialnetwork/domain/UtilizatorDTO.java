package socialnetwork.domain;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class UtilizatorDTO {
    private String firstName;
    private String lastName;
    private List<String> friends;

    public UtilizatorDTO(String firstName, String lastName, List<Utilizator> list) {
        this.firstName = firstName;
        this.lastName = lastName;
        friends = new ArrayList<>();
        for(Utilizator utilizator:list){
            friends.add(utilizator.getFirstName() + " " +utilizator.getLastName());
        }
    }

    public String getFirstName() {
        return firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public List<String> getFriends() {
        return friends;
    }

    @Override
    public String toString() {
        String rez = "Utilizator{" +
                "firstName='" + firstName + '\'' +
                ", lastName='" + lastName + '\'' +
                ", friends=";
        for(String utilizator:friends){
            rez = rez + '\'' + utilizator+ '\''+ ", ";
        }
        rez+="}\n";
        return rez;

    }
}
