package domain;

public class Student extends Entity{
    private int group;
    private String name;

    public Student(int group, String name) {
        this.group = group;
        this.name = name;
    }

    public void setGroup(int group) {
        this.group = group;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getGroup() {
        return group;
    }

    public String getName() {
        return name;
    }

    @Override
    public String toString() {
        return super.toString()+" "+ name +" "+String.valueOf(group);
    }
}
