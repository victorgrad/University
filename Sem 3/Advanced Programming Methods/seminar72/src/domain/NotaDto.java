package domain;

public class NotaDto {
    private double nota;
    private String studentName;
    private String temaID;
    private final String profesor;

    public NotaDto(double nota, String studentName, String temaID, String profesor) {
        this.nota = nota;
        this.studentName = studentName;
        this.temaID = temaID;
        this.profesor = profesor;
    }

    @Override
    public String toString() {
        return "NotaDto{" +
                "nota=" + nota +
                ", studentName='" + studentName + '\'' +
                ", temaID='" + temaID + '\'' +
                '}';
    }

    public double getNota() {
        return nota;
    }

    public void setNota(double nota) {
        this.nota = nota;
    }

    public String getStudentName() {
        return studentName;
    }

    public void setStudentName(String studentName) {
        this.studentName = studentName;
    }

    public String getTemaID() {
        return temaID;
    }

    public void setTemaID(String temaID) {
        this.temaID = temaID;
    }

    public String getProfesor() {
        return profesor;
    }
}
