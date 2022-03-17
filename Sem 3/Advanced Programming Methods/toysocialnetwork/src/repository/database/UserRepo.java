package repository.database;

import domain.User;
import domain.exceptions.RepoException;
import repository.Repository;

import java.sql.*;
import java.util.HashSet;
import java.util.Set;

public class UserRepo implements Repository<String, User> {
    private final Connection connection;

    public UserRepo(String url, String username, String password) throws SQLException {
        connection = DriverManager.getConnection(url, username, password);
    }

    @Override
    public boolean exists(String username){
        String sql = "SELECT count(*) from users where username = ?";

        try (PreparedStatement statement = connection.prepareStatement(sql)) {
            statement.setString(1, username);
            ResultSet resultSet = statement.executeQuery();
            if(resultSet.next()){
                if(resultSet.getInt("count") > 0){
                    return true;
                }
            }
        }
        catch (SQLException err){
            throw new RepoException("SQL query error");
        }
        return false;
    }

    @Override
    public User findOne(String username) {
        User user = null;
        String sql = "SELECT * from users where username = ?";

        try (PreparedStatement statement = connection.prepareStatement(sql)){
            statement.setString(1, username);
            ResultSet resultSet = statement.executeQuery();

            if(resultSet.next()) {
                String firstName = resultSet.getString("first_name");
                String lastName = resultSet.getString("last_name");
                user = new User(username, firstName, lastName);
            }
        }
        catch (SQLException err){
            throw new RepoException("SQL query error");
        }

        return user;
    }

    @Override
    public Iterable<User> findAll() {
        Set<User> users = new HashSet<>();

        try(PreparedStatement statement = connection.prepareStatement("SELECT * from users");
            ResultSet resultSet = statement.executeQuery()) {

            while (resultSet.next()) {
                String username = resultSet.getString("username");
                String firstName = resultSet.getString("first_name");
                String lastName = resultSet.getString("last_name");

                User user = new User(username, firstName, lastName);
                users.add(user);
            }
        }
        catch (SQLException err){
            throw new RepoException("SQL query error");
        }
        return users;
    }

    @Override
    public void save(User entity) {
        String sql = "insert into users (username, first_name, last_name ) values (?, ?, ?)";

        try (PreparedStatement ps = connection.prepareStatement(sql)) {

            ps.setString(1, entity.getId());
            ps.setString(2, entity.getFirstName());
            ps.setString(3, entity.getLastName());

            ps.executeUpdate();
        } catch (SQLException e) {
            throw new RepoException("Couldn't insert in repo");
        }
    }

    @Override
    public void delete(String username) {
        String sql = "delete from users where username = ?";
        try (PreparedStatement statement = connection.prepareStatement(sql)){
            statement.setString(1, username);
            statement.executeUpdate();
        }
        catch (SQLException err){
            throw new RepoException("Couldn't delete from repo");
        }
    }

    @Override
    public void update(User entity) {
        String sql = "update users set first_name = ?, last_name = ? where username = ?";

        try (PreparedStatement statement = connection.prepareStatement(sql)){
            statement.setString(1, entity.getFirstName());
            statement.setString(2, entity.getLastName());
            statement.setString(3, entity.getId());

            statement.executeUpdate();
        }
        catch (SQLException err){
            throw new RepoException("Couldn't update repo");
        }
    }
}
