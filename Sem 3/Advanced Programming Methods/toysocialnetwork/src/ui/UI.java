package ui;

import constants.Constants;
import domain.FriendshipDTO;
import domain.Message;
import domain.Tuple;
import domain.UserDTO;
import domain.exceptions.DuplicateException;
import domain.exceptions.NotFoundException;
import domain.exceptions.RepoException;
import domain.exceptions.ValidationException;
import bussiness.SuperService;

import javax.sound.midi.Soundbank;
import java.time.LocalDate;
import java.util.*;

public class UI {
    private final SuperService superService;
    Scanner console;

    public UI(SuperService superService){
        this.superService = superService;
        console = new Scanner(System.in);
    }

    private void printUser(UserDTO userDTO){
        System.out.print("'" + userDTO.getUsername() + "': " + userDTO.getFirstname() + " " + userDTO.getLastname());
    }

    private void printFriendship(FriendshipDTO friendshipDTO){
        printUser(friendshipDTO.getUser1());
        System.out.print(" | ");
        printUser(friendshipDTO.getUser2());
        System.out.print(" | ");
        if(friendshipDTO.getDate() != null){
            System.out.print(friendshipDTO.getDate().format(Constants.DATE_TIME_FORMATTER));
        }
    }

    private void showUsers(){
        System.out.println("Users:");

        superService.getAllUsers().forEach(user -> {
            printUser(user);
            System.out.println();
        });
    }

    private void showFriends(){
        System.out.print("Username: ");
        String userID = console.nextLine();
        UserDTO user = superService.getUser(userID);

        if(user == null){
            System.out.println("User not found");
            return;
        }

        printUser(user);
        System.out.println();
        System.out.print("Friends: \n");
        superService.getUserFriends(userID).forEach(tuple -> {
            printUser(tuple.getFirst());
            System.out.println(" | " + tuple.getSecond().format(Constants.DATE_TIME_FORMATTER));

        });
        System.out.println();
    }

    private void showFriendsByMonth(){
        System.out.print("Username: ");
        String userID = console.nextLine();
        System.out.print("Month: ");
        String month = console.nextLine();

        UserDTO user = superService.getUser(userID);

        if(user == null){
            System.out.println("User not found");
            return;
        }

        printUser(user);
        System.out.println();
        System.out.print("Friends: \n");

        superService.getUserFriendshipsFromMonth(userID, month)
                .forEach(x -> {
                    printUser(x.getFirst());
                    System.out.println(" " + x.getSecond().format(Constants.DATE_TIME_FORMATTER));
                });
        System.out.println();
    }

    private String[] readUserData(){
        String[] data = new String[3];
        System.out.print("Username: ");
        data[0] = console.nextLine();
        System.out.print("Firstname: ");
        data[1] = console.nextLine();
        System.out.print("Lastname: ");
        data[2] = console.nextLine();

        return data;
    }

    private void addUser(){
        String[] userData = readUserData();
        superService.addUser(userData[0], userData[1], userData[2]);
        System.out.println("User added successfully");
    }


    private void updateUser(){
        String[] userData = readUserData();
        superService.updateUser(userData[0], userData[1], userData[2]);
        System.out.println("User updated successfully");
    }

    private void removeUser(){
        String userID;
        System.out.print("Username: ");
        userID = console.nextLine();

        superService.removeUser(userID);
        System.out.println("User removed successfully");
    }

    private void addFriendship(){
        String userID1, userID2;
        System.out.print("First username: ");
        userID1 = console.nextLine();
        System.out.print("Second username: ");
        userID2 = console.nextLine();

        superService.addFriendship(userID1, userID2);
        System.out.println("Befriended users successfully");
    }

    private void removeFriendship(){
        String userID1, userID2;
        System.out.print("First username: ");
        userID1 = console.nextLine();
        System.out.print("Second username: ");
        userID2 = console.nextLine();

        superService.removeFriendship(userID1, userID2);
        System.out.println("Removed friendship between users successfully");
    }

