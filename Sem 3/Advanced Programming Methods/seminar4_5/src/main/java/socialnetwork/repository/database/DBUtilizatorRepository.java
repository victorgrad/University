package socialnetwork.repository.database;

import socialnetwork.domain.Entity;
import socialnetwork.domain.Utilizator;
import socialnetwork.domain.validators.ValidationException;
import socialnetwork.domain.validators.Validator;
import socialnetwork.repository.Repository0;

import java.sql.*;
import java.util.HashSet;
import java.util.Set;

public class DBUtilizatorRepository implements Repository0<Long, Utilizator> {
    private String url;
    private String username;
    private String password;
    private Validator<Utilizator> validator;

    public DBUtilizatorRepository(String url, String username, String password, Validator<Utilizator> validator) {
        this.url = url;
        this.username = username;
        this.password = password;
        this.validator = validator;
    }

    public Long getUserId(String userName){
        try (Connection connection = DriverManager.getConnection(url, username, password);
             PreparedStatement statement = connection.prepareStatement("SELECT * from Utilizatori WHERE userName = ?")){
            statement.setString(1,userName);
            try(ResultSet resultSet = statement.executeQuery()){
                if(resultSet.next()){
                    return  resultSet.getLong("id");
                }
                return -1l;
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return -1l;
    }

    @Override
    public Utilizator findOne(Long aLong) {
        try (Connection connection = DriverManager.getConnection(url, username, password);
             PreparedStatement statement = connection.prepareStatement("SELECT * from Utilizatori WHERE id = ?")){
            statement.setString(1,String.valueOf(aLong));
            try(ResultSet resultSet = statement.executeQuery()){
                if(resultSet.next()){
                    Utilizator util = new Utilizator(resultSet.getString(2),resultSet.getString(3),resultSet.getString(4));
                    util.setId(resultSet.getLong(1));
                    return util;
                }
                return null;
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return null;
    }

    @Override
    public Iterable<Utilizator> findAll() {
        Set<Utilizator> users = new HashSet<>();
        try (Connection connection = DriverManager.getConnection(url, username, password);
             PreparedStatement statement = connection.prepareStatement("SELECT * from Utilizatori");
             ResultSet resultSet = statement.executeQuery()) {

            while (resultSet.next()) {
                Long id = resultSet.getLong("id");
                String firstName = resultSet.getString("firstName");
                String lastName = resultSet.getString("lastName");
                String userName = resultSet.getString("userName");
                Utilizator utilizator = new Utilizator(userName,firstName, lastName);
                utilizator.setId(id);
                users.add(utilizator);
            }
            return users;
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return users;
    }

    @Override
    public Utilizator save(Utilizator entity) {
        if (entity==null)
            throw new IllegalArgumentException("entity must be not null");
        validator.validate(entity);
        String sql = "insert into Utilizatori (userName, firstName, lastName ) values (?, ?, ?)";

        try (Connection connection = DriverManager.getConnection(url, username, password);
             PreparedStatement ps = connection.prepareStatement(sql)) {

            ps.setString(1, entity.getUserName());
            ps.setString(2, entity.getFirstName());
            ps.setString(3, entity.getLastName());

            ps.executeUpdate();
            return null;
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return entity;
    }

    @Override
    public Utilizator delete(Long aLong) {
        try (Connection connection = DriverManager.getConnection(url, username, password);
             PreparedStatement statement = connection.prepareStatement("SELECT * from Utilizatori WHERE id = ?");
            PreparedStatement delstatement = connection.prepareStatement("DELETE from Utilizatori WHERE id = ?")
        ){
            statement.setString(1,String.valueOf(aLong));
            delstatement.setString(1,String.valueOf(aLong));
            try(ResultSet resultSet = statement.executeQuery()){
                if(resultSet.next()){
                    Utilizator util = new Utilizator(resultSet.getString(2),resultSet.getString(3),resultSet.getString(4));
                    util.setId(resultSet.getLong(1));
                    delstatement.executeUpdate();//daca s-a gasit il stergem
                    return util;
                }
                return null;
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return null;
    }

    @Override
    public Utilizator update(Utilizator entity) {
        return null;
    }
}
