import bussiness.*;
import domain.Friendship;
import domain.Message;
import domain.User;
import domain.validators.FriendshipValidator;
import domain.validators.MessageValidator;
import domain.validators.UserValidator;
import domain.validators.Validator;
import repository.database.FriendshipRepo;
import repository.database.MessageRepo;
import repository.database.UserRepo;
import ui.UI;
import java.sql.SQLException;

public class Main {

    public static void main(String[] args) {
        /*
        todo:
                Request validator and repo
                validate input in SuperService for ReplyMessage
                use DTOs in SuperService as input parameters
                show names instead of usernames for messages?
         */

        try{
            UserRepo userRepository = new UserRepo("jdbc:postgresql://localhost:5432/ToySocialNetwork", "postgres", "postgres");
            FriendshipRepo friendshipRepository = new FriendshipRepo("jdbc:postgresql://localhost:5432/ToySocialNetwork", "postgres", "postgres");
            MessageRepo messageRepo = new MessageRepo("jdbc:postgresql://localhost:5432/ToySocialNetwork", "postgres", "postgres");

            Network userNetwork = new Network(userRepository, friendshipRepository);

            UserService userService = new UserService(userRepository, friendshipRepository);
            FriendshipService friendshipService = new FriendshipService(friendshipRepository, userRepository);
            MessageService messageService = new MessageService(messageRepo);

            Validator<Message> messageValidator = new MessageValidator();
            Validator<User> userValidator = new UserValidator();
            Validator<Friendship> friendshipValidator = new FriendshipValidator();

            SuperService superService = new SuperService(userNetwork, userService, friendshipService, messageService, userValidator, friendshipValidator, messageValidator);
            UI ui = new UI(superService);
            ui.run();
        }
        catch (SQLException err){
            err.printStackTrace();
        }
    }
}
