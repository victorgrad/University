package constants;

import java.time.format.DateTimeFormatter;

public class Constants {
    public static final String SEPARATOR = ",";
    public static final DateTimeFormatter DATE_TIME_FORMATTER = DateTimeFormatter.ofPattern("yyyy-MM-dd");
    public static final DateTimeFormatter DATE_TIME_FORMATTER2 = DateTimeFormatter.ofPattern("yyyy-MM-dd hh:mm");
    public static final int MAXLENGTH = 64;
    public static final int SHOWING = 5;
    public static final String PENDINGREQUEST = "pending";
    public static final String ACCEPTEDREQUEST = "accepted";
    public static final String REJECTEDREQUEST = "rejected";
}