    private void numberOfCommunities(){
        System.out.println("There are " + superService.numberOfCommunities() + " communities");
    }

    private void mostSociableCommunity(){
        Tuple<Integer, List<UserDTO>> community = superService.getMostSociableCommunity();
        System.out.println("The most sociable community contains a path of " + community.getFirst() + " users");
        System.out.println("The users in this community are: ");
        community.getSecond().forEach(u -> System.out.print(u + "; "));
        System.out.println();
    }

    private void showAllFriendships(){
        System.out.println("Friendships:");
        superService.getAllFriendships().forEach(x -> {printFriendship(x);
            System.out.println();
        });
    }

    private void showFriendship(){
        String userID1, userID2;
        System.out.print("First username: ");
        userID1 = console.nextLine();
        System.out.print("Second username: ");
        userID2 = console.nextLine();

        printFriendship(superService.getFriendship(userID1, userID2));
        System.out.println();
    }

    private void sendMessage(){
        String from, to, text;
        System.out.print("From: ");
        from = console.nextLine();
        System.out.println("To (separated by spaces, commas or semicolons): ");
        to = console.nextLine();
        System.out.println("Message: ");
        text = console.nextLine();

        superService.sendMessage(from, text, to);
    }

    private void printMessage(Message message){
        System.out.println("From: " + message.getFrom());
        System.out.print("To: ");
        message.getTo().forEach(username -> System.out.print(username + "; "));
        System.out.println();

        System.out.print(message.getMessageDateTime().format(Constants.DATE_TIME_FORMATTER2));
        System.out.println(" \"" + message.getMessage() + "\"");
    }

    private void printReplyMessage(Message message, Message replying){
        System.out.println("From: " + message.getFrom());
        System.out.print("To: ");
        message.getTo().forEach(username -> System.out.print(username + "; "));
        System.out.println();

        System.out.println("Replying to message:");
        System.out.println("--------------------------------");
        printMessage(replying);
        System.out.println("--------------------------------");

        System.out.print(message.getMessageDateTime().format(Constants.DATE_TIME_FORMATTER2));
        System.out.println(" \"" + message.getMessage() + "\"");
    }

    private void printMessages(Set<Message> messages) {
        List<Message> toShow = new ArrayList<>(messages);
        int start = toShow.size() - Constants.SHOWING;
        int stop = toShow.size();
        boolean quit = false;

        if(start < 0){
            start = 0;
        }

        while (!quit) {
            printMessageRange(toShow, start, stop);
            boolean ok = false;

            while(!ok) {
                System.out.println();
                System.out.println("p - to see previous messages\nn - to see next messages\nq - to exit this menu");
                System.out.print(">>");
                String response = console.nextLine();
                switch (response) {
                    case "q" -> {
                        quit = true;
                        ok = true;
                    }
                    case "p" -> {
                        if (start == 0) {
                            System.out.println("You have reached the end");
                            break;
                        }
                        stop = start;
                        start = start - Constants.SHOWING;
                        if (start < 0) {
                            start = 0;
                        }
                        ok = true;
                    }
                    case "n" -> {
                        if (stop == toShow.size()) {
                            System.out.println("You have reached the end");
                            break;
                        }
                        start = stop;
                        stop = stop + Constants.SHOWING;
                        if (stop > toShow.size()) {
                            stop = toShow.size();
                        }
                        ok = true;
                    }
                    default -> System.out.println("Invalid command");
                }
            }
        }
    }

    private void showUserMessages(){
        String username;
        System.out.print("Username: ");
        username = console.nextLine();

        Set<Message> messages = superService.getUserMessages(username);
        printMessages(messages);
    }

    private void showConversation(){
        String user1, user2;
        System.out.print("First user: ");
        user1 = console.nextLine();
        System.out.print("Second user: ");
        user2 = console.nextLine();

        Set<Message> messages = superService.getConversation(user1, user2);
        printMessages(messages);
    }

