package bussiness;


import domain.Friendship;
import domain.Message;
import domain.Pair;
import domain.exceptions.DuplicateException;
import domain.exceptions.NotFoundException;
import repository.database.MessageRepo;

import java.util.Set;

public class MessageService {
    private final MessageRepo messageRepository;

    /**
     * Class constructor
     * @param messageRepo - instance of MessageRepo
     */
    public MessageService(MessageRepo messageRepo) {
        this.messageRepository = messageRepo;
    }

    /**
     * Adds the message in the repository
     * @param message - a valid message object
     */
    public void sendMessage(Message message){
        messageRepository.save(message);
    }

    /**
     * Returns the Message object for the Message id provided
     * @param messageID - a Long
     * @return an instance of Message
     * @throws NotFoundException - if the user aren't friends
     */
    public Message getMessage(Long messageID){
        Message found = messageRepository.findOne(messageID);
        if(found == null){
            throw new NotFoundException("Message not found");
        }
        return found;
    }

    /**
     * Returns an iterable container that contains all the messages
     * @return - an iterable container
     */
    public Set<Message> getAllMessages(){
        return messageRepository.findAll();
    }

    /**
     * Returns the set of messages that were sent or received by a user
     * @param userId String, the id of the user
     * @return Set<Message>
     * @throws NotFoundException - if there are no messages sent or received by the user or the user doesn't exist
     */
    public Set<Message> getUserMessages(String userId){
        Set<Message> found = messageRepository.findUserMessages(userId);
        if(found.isEmpty())
            throw new NotFoundException("Messages not found");
        return found;
    }

    /**
     * Returns the set of messages that make up the conversation
     * @param userId1 String, the id of the first user
     * @param userId2 String,  the id of the second user
     * @return Set<Message>
     * @throws NotFoundException - if there are no messages between the 2 users or the users don't exist
     */
    public Set<Message> getConversation(String userId1, String userId2){
        Set<Message> found = messageRepository.findConversation(userId1,userId2);
        if(found.isEmpty())
            throw new NotFoundException("Conversation not found");
        return found;
    }


}
