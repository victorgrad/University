package domain;

public class UserDTO {
    private final String username;
    private final String firstname;
    private final String lastname;

    /**
     * Class constructor
     * @param user User, an User object
     */
    public UserDTO(User user){
        username = user.getId();
        firstname = user.getFirstName();
        lastname = user.getLastName();
    }

    /**
     * Returns the id of the user
     * @return String
     */
    public String getUsername() {
        return username;
    }

    /**
     * Returns the firstname of the user
     * @return String
     */
    public String getFirstname() {
        return firstname;
    }

    /**
     * Returns the lastname of the user
     * @return String
     */
    public String getLastname() {
        return lastname;
    }
}