    private void printMessageRange(List<Message> messages, int start, int stop){
        System.out.println("Showing messages from " + (start + 1) + " to " + (stop) + ":");
        for (int i = start; i < stop; i++) {
            Long replyTo = messages.get(i).getReplyToMessageId();

            System.out.println("===================================================================");
            System.out.println((i + 1) + ".");
            if (replyTo.equals(0L)) {
                printMessage(messages.get(i));
            } else {
                boolean ok = false;
                for (Message msg : messages) {
                    if (msg.getId().equals(replyTo)) {
                        printReplyMessage(messages.get(i), msg);
                        ok = true;
                        break;
                    }
                }
                if (!ok) {
                    printMessage(messages.get(i));
                }
            }
            System.out.println("===================================================================");
        }
    }

    private int getMessageIndex(List<Message> messages){
        int start = messages.size() - Constants.SHOWING;
        int stop = messages.size();
        boolean quit = false;

        if(start < 0){
            start = 0;
        }

        while (!quit) {
            printMessageRange(messages, start, stop);

            boolean ok = false;

            while(!ok) {
                System.out.println();
                System.out.println("p - to see previous messages\nn - to see next messages\nq - to abort the operation\ns - to select a message");
                System.out.print(">>");
                String response = console.nextLine();
                switch (response) {
                    case "q" -> {
                        quit = true;
                        ok = true;
                    }
                    case "p" -> {
                        if (start == 0) {
                            System.out.println("You have reached the end");
                            break;
                        }
                        stop = start;
                        start = start - Constants.SHOWING;
                        if (start < 0) {
                            start = 0;
                        }
                        ok = true;
                    }
                    case "n" -> {
                        if (stop == messages.size()) {
                            System.out.println("You have reached the end");
                            break;
                        }
                        start = stop;
                        stop = stop + Constants.SHOWING;
                        if (stop > messages.size()) {
                            stop = messages.size();
                        }
                        ok = true;
                    }
                    case "s" -> {
                        System.out.print(">>");
                        String number = console.nextLine();
                        int value = -1;
                        try {
                            value = Integer.parseInt(number);
                            if (value > 0 && value <= messages.size()) {
                                return value - 1;
                            } else {
                                System.out.println("Invalid value");
                            }
                        } catch (NumberFormatException err){
                            System.out.println("invalid value");
                        }
                    }
                    default -> System.out.println("Invalid command");
                }
            }
        }
        return -1;
    }

    private void sendReply(){
        String user1, user2, text;
        System.out.print("From: ");
        user1 = console.nextLine();
        System.out.print("Conversation with: ");
        user2 = console.nextLine();

        List<Message> messages = new ArrayList<>(superService.getConversation(user1, user2));
        int index = getMessageIndex(messages);

        if(index >= 0) {
            System.out.println("Message: ");
            text = console.nextLine();
            superService.replyMessage(user1, text, messages.get(index).getId());
        }
    }

    private void sendReplyAll() {
        String user1, user2, text;
        System.out.print("From: ");
        user1 = console.nextLine();
        System.out.print("Conversation with: ");
        user2 = console.nextLine();

        List<Message> messages = new ArrayList<>(superService.getConversation(user1, user2));
        int index = getMessageIndex(messages);

        if (index >= 0) {
            System.out.println("Message: ");
            text = console.nextLine();
            superService.replyAllMessage(user1, text, messages.get(index).getId());
        }
    }

    private void addFriendRequest(){
        String from, to;
        System.out.print("From: ");
        from = console.nextLine();
        System.out.print("To: ");
        to = console.nextLine();

        superService.addFriendRequest(from, to);
        System.out.println("Friend request sent");
    }

    private void acceptFriendRequest(){
        String from, to;
        System.out.print("From: ");
        from = console.nextLine();
        System.out.print("To: ");
        to = console.nextLine();

        superService.acceptFriendRequest(from, to);
        System.out.println("Request accepted");
    }

    private void rejectFriendRequest(){
        String from, to;
        System.out.print("From: ");
        from = console.nextLine();
        System.out.print("To: ");
        to = console.nextLine();

        superService.rejectFriendRequest(from, to);
        System.out.println("Request rejected");
    }

