package bussiness;

import domain.Pair;
import domain.User;
import domain.exceptions.DuplicateException;
import domain.exceptions.NotFoundException;
import repository.database.FriendshipRepo;
import repository.database.UserRepo;

public class UserService {
    private final UserRepo userRepository;
    private final FriendshipRepo friendshipRepository;

    /**
     * Class constructor
     * @param userRepository - instance of UserRepository
     */
    public UserService(UserRepo userRepository, FriendshipRepo friendshipRepository){
        this.userRepository = userRepository;
        this.friendshipRepository = friendshipRepository;
    }

    /**
     * Returns the user with the same id as userID
     * @param userID - a user id
     * @return the user with the id userID
     * @throws NotFoundException if the user doesn't exist
     */
    public User getUser(String userID){
        User found =  userRepository.findOne(userID);
        if(found == null){
            throw new NotFoundException("User not found");
        }
        return found;
    }

    /**
     * Adds the user user in repository
     * @param user - a valid user
     * @throws DuplicateException - if a user with the same id already exists in repository
     */
    public void addUser(User user){
        if(userRepository.exists(user.getId())){
            throw new DuplicateException("User already exists");
        }
        userRepository.save(user);
    }

    /**
     * removes from repository the user with the id userID
     * @param userID - the id of the user to be removed
     * @throws NotFoundException if the user doesn't exist
     */
    public void removeUser(String userID){
        if(!userRepository.exists(userID)){
            throw new NotFoundException("User not found");
        }
        userRepository.delete(userID);
    }

    /**
     * returns an ietrable container with all the users in the repository
     * @return - an iterable container
     */
    public Iterable<User> getAllUsers(){
        return userRepository.findAll();
    }

    public void updateUser(User user){
        if(!userRepository.exists(user.getId())){
            throw new NotFoundException("User not found");
        }
        userRepository.update(user);
    }
}
