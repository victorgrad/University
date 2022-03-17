package repository.database;

import constants.Constants;
import domain.Friendship;
import domain.Pair;
import domain.Tuple;
import domain.exceptions.RepoException;
import repository.Repository;

import java.sql.*;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class FriendshipRepo implements Repository<Pair<String>, Friendship> {
    Connection connection;

    public FriendshipRepo(String url, String username, String password) throws SQLException {
        connection = DriverManager.getConnection(url, username, password);
    }

    @Override
    public boolean exists(Pair<String> usernames){
        String sql = "SELECT count(*) from friendships where first_user = ? and second_user = ?";

        try (PreparedStatement statement = connection.prepareStatement(sql)) {

            statement.setString(1, usernames.getLeft());
            statement.setString(2, usernames.getRight());
            ResultSet resultSet = statement.executeQuery();
            if(resultSet.next()){
                if(resultSet.getInt("count") > 0){
                    return true;
                }
            }
        }
        catch (SQLException err){
            throw new RepoException("Sql query error");
        }
        return false;
    }

    @Override
    public Friendship findOne(Pair<String> usernames) {
        Friendship friendship = null;
        String sql = "SELECT * from friendships where first_user = ? and second_user = ?";

        try (PreparedStatement statement = connection.prepareStatement(sql)){

            statement.setString(1, usernames.getLeft());
            statement.setString(2, usernames.getRight());
            ResultSet resultSet = statement.executeQuery();

            if(resultSet.next()) {
                String first = resultSet.getString("first_user");
                String second = resultSet.getString("second_user");
                LocalDate date = LocalDate.parse(resultSet.getString("begin_date"), Constants.DATE_TIME_FORMATTER);
                friendship = new Friendship(first, second, date);
            }
        }
        catch (SQLException err){
            throw new RepoException("Sql query error");
        }

        return friendship;
    }

    @Override
    public Set<Friendship> findAll() {
        Set<Friendship> friendships = new HashSet<Friendship>();
        String sql = "SELECT * from friendships";

        try (PreparedStatement statement = connection.prepareStatement(sql);
             ResultSet resultSet = statement.executeQuery()){

            while(resultSet.next()) {
                String first = resultSet.getString("first_user");
                String second = resultSet.getString("second_user");
                LocalDate date = LocalDate.parse(resultSet.getString("begin_date"), Constants.DATE_TIME_FORMATTER);
                Friendship friendship = new Friendship(first, second, date);
                friendships.add(friendship);
            }
        }
        catch (SQLException err){
            throw new RepoException("Sql query error");
        }

        return friendships;
    }

    @Override
    public void save(Friendship entity) {
        String sql = "insert into friendships (first_user, second_user, begin_date) values (?, ?, ?)";

        try (PreparedStatement ps = connection.prepareStatement(sql)) {

            ps.setString(1, entity.getId().getLeft());
            ps.setString(2, entity.getId().getRight());
            ps.setDate(3, Date.valueOf(entity.getFriendshipDate()));

            ps.executeUpdate();
        } catch (SQLException e) {
            throw new RepoException("Couldn't save in repo");
        }
    }

    @Override
    public void delete(Pair<String> usernames) {
        String sql = "delete from friendships where first_user = ? and second_user = ?";
        try (PreparedStatement statement = connection.prepareStatement(sql)){
            statement.setString(1, usernames.getLeft());
            statement.setString(2, usernames.getRight());
            statement.executeUpdate();
        }
        catch (SQLException err){
            throw new RepoException("Couldn't delete from repo");
        }
    }

    @Override
    public void update(Friendship entity) {
        String sql = "update friendships set begin_date = ? where first_user = ? and second_user = ?";

        try (PreparedStatement statement = connection.prepareStatement(sql)){
            statement.setString(1, entity.getFriendshipDate().format(Constants.DATE_TIME_FORMATTER));
            statement.setString(2, entity.getId().getLeft());
            statement.setString(3, entity.getId().getRight());

            statement.executeUpdate();
        }
        catch (SQLException err){
            throw new RepoException("Couldn't update repo");
        }
    }

    public Iterable<String> getUserFriends(String username){
        String sql = "select * from friendships where first_user = ? or second_user = ?";
        Set<String> friends = new HashSet<>();

        try(PreparedStatement statement = connection.prepareStatement(sql)){
            statement.setString(1, username);
            statement.setString(2, username);
            ResultSet resultSet = statement.executeQuery();

            while(resultSet.next()) {
                String first = resultSet.getString("first_user");
                String second = resultSet.getString("second_user");

                if(first.equals(username)){
                    friends.add(second);
                }
                else{
                    friends.add(first);
                }
            }
        }
        catch (SQLException err){
            throw new RepoException("Sql query error");
        }

        return friends;
    }

    /**
     * Updates the status of the request sent by the user with the username 'from'
     * to the user with the username 'to'
     * @param from String the username of the user sending the request
     * @param to String the username of the user receiving the request
     * @param status String the new status of the request, value from constants
     * @throws RepoException if an SQL error occurs when updating the database
     */
    public void updateRequest(String from, String to, String status) {
        String sql = "update friendship_requests set status = ? where first_user = ? and second_user = ?";
        try (PreparedStatement ps = connection.prepareStatement(sql)) {

            ps.setString(1, status);
            ps.setString(2, from);
            ps.setString(3, to);

            ps.executeUpdate();
        } catch (SQLException e) {
            throw new RepoException("Couldn't save request");
        }
    }

    /**
     * Returns the status of the friend request between the users
     * @param from String the username of the user sending the request
     * @param to String the username of the user receiving the request
     * @return String the status of the request value from constants of null if the request doesn't exist
     * @throws RepoException if an SQL error occurs when updating the database
     */
    public String getRequestStatus(String from, String to){
        String sql1 = "select status from friendship_requests where first_user = ? and second_user = ?";
        String status = null;

        try (PreparedStatement ps = connection.prepareStatement(sql1)) {
            ps.setString(1, from);
            ps.setString(2, to);

            ResultSet resultSet = ps.executeQuery();
            if(resultSet.next()){
                //the friend request already exists
                status = resultSet.getString("status");
            }
        } catch (SQLException e){
            throw new RepoException("SQL query error");
        }

        return status;
    }

    /**
     * Adds a new request or updates an existent one if possible
     * @param from String the username of the user sending the request
     * @param to String the username of the user receiving the request
     * @throws RepoException if the users are already friends or the request is already pending
     */
    public void addFriendshipRequest(String from, String to){
        String sql = "insert into friendship_requests (first_user, second_user, status) values (?, ?, ?)";
        try (PreparedStatement ps = connection.prepareStatement(sql)) {
            ps.setString(1, from);
            ps.setString(2, to);
            ps.setString(3, Constants.PENDINGREQUEST);

            ps.executeUpdate();
        } catch (SQLException e) {
            throw new RepoException("Couldn't save request");
        }
    }

    /**
     * Returns a list with all the requests that can be accepted by the user
     * @param user String the username of the user
     * @return List that contains Tuples that contain in the first value the username of the user sending the request and in the second value the status of the request
     */
    public List<Tuple<String, String>> getFriendRequests(String user) {
        List<Tuple<String, String>> rez = new ArrayList<>();

        String sql = "select * from friendship_requests where second_user = ?";

        try(PreparedStatement ps = connection.prepareStatement(sql)){
            ps.setString(1, user);
            ResultSet resultSet = ps.executeQuery();

            while (resultSet.next()){
                String friend = resultSet.getString("first_user");
                String status = resultSet.getString("status");
                Tuple<String, String> request = new Tuple<String, String >(friend, status);

                rez.add(request);
            }
        }catch (SQLException err){
            throw new RepoException("SQL query error");
        }

        return rez;
    }

    /**
     * Removes the request sent by the first user to the second user
     * @param from String the username of the user sending the request
     * @param to String the username of the user receiving the request
     * @throws RepoException if an SQL error occurs when updating the database
     */
    public void removeFriendRequest(String from, String to){
        String sql = "delete from friendship_requests where (first_user = ? and second_user = ?)";
        try (PreparedStatement ps = connection.prepareStatement(sql)) {
            ps.setString(1, from);
            ps.setString(2, to);

            ps.executeUpdate();
        } catch (SQLException err){
            throw new RepoException("Couldn't delete request");
        }
    }
}