    private void showUserFriendRequests(){
        String userId;
        System.out.print("Username: ");
        userId = console.nextLine();

        List<Tuple<String, String>> requests = superService.getUserFriendRequests(userId);

        System.out.println("Requests: ");
        requests.forEach(x -> System.out.println(x.getFirst() + " status: " + x.getSecond()));
    }

    private void help(){
        System.out.println("Supported commands:");
        System.out.println("    help                        - show this menu;");
        System.out.println("    showusers / su              - show all registered users;");
        System.out.println("    showuserfriends / suf       - show all friends of an user;");
        System.out.println("    showallfriendships / saf    - show all the friendships;");
        System.out.println("    showfriendship / sf         - show the friendship between two users;");
        System.out.println("    adduser / au                - register a new user;");
        System.out.println("    updateuser / uu             - update an existing user;");
        System.out.println("    removeuser / ru             - remove an user;");
        System.out.println("    addfriendship / af          - make two users friends;");
        System.out.println("    removefriendship /rf        - remove the friendship between two users;");
        System.out.println("    numberofcommunities / nc    - shows the number of communities");
        System.out.println("    mostsociablecommunity / msc - shows the most sociable communities");
        System.out.println("    sendmessage / sm            - send a message to one or more users");
        System.out.println("    showusermessages / sum      - show all messages of a user");
        System.out.println("    showconversation / sc       - show the conversation between two users");
        System.out.println("    sendreply / sr              - send a reply to the sender of the message");
        System.out.println("    sendreplyall / sra          - send a reply to the sender and all who got the message");
        System.out.println("    addFriendRequest / afr       - send a friend request from a user to another");
        System.out.println("    acceptFriendRequest / acfr   - accept a friend request");
        System.out.println("    rejectFriendRequest / rfr    - reject a friend request");
        System.out.println("    showUserFriendRequests / sfr - shows all the friend requests of a user");
        System.out.println();
        System.out.println("    quit / close                 - stop the program;");
        System.out.println();
    }

    public void run(){
        boolean run = true;
        String cmd;
        while (run){
            System.out.print(">>>");
            cmd = console.nextLine();
            try {
                switch (cmd) {
                    case "help"                          -> help();
                    case "quit", "close"                 -> run = false;
                    case "showusers",               "su" -> showUsers();
                    case "showuserfriends",        "suf" -> showFriends();
                    case "showuserfriendsbymonth", "sufm"-> showFriendsByMonth();
                    case "showallfriendships",     "saf" -> showAllFriendships();
                    case "showfriendship",          "sf" -> showFriendship();
                    case "adduser",                 "au" -> addUser();
                    case "updateuser",              "uu" -> updateUser();
                    case "removeuser",              "ru" -> removeUser();
                    case "addfriendship",           "af" -> addFriendship();
                    case "removefriendship",        "rf" -> removeFriendship();
                    case "numberofcommunities",     "nc" -> numberOfCommunities();
                    case "mostsociablecommunity",  "msc" -> mostSociableCommunity();
                    case "sendmessage",             "sm" -> sendMessage();
                    case "showusermessages",       "sum" -> showUserMessages();
                    case "showconversation",        "sc" -> showConversation();
                    case "sendreply",               "sr" -> sendReply();
                    case "sendreplyall",           "sra" -> sendReplyAll();
                    case "addFriendRequest",       "afr" -> addFriendRequest();
                    case "acceptFriendRequest",    "acfr"-> acceptFriendRequest();
                    case "rejectFriendRequest",    "rfr" -> rejectFriendRequest();
                    case "showUserFriendRequest",  "sfr" -> showUserFriendRequests();
                    default -> System.out.println("Invalid command");
                }
            }catch (ValidationException | NotFoundException | IllegalArgumentException | DuplicateException | RepoException exception){
                System.out.println(exception.getMessage());
            }
        }
        System.out.println("Closed");
        console.close();
    }
}
