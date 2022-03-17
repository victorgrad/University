package bussiness;

import domain.*;
import domain.exceptions.DuplicateException;
import domain.exceptions.NotFoundException;
import domain.exceptions.ValidationException;
import domain.validators.Validator;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.*;
import java.util.List;
import java.util.function.Predicate;

/*
todo:
        use DTOs for input parameters
 */

public class SuperService {
    private final UserService userService;
    private final FriendshipService friendshipService;
    private final MessageService messageService;
    private final Validator<User> userValidator;
    private final Validator<Friendship> friendshipValidator;
    private final Validator<Message> messageValidator;
    private final Network userNetwork;

    /**
     * Class constructor
     * @param userNetwork, a Network object
     * @param userService, a UserService object
     * @param friendshipService, a FrienshipService object
     * @param messageService, a MessageService object
     * @param userValidator, a user validator
     * @param friendshipValidator, a friendship validator
     * @param messageValidator, a message validator
     */
    public SuperService(Network userNetwork,
                        UserService userService, FriendshipService friendshipService, MessageService messageService,
                        Validator<User> userValidator, Validator<Friendship> friendshipValidator,
                        Validator<Message> messageValidator){
        this.userService = userService;
        this.friendshipService = friendshipService;
        this.messageService = messageService;
        this.userValidator = userValidator;
        this.friendshipValidator = friendshipValidator;
        this.messageValidator = messageValidator;
        this.userNetwork = userNetwork;
    }

    /**
     * Creates an iterable of UserDTO objects that contain all the users
     * @return an iterable of UserDTO objects
     */
    public Iterable<UserDTO> getAllUsers(){
        Iterable<User> users = userService.getAllUsers();
        List<UserDTO> userDTOList = new ArrayList<>();
        for(User u: users){
            userDTOList.add(new UserDTO(u));
        }
        return userDTOList;
    }

    /**
     * Creates a new User object, validates it and adds it in the repository
     * @param userID string, a unique id for the user
     * @param firstname string, the firstname of the user
     * @param lastname string, the lastname of the user
     */
    public void addUser(String userID, String firstname, String lastname) {
        User user = new User(userID, firstname, lastname);
        userValidator.validate(user);
        userService.addUser(user);
    }

    /**
     * Searches if a user has the id userID and returns it
     * @param userID string, the id to be found
     * @return the user with the id userId
     * @throws NotFoundException if the user is not found
     */
    public UserDTO getUser(String userID) {
        return new UserDTO(userService.getUser(userID));
    }

    /**
     * Creates an iterable of FriendshipDTO objects that contain all the friendships
     * @return an iterable of FriendshipDTO objects
     */
    public Iterable<FriendshipDTO> getAllFriendships(){
        Iterable<Friendship> friendships = friendshipService.getAllFriendships();
        List<FriendshipDTO> friendshipDTOList = new ArrayList<>();
        for(Friendship f: friendships){
            UserDTO user1 = new UserDTO(userService.getUser(f.getId().getLeft()));
            UserDTO user2 = new UserDTO(userService.getUser(f.getId().getRight()));
            friendshipDTOList.add(new FriendshipDTO(user1, user2, f.getFriendshipDate()));
        }
        return friendshipDTOList;
    }

    /**
     * Searches if the users are friends
     * @param userID1 string, the id of a user
     * @param userID2 string, the id of another user
     * @return a FriendshipDTO object that contains information about the users and their friendship
     * @throws NotFoundException if the users don't exist or aren't friends
     */
    public FriendshipDTO getFriendship(String userID1, String userID2){
        Pair<String> friendshipID = new Pair<>(userID1, userID2);
        Friendship friendship = friendshipService.getFriendship(friendshipID);
        UserDTO user1 = new UserDTO(userService.getUser(friendship.getId().getLeft()));
        UserDTO user2 = new UserDTO(userService.getUser(friendship.getId().getRight()));

        return new FriendshipDTO(user1, user2, friendship.getFriendshipDate());
    }

