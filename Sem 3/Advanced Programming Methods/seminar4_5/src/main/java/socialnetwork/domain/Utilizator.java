package socialnetwork.domain;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class Utilizator extends Entity<Long>{
    private String userName;
    private String firstName;
    private String lastName;
    //private List<Utilizator> friends;

    public Utilizator(String userName,String firstName, String lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
        //friends = new ArrayList<>();
    }

    public String getUserName() {
        return userName;
    }

    public void setUserName(String userName) {
        this.userName = userName;
    }

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

//    public List<Utilizator> getFriends() {
//        return friends;
//    }
//
//    public void addFriend(Utilizator prieten){
//        friends.add(prieten);
//    }
//
//    public void removeFriend(Utilizator prieten){
//        friends.remove(prieten);
//    }

    @Override
    public String toString() {
        String rez = "Utilizator{" +
                "firstName='" + firstName + '\'' +
                ", lastName='" + lastName + '\'' +
                ", friends=";
//        for(Utilizator utilizator:friends){
//            rez = rez + '\'' + utilizator.firstName + " " + utilizator.lastName+ '\''+ ", ";
//      }
        rez+='}';
        return rez;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Utilizator)) return false;
        Utilizator that = (Utilizator) o;
        return getFirstName().equals(that.getFirstName()) &&
                getLastName().equals(that.getLastName());
//                getFriends().equals(that.getFriends());
    }

    @Override
    public int hashCode() {
        return Objects.hash(getFirstName(), getLastName());
    }
}