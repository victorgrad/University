package socialnetwork.service;

import socialnetwork.domain.Prietenie;
import socialnetwork.domain.Utilizator;
import socialnetwork.repository.Repository0;
import socialnetwork.repository.database.DBUtilizatorRepository;

public class UtilizatorService0 {
    private DBUtilizatorRepository repo;
    //private Repository0<Long, Utilizator> repo;

    public UtilizatorService0(DBUtilizatorRepository repo) {
        this.repo = repo;
    }

    /***
     * Functie care adauga un utilizator in repo utilizatori
     * @param messageTask - Utilizator
     * @return returneaza null daca utilizatorul a fost adaugat
     *         returneaza Utilizator daca utilizatorul exista deja
     */
    public Utilizator addUtilizator(Utilizator messageTask) {
        Utilizator task = repo.save(messageTask);
        return task;
    }

    /***
     * Functie care primeste un id de utilizator si il sterge din lista de utilizatori
     * @param username
     * @return returneaza utilizatorul daca a fost sters
     *         returneaza null daca utilizatorul nu exista
     */
    public Utilizator removeUtilizator(String username){
        Utilizator task = repo.delete(repo.getUserId(username));
        return task;
    }

    /***
     * Functie care pentru un utilizator adauga un alt utilizator in lista de prieteni
     * @param username - username-ul utilizatorului la care dorim sa adaugam un prieten
     * @param prt - Utilizatorul care dorim sa il adaugam
     */
//    public void addPrietenie(String username, Utilizator prt){
//        repo.findOne(repo.getUserId(username)).addFriend(prt);
//    }

    /***
     * Functie care returneaza un utilizator din repo
     * @param username
     * @return Utilizator daca utilizatorul exista
     *         null daca utilizatorul nu exista
     */
    public Utilizator getOne(String username){return repo.findOne(repo.getUserId(username));}

    /***
     * Functie care returneaza un utilizator din repo
     * @param id
     * @return Utilizator daca utilizatorul exista
     *         null daca utilizatorul nu exista
     */
    public Utilizator getOneById(Long id){return repo.findOne(id);}
    /***
     * Functie care returneaza toti utilizatorii
     * @return Iterable<Utilizator>
     */
    public Iterable<Utilizator> getAll(){
        return repo.findAll();
    }

    /***
     * Functie ajutor care returneaza cel mai mare id de utilizator prezent in repo
     * @return id - int
     */
    public int maxId(){
        int rez=-99999;
        for(Utilizator utilizator: repo.findAll()){
            if(utilizator.getId().intValue()>rez)
                rez=utilizator.getId().intValue();
        }
        return rez;
    }
}