    /**
     * Creates an iterable of Tuple of UserDTO objects and LocalDate objects that contain all the users that are friends with the user with the id userID and the dates of their friendships
     * @param userID string, the id of the user
     * @return an iterable af UserDTO objects
     * @throws NotFoundException if the user with the id userID is not found
     */
    public Iterable<Tuple<UserDTO,LocalDate>> getUserFriends(String userID) {
        List<Friendship> friendships=new ArrayList<Friendship>(friendshipService.getAllFriendships());
        List<Tuple<UserDTO,LocalDate>> friendsWithDates = new ArrayList<>();
        Predicate<Friendship> pFriend = x -> (x.getId().getLeft().equals(userID) || x.getId().getRight().equals(userID));

        friendships.stream()
                .filter(pFriend)
                .forEach(x ->{
                    Tuple<UserDTO,LocalDate> aux = new Tuple<>();
                    if(x.getId().getLeft().equals(userID)){
                        aux.setFirst(new UserDTO(userService.getUser(x.getId().getRight())));
                        aux.setSecond(x.getFriendshipDate());
                    }
                    else{
                        aux.setFirst(new UserDTO(userService.getUser(x.getId().getLeft())));
                        aux.setSecond(x.getFriendshipDate());
                    }
                    friendsWithDates.add(aux);
                });
        return friendsWithDates;
    }

    /**
     * Returns the friendships, of the user with the username userID, created in the specified month
     * @param userID string the id of the user
     * @param m String the number of the month
     * @return iterable that contains friends of the specified user
     */
    public Iterable<Tuple<UserDTO, LocalDate>> getUserFriendshipsFromMonth(String userID, String m){
        int month;
        try {
            month = Integer.parseInt(m);
        }catch (NumberFormatException err){
            throw new ValidationException("Invalid month");
        }

        if(month < 1 || month > 12){
            throw new ValidationException("Invalid month");
        }
        List<Tuple<UserDTO, LocalDate>> rez = new ArrayList<>();

        Set<Friendship> friendships = friendshipService.getAllFriendships();
        Predicate<Friendship> userPredicate = x -> (userID.equals(x.getId().getLeft()) || userID.equals(x.getId().getRight()));
        Predicate<Friendship> datePredicate = x -> (x.getFriendshipDate().getMonthValue() == month);
        Predicate<Friendship> friendshipPredicate = userPredicate.and(datePredicate);

        friendships.stream()
                .filter(friendshipPredicate)
                .forEach(x -> {
                    Tuple<UserDTO, LocalDate> friend = null;
                    if(x.getId().getLeft().equals(userID)){
                        UserDTO userDTO = new UserDTO(userService.getUser(x.getId().getRight()));
                        friend = new Tuple<UserDTO, LocalDate>(userDTO, x.getFriendshipDate());
                    }
                    else{
                        UserDTO userDTO = new UserDTO(userService.getUser(x.getId().getLeft()));
                        friend = new Tuple<UserDTO, LocalDate>(userDTO, x.getFriendshipDate());
                    }
                    rez.add(friend);
                });

        return rez;
    }

    /**
     * Adds a friendship between the users with the ids userID1 and userID2
     * @param userID1 string, the id of a user
     * @param userID2 string, the if of another user
     * @throws NotFoundException if the users are not found
     * @throws ValidationException if the friendship is not valid
     */
    public void addFriendship(String userID1, String userID2) {
        Friendship friendship = new Friendship(userID1, userID2, LocalDate.now());
        friendshipValidator.validate(friendship);
        friendshipService.addFriendship(friendship);
    }

    /**
     * Removes the user with the id userID
     * @param userID string the id of the user
     * @throws NotFoundException if the user does not exist
     */
    public void removeUser(String userID) {
        userService.removeUser(userID);
    }

    /**
     * Removes the friendship between the user with the ids userID1 and userID2
     * @param userID1 string, the id of a user
     * @param userID2 string, the id of another user
     * @throws NotFoundException if the users do not exist or are not friends
     */
    public void removeFriendship(String userID1, String userID2) {
        friendshipService.removeFriendship(new Pair<String>(userID1, userID2));
    }

    public void updateUser(String username, String firstname, String lastname){
        User user = new User(username, firstname, lastname);
        userValidator.validate(user);
        userService.updateUser(user);
    }

    /**
     * Computes the number of communities between users
     * @return the number of communities
     */
    public int numberOfCommunities(){
        return userNetwork.getConnexComponents().size();
    }

    /**
     * Finds the most sociable community: the community that contains the longest elementary path between its users
     * @return a tuple with the length of the path and the users in the community
     */
    public Tuple<Integer, List<UserDTO>> getMostSociableCommunity(){
        Tuple<Integer, List<String>> mostSociable = userNetwork.getMostSociableComponent();
        List<UserDTO> userDTOList = new ArrayList<>();

        for(String username: mostSociable.getSecond()){
            userDTOList.add(new UserDTO(userService.getUser(username)));
        }
        return new Tuple<>(mostSociable.getFirst(), userDTOList);
    }

