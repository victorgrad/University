package bussiness;

import domain.Friendship;
import domain.Pair;
import domain.Tuple;
import domain.User;
import domain.exceptions.DuplicateException;
import domain.exceptions.NotFoundException;
import domain.exceptions.RepoException;
import repository.database.FriendshipRepo;
import repository.database.UserRepo;
import constants.Constants;

import java.time.LocalDate;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class FriendshipService {
    private final FriendshipRepo friendshipRepository;
    private final UserRepo userRepository;

    /**
     * Class constructor
     * @param friendshipRepository - instance of FriendshipRepository
     */
    public FriendshipService(FriendshipRepo friendshipRepository, UserRepo userRepository){
        this.friendshipRepository = friendshipRepository;
        this.userRepository = userRepository;
    }

    /**
     * Returns the Friendship object for the users with the id-s contained in the pair
     * @param friendshipID - a pair of 2 user id-s
     * @return an instance of Friendship
     * @throws NotFoundException - if the user aren't friends
     */
    public Friendship getFriendship(Pair<String> friendshipID){
        Friendship found = friendshipRepository.findOne(friendshipID);
        if(found == null){
            throw new NotFoundException("Friendship not found");
        }
        return found;
    }

    /**
     * Returns an iterable container that contains all the friendships
     * @return - an iterable container
     */
    public Set<Friendship> getAllFriendships(){
        return friendshipRepository.findAll();
    }

    /**
     * removes from repository the Friendship object with the id equal to friendshipID
     * @param friendshipID - the id of the friendship to be removed
     * @throws NotFoundException - if the friendship doesn't exist
     */
    public void removeFriendship(Pair<String> friendshipID){
        if(!friendshipRepository.exists(friendshipID)){
            throw new NotFoundException("Friendship not found");
        }
        friendshipRepository.delete(friendshipID);
        if(friendshipRepository.getRequestStatus(friendshipID.getLeft(), friendshipID.getRight()) != null)
            friendshipRepository.removeFriendRequest(friendshipID.getLeft(), friendshipID.getRight());
        if(friendshipRepository.getRequestStatus(friendshipID.getRight(), friendshipID.getLeft()) != null)
            friendshipRepository.removeFriendRequest(friendshipID.getRight(), friendshipID.getLeft());
    }

    /**
     * adds the friendship in the repository
     * @param friendship - a valid friendship object
     * @throws DuplicateException - if the friendship already exists
     */
    public void addFriendship(Friendship friendship){
        if(friendshipRepository.exists(friendship.getId())){
            throw new DuplicateException("Friendship already exists");
        }
        friendshipRepository.save(friendship);
    }

    public Iterable<User> getUserFriends(String username){
        Iterable<String> friends = friendshipRepository.getUserFriends(username);
        Set<User> users = new HashSet<>();

        for(String f: friends){
            users.add(userRepository.findOne(f));
        }

        return users;
    }

    /**
     * Saves a new friendship request from the first user
     * @param from String the username of the user sending te request
     * @param to String the username of the user receiving the request
     * @throws NotFoundException if one of the users does not exist
     * @throws DuplicateException if the users are already friends or a request that is not rejected already exists
     */
    public void addFriendshipRequest(String from, String to){
        if(!userRepository.exists(from)){
            throw new NotFoundException("First user not found");
        }
        if(!userRepository.exists(to)){
            throw new NotFoundException("Second user not found");
        }
        if(friendshipRepository.exists(new Pair<>(from, to))){
            throw new DuplicateException("Already friends");
        }

        String exists = friendshipRepository.getRequestStatus(to, from);
        if(exists != null){
            switch (exists){
                case Constants.PENDINGREQUEST -> throw new DuplicateException("Second user already sent a request");
                case Constants.ACCEPTEDREQUEST -> throw new DuplicateException("Already friends");
            }
        }

        String status = friendshipRepository.getRequestStatus(from, to);
        if(status == null) {
            friendshipRepository.addFriendshipRequest(from, to);
        } else {
            switch (status){
                case Constants.ACCEPTEDREQUEST -> throw new DuplicateException("Request is already accepted");
                case Constants.PENDINGREQUEST -> throw new DuplicateException("Request is already pending");
                default -> friendshipRepository.updateRequest(from, to, Constants.PENDINGREQUEST);
            }
        }
    }

    /**
     * Accepts the request sent by the first user to the second user
     * @param from String the username of the user sending te request
     * @param to String the username of the user receiving the request
     * @throws NotFoundException if the request is not found
     */
    public void acceptFriendshipRequest(String from, String to){
        String status = friendshipRepository.getRequestStatus(from, to);
        if(status == null) {
            throw new NotFoundException("Request not found");
        } else {
            switch (status){
                case Constants.ACCEPTEDREQUEST -> throw new DuplicateException("Request is already accepted");
                case Constants.REJECTEDREQUEST -> throw new DuplicateException("Request is already rejected");
                default -> {
                    friendshipRepository.updateRequest(from, to, Constants.ACCEPTEDREQUEST);
                    friendshipRepository.save(new Friendship(from, to, LocalDate.now()));
                }
            }
        }
    }

    /**
     * Rejects the request sent by the first user to the second user
     * @param from String the username of the user sending te request
     * @param to String the username of the user receiving the request
     * @throws NotFoundException if the request is not found
     */
    public void rejectFriendRequest(String from, String to){
        String status = friendshipRepository.getRequestStatus(from, to);
        if(status == null) {
            throw new NotFoundException("Request not found");
        } else {
            switch (status){
                case Constants.ACCEPTEDREQUEST -> throw new DuplicateException("Request is already accepted");
                case Constants.REJECTEDREQUEST -> throw new DuplicateException("Request is already rejected");
                default -> friendshipRepository.updateRequest(from, to, Constants.REJECTEDREQUEST);
            }
        }
    }

    /**
     * Returns a list with all the requests that can be accepted by the user
     * @param userID String the username of the user
     * @return List that contains Tuples that contain in the first value the username of the user sending the request and in the second value the status of the request
     * @throws NotFoundException if the user does not exist
     */
    public List<Tuple<String, String>> getUserFriendRequests(String userID){
        if(!userRepository.exists(userID)){
            throw new NotFoundException("User not found");
        }
        return friendshipRepository.getFriendRequests(userID);
    }
}
