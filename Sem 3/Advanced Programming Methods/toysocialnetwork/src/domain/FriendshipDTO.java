package domain;
import java.time.LocalDate;

public class FriendshipDTO {
    private final UserDTO user1;
    private final UserDTO user2;
    private final LocalDate date;

    /**
     * Class constructor
     * @param user1 UserDTO, an user
     * @param user2 UserDTO, another user
     * @param date LocalDateTime, the date of the friendship, can be null
     */
    public FriendshipDTO(UserDTO user1, UserDTO user2, LocalDate date){
        this.user1 = user1;
        this.user2 = user2;
        this.date = date;
    }

    /**
     * Returns the UserDTO object of the first user
     * @return UserDTO
     */
    public UserDTO getUser1() {
        return user1;
    }

    /**
     * Returns the UserDTO object of the second user
     * @return UserDTO
     */
    public UserDTO getUser2() {
        return user2;
    }

    /**
     * Reruns the date of the beginning of the friendship, can be null
     * @return LocalDateTime
     */
    public LocalDate getDate() {
        return date;
    }
}