    /**
     * Sends the message
     * @param from String - id of the user that sends the message
     * @param text String - the main body of the message
     * @param to String - a list of recipients separated by ","(comma) " "(space) ";"(semicolon)
     */
    public void sendMessage(String from, String text, String to){
        LocalDateTime localDateTime = LocalDateTime.now();
        Set<String> toSet = new HashSet<>(Arrays.asList(to.split("[,; ]+")));
        Message message = new Message(0L, from, text, localDateTime);
        message.setTo(toSet);
        messageValidator.validate(message);
        messageService.sendMessage(message);
    }

    /**
     * Replies to a message by sending a message to the person that wrote the initial one
     * @param from String - id of the user that sends the message
     * @param text String - the main body of the message
     * @param originalMessageId Long - id of the message which we are replying to
     */
    public void replyMessage(String from, String text, Long originalMessageId){
        //fixme: add validation for eligibility for sending a reply to this message
        LocalDateTime localDateTime = LocalDateTime.now();
        Message originalMessage = messageService.getMessage(originalMessageId);
        Set<String> toSet = new HashSet<>();
        toSet.add(originalMessage.getFrom());
        Message message = new Message(0L,from,text,localDateTime, originalMessageId);
        message.setTo(toSet);
        messageValidator.validate(message);
        messageService.sendMessage(message);
    }

    /**
     * Replies to a message by sending a message to all the users that received the initial one
     * @param from String - id of the user that sends the message
     * @param text String - the main body of the message
     * @param originalMessageId Long - id of the message which we are replying to
     */
    public void replyAllMessage(String from, String text, Long originalMessageId){
        //fixme: add validation for eligibility for sending a reply to this message
        LocalDateTime localDateTime = LocalDateTime.now();
        Message originalMessage = messageService.getMessage(originalMessageId);
        Set<String> toSet = new HashSet<>(originalMessage.getTo());
        toSet.add(originalMessage.getFrom());
        toSet.remove(from);
        Message message = new Message(0L,from,text,localDateTime, originalMessageId);
        message.setTo(toSet);
        messageValidator.validate(message);
        messageService.sendMessage(message);
    }

    /**
     * Returns the set of messages that make up the conversation
     * @param userId1 String, the id of the first user
     * @param userId2 String,  the id of the second user
     * @return Set<Message>
     * @throws NotFoundException - if there are no messages between the 2 users or the users don't exist
     */
    public Set<Message> getConversation(String userId1, String userId2){
        return messageService.getConversation(userId1,userId2);
    }

    /**
     * Returns the set of messages that were sent or received by a user
     * @param userId String, the id of the user
     * @return Set<Message>
     * @throws NotFoundException - if there are no messages sent or received by the user or the user doesn't exist
     */
    public Set<Message> getUserMessages(String userId) {
        return messageService.getUserMessages(userId);
    }

    /**
     * Saves a new friendship request from the first user
     * @param from String the username of the user sending te request
     * @param to String the username of the user receiving the request
     * @throws NotFoundException if one of the users does not exist
     * @throws DuplicateException if the users are already friends or a request that is not rejected already exists
     */
    public void addFriendRequest(String from, String to){
        friendshipService.addFriendshipRequest(from, to);
    }

    /**
     * Accepts the request sent by the first user to the second user
     * @param from String the username of the user sending te request
     * @param to String the username of the user receiving the request
     * @throws NotFoundException if the request is not found
     */
    public void acceptFriendRequest(String from, String to){
        friendshipService.acceptFriendshipRequest(from, to);
    }

    /**
     * Rejects the request sent by the first user to the second user
     * @param from String the username of the user sending te request
     * @param to String the username of the user receiving the request
     * @throws NotFoundException if the request is not found
     */
    public void rejectFriendRequest(String from, String to){
        friendshipService.rejectFriendRequest(from, to);
    }

    /**
     * Returns a list with all the requests that can be accepted by the user
     * @param userID String the username of the user
     * @return List that contains Tuples that contain in the first value the username of the user sending the request and in the second value the status of the request
     * @throws NotFoundException if the user does not exist
     */
    public List<Tuple<String, String>> getUserFriendRequests(String userID){
        return friendshipService.getUserFriendRequests(userID);
    }
}
