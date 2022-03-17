package socialnetwork.domain;

import java.time.LocalDateTime;


public class Prietenie extends Entity<Tuple<Long>>{

    LocalDateTime date;
    Stare stare1,stare2;

    public Prietenie() {
    }

    public Long getId1(){
        return super.getId().getLeft();
    }

    public Long getId2(){
        return super.getId().getRight();
    }

    public Stare getStare1() {
        return stare1;
    }

    public Stare getStare2() {
        return stare2;
    }

    public void setStare1(Stare stare1) {
        this.stare1 = stare1;
    }

    public void setStare2(Stare stare2) {
        this.stare2 = stare2;
    }

    /**
     *
     * @return the date when the friendship was created
     */
    public LocalDateTime getDate() {
        return date;
    }
}
