package socialnetwork.service;

import socialnetwork.domain.Prietenie;
import socialnetwork.domain.Tuple;
import socialnetwork.domain.Utilizator;
import socialnetwork.domain.validators.ValidationException;
import socialnetwork.repository.Repository0;
import socialnetwork.repository.database.DBPrietenieRepository;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class PrietenieService {
    private DBPrietenieRepository repo;

    public PrietenieService(DBPrietenieRepository repo) {
        this.repo = repo;
    }

    /***
     * Functie care primeste o prietenie si o salveaza in repo de prietenii
     * @param messageTask
     * @return returneaza null daca prietenia a fost adaugata
     *         returneaza prietenia daca exista deja
     */
    public Prietenie addPrietenie(Prietenie messageTask) {
        Prietenie task = repo.save(messageTask);
        return task;
    }

    /***
     * Functie care primeste un id de prietenie si o sterge din lista de prietenii
     * @param id
     * @return returneaza prietenia daca a fost stearsa
     *         returneaza null daca prietenia nu exista
     */
    public Prietenie removePrietenie(Tuple<Long> id){
        Prietenie task = repo.delete(id);
        return task;
    }

    /***
     * Functie care returneaza toate prieteniile
     * @return Iterable<Prietenie>
     */
    public Iterable<Prietenie> getAll(){
        return repo.findAll();
    }

    public List<Long> getPrieteni(Long id){
        return repo.getPrieteni(id);
    }
}
