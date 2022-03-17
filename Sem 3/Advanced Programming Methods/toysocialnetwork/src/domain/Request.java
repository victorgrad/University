package domain;

import constants.Constants;

public class Request extends Entity<Long>{
    String from;
    String to;
    String status;

    /**
     * Class constructor
     * @param from String, the username of the person that sent the request
     * @param to String, the username of the person that recieved the request
     * @param status String, the status of the request
     */
    public Request(String from, String to, String status){
        this.from = from;
        this.to = to;
        this.status = status;
    }

    /**
     * Class constructor that defaults the status as pending
     * @param from String, the username of the person that sent the request
     * @param to String, the username of the person that recieved the request
     */
    public Request(String from, String to){
        this.from = from;
        this.to = to;
        this.status = Constants.PENDINGREQUEST;
    }

    /**
     * Returns the username of the sender of the request
     * @return String
     */
    public String getFrom() {
        return from;
    }

    /**
     * Sets the username of the sender of the request
     * @param from String, username of user that sent the request
     */
    public void setFrom(String from) {
        this.from = from;
    }

    /**
     * Returns the username of the receiver of the request
     * @return String
     */
    public String getTo() {
        return to;
    }

    /**
     * Sets the username of the receiver of the request
     * @param to String, the username of the user that received the request
     */
    public void setTo(String to) {
        this.to = to;
    }

    /**
     * Returns the status of the request
     * @return String
     */
    public String getStatus() {
        return status;
    }

    /**
     * Sets the status of the request
     * @param status String, the status of the request
     */
    public void setStatus(String status) {
        this.status = status;
    }
}
