package socialnetwork.repository.database;

import socialnetwork.domain.Prietenie;
import socialnetwork.domain.Tuple;
import socialnetwork.domain.Utilizator;
import socialnetwork.domain.validators.Validator;
import socialnetwork.repository.Repository0;

import java.sql.*;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class DBPrietenieRepository implements Repository0<Tuple<Long>, Prietenie> {
    private String url;
    private String username;
    private String password;
    private Validator<Prietenie> validator;

    public DBPrietenieRepository(String url, String username, String password, Validator<Prietenie> validator) {
        this.url = url;
        this.username = username;
        this.password = password;
        this.validator = validator;
    }

    @Override
    public Prietenie findOne(Tuple<Long> longTuple) {
        try (Connection connection = DriverManager.getConnection(url, username, password);
             PreparedStatement statement = connection.prepareStatement("SELECT * from Prietenii WHERE id1 = ? and id2 = ?")){
            statement.setString(1,String.valueOf(longTuple.getLeft()));
            statement.setString(2,String.valueOf(longTuple.getRight()));
            try(ResultSet resultSet = statement.executeQuery()){
                if(resultSet.next()){
                    Prietenie prt = new Prietenie();
                    prt.setId(longTuple);
                    return prt;
                }
                return null;
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return null;
    }

    @Override
    public Iterable<Prietenie> findAll() {
        Set<Prietenie> prietenii = new HashSet<>();
        try (Connection connection = DriverManager.getConnection(url, username, password);
             PreparedStatement statement = connection.prepareStatement("SELECT * from Prietenii");
             ResultSet resultSet = statement.executeQuery()) {

            while (resultSet.next()) {
                Long id1 = resultSet.getLong("id1");
                Long id2 = resultSet.getLong("id2");
                Prietenie prt = new Prietenie();
                prt.setId(new Tuple<>(id1,id2));
                prietenii.add(prt);
            }
            return prietenii;
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return prietenii;
    }

    @Override
    public Prietenie save(Prietenie entity) {
        if (entity==null)
            throw new IllegalArgumentException("entity must be not null");
        validator.validate(entity);
        String sql = "insert into Prietenii (id1, id2) values (?, ?)";

        try (Connection connection = DriverManager.getConnection(url, username, password);
             PreparedStatement ps = connection.prepareStatement(sql)) {

            ps.setString(1, String.valueOf(entity.getId1()));
            ps.setString(2, String.valueOf(entity.getId2()));

            ps.executeUpdate();
            return null;
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return entity;
    }

    @Override
    public Prietenie delete(Tuple<Long> longTuple) {
        try (Connection connection = DriverManager.getConnection(url, username, password);
             PreparedStatement statement = connection.prepareStatement("SELECT * from Prietenii WHERE id1 = ? and id2 = ?");
             PreparedStatement delstatement = connection.prepareStatement("DELETE from Prietenii WHERE id1 = ? and id2 = ?")
        ){
            statement.setString(1,String.valueOf(longTuple.getLeft()));
            statement.setString(2,String.valueOf(longTuple.getRight()));
            delstatement.setString(1,String.valueOf(longTuple.getLeft()));
            delstatement.setString(1,String.valueOf(longTuple.getRight()));
            try(ResultSet resultSet = statement.executeQuery()){
                if(resultSet.next()){
                    Prietenie prt = new Prietenie();
                    prt.setId(longTuple);
                    delstatement.executeUpdate();//daca s-a gasit o stergem
                    return prt;
                }
                return null;
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return null;
    }

    @Override
    public Prietenie update(Prietenie entity) {
        return null;
    }

    /**
     * Functie care returneaza o lista cu id-urile prietenilor unui utilizator dat
     * @param id
     * @return
     */
    public List<Long> getPrieteni(Long id){
        List<Long> rez = new ArrayList<>();
        //id-ul prietenului se afla in dreapta
        try (Connection connection = DriverManager.getConnection(url, username, password);
             PreparedStatement statement = connection.prepareStatement("SELECT * from Prietenii WHERE id1 = ?")){
            statement.setString(1,String.valueOf(id));
            try(ResultSet resultSet = statement.executeQuery()){
                while (resultSet.next()) {
                    Long id2 = resultSet.getLong("id2");
                    rez.add(id2);
                }
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        //id-ul prietenului se afla in stanga
        try (Connection connection = DriverManager.getConnection(url, username, password);
             PreparedStatement statement = connection.prepareStatement("SELECT * from Prietenii WHERE id2 = ?")){
            statement.setString(1,String.valueOf(id));
            try(ResultSet resultSet = statement.executeQuery()){
                while (resultSet.next()) {
                    Long id1 = resultSet.getLong("id1");
                    rez.add(id1);
                }
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return rez;
    }
}
