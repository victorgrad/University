package socialnetwork.service;

import socialnetwork.domain.*;

import java.util.ArrayList;
import java.util.Collection;
import java.util.HashMap;
import java.util.List;

public class ReteaService {
    public UtilizatorService0 utilizatorService;
    public PrietenieService prietenieService;

    public ReteaService(UtilizatorService0 utilizatorService, PrietenieService prietenieService) {
        this.utilizatorService = utilizatorService;
        this.prietenieService = prietenieService;
        //AddPrietenii();
    }

    /***
     * Functie care ia prieteniile din fisier si le adauga la fiecare utilizator la pornirea aplicatiei
     */
//    private void AddPrietenii(){
//        for(Prietenie pr: prietenieService.getAll()){
//            Utilizator u1 = utilizatorService.getOneById(pr.getId().getLeft());
//            Utilizator u2 = utilizatorService.getOneById(pr.getId().getRight());
//            u1.addFriend(u2);
//            u2.addFriend(u1);
//        }
//    }

    /***
     * Functie care returneaza o lista de prieteni pentru un utilizator cu un id dat
     * @return
     */
    public List<Utilizator> getFriends(Long idUser){
        List<Long> iduri = prietenieService.getPrieteni(idUser);
        List<Utilizator> rez = new ArrayList<>();
        for(Long id:iduri){
            rez.add(utilizatorService.getOneById(id));
        }
        return rez;
    }
    /***
     * Functie care adauga o prietenie adaugand totodata utilizatorul in lista de prieteni a fiecaruia
     * @param util1,util2 - string - Username-urile celor 2 utilizatori
     */
    public void AddPrietenie(String util1,String util2){
        //verificam existenta utilizatorilor
        Utilizator u1 = utilizatorService.getOne(util1);
        Utilizator u2 = utilizatorService.getOne(util2);
        if(u1==null || u2 == null){
            System.out.println("Unul dintre utilizatori nu exista\n");
            return;
        }
        //verificam existenta prieteniei
        Tuple<Long> tpl = new Tuple<>(u1.getId(), u2.getId());
        Prietenie prt = new Prietenie();
        prt.setId(tpl);
        if(prietenieService.addPrietenie(prt)!=null){
            System.out.println("Prietenia exista deja\n");
        }
//        else{//daca prietenia nu exista adaugam prietenii in lista "privata"
//            u1.addFriend(u2);
//            u2.addFriend(u1);
//        } nu mai este nevoie de lista de prieteni
    }

    /***
     * Functie care sterge o prietenie stergand totodata utilizatorul din lista de prieteni a fiecaruia
     * @param util1,util2 - string - Username-urile celor 2 utilizatori
     */
    public void RemovePrietenie(String util1,String util2){
        //verificam existenta utilizatorilor
        Utilizator u1 = utilizatorService.getOne(util1);
        Utilizator u2 = utilizatorService.getOne(util2);
        if(u1==null || u2 == null){
            System.out.println("Unul dintre utilizatori nu exista\n");
            return;
        }
        //verificam existenta prieteniei
        Tuple<Long> tpl = new Tuple<>(u1.getId(), u2.getId());
        if(prietenieService.removePrietenie(tpl)==null){
            System.out.println("Prietenia nu exista\n");
        }
//        else{//daca prietenia exista stergem prietenii din lista "privata"
//            u1.removeFriend(u2);
//            u2.removeFriend(u1);
//        }
    }

    /***
     * Functie care returneaza o lista de utilizatori doar cu informatie de afisat
     * @return List<UtilizatorDTO>
     */
    public List<UtilizatorDTO> GetUsersAsDTO(){
        List<UtilizatorDTO> rez = new ArrayList<>();
        for(Utilizator utilizator: utilizatorService.getAll()){
            UtilizatorDTO nou = new UtilizatorDTO(utilizator.getFirstName(), utilizator.getLastName(), getFriends(utilizator.getId()));
            rez.add(nou);
        }
        return rez;
    }

    /***
     * Functie care returneaza un utilizator doar cu informatie de afisat pe baza id-ului
     * @param username
     * @return List<UtilizatorDTO>
     */
    public UtilizatorDTO GetUserAsDTO(String username){
        Utilizator util = utilizatorService.getOne(username);
        UtilizatorDTO nou = new UtilizatorDTO(util.getFirstName(), util.getLastName(), getFriends(util.getId()));
        return nou;
    }

    /***
     * Functie utilitara de DFS
     * @param v
     * @param visited
     * @param adjListArray
     * @param membri
     */
    private void DFSUtil(int v, boolean[] visited, HashMap<Integer,ArrayList<Integer>> adjListArray,List<Integer> membri)
    {
        //marcam nodul curent ca vizitat si vizitam nodurile alturate
        visited[v] = true;
        membri.add(v);//il adaugam la membri
        for (int x : adjListArray.get(v)) {
            if (!visited[x]) {
                DFSUtil(x, visited, adjListArray, membri);
            }
        }
    }

    /***
     * Functie care returneaza mai multe date despre comunitatile din retea
     * @return Tuplu<Integer,List<Integer>>
     *     Integer - numarul de comunitati din retea
     *     List<UtilizatorDTO> - lista cu DTO-urile utilizatorilor din comunitatea cea mai populata
     */
    public Tuplu<Integer,List<UtilizatorDTO>> NrOfComunities(){
        HashMap<Integer,ArrayList<Integer>> adjListArray = new HashMap<>();
        for (Utilizator utilizator: utilizatorService.getAll()) {
            adjListArray.put(utilizator.getId().intValue(), new ArrayList<>());
        }

        //adaugam toate componentele in lista de adiacenta
        for(Prietenie prietenie: prietenieService.getAll()){
            adjListArray.get(prietenie.getId().getLeft().intValue()).add(prietenie.getId().getRight().intValue());
            adjListArray.get(prietenie.getId().getRight().intValue()).add(prietenie.getId().getLeft().intValue());
        }

        //calculam numarul de componente conexe
        int nr=0;
        List<Integer> membri = new ArrayList<Integer>();
        boolean[] visited = new boolean[utilizatorService.maxId()+1];
        for (Utilizator utilizator: utilizatorService.getAll()) {
            if (!visited[utilizator.getId().intValue()]) {
                //pornim de la v si marcam toti utilizatorii comunitatii ca fiind 'vizitati'
                List<Integer> membritmp = new ArrayList<Integer>();
                DFSUtil(utilizator.getId().intValue(), visited, adjListArray,membritmp);
                if(membritmp.size()>membri.size()){
                    membri=new ArrayList<>(membritmp);
                }
                //contorizam comunitatea
                nr++;
            }
        }
        List<UtilizatorDTO> comunitate = new ArrayList<UtilizatorDTO>();
        for(Integer id:membri){
            comunitate.add(GetUserAsDTO(utilizatorService.getOneById(Integer.toUnsignedLong(id)).getUserName()));
        }
        return new Tuplu<>(nr,comunitate);
    }

    /***
     * Functie care sterge un utilizator din repo de utilizatori si din lista de prietenii a fiecarui utilizator,stergand totodata prieteniile care il contin pe acesta
     * @param username
     * @return Utilizatorul daca a fost sters
     *         null daca utilizatorul nu exista
     */
    public Utilizator removeUtilizator(String username){
        Utilizator util = utilizatorService.getOne(username);
        Utilizator task = utilizatorService.removeUtilizator(username);
        if(task!=null) {
            for (Prietenie prt : prietenieService.getAll()) {
                if (prt.getId1() == util.getId() || prt.getId2() == util.getId()) {
                    prietenieService.removePrietenie(prt.getId());
                }
            }
//            for (Utilizator utilizator : utilizatorService.getAll()) {
//                utilizator.removeFriend(util);
//            }
        }
        return task;
    }

    public void FindSolutions(HashMap<Integer,ArrayList<Integer>> adjListArray,boolean[] visited,int util,int len,int utilf,int lenf){
        boolean AllVisited = true;
        visited[util]=true;
        //verificam daca toate nodurile adiacente unui nod au fost vizitate
        for(Integer vecin:adjListArray.get(util)){
            if(visited[vecin]==false){
                AllVisited=false;
            }
        }
        if(AllVisited){//daca am gasit o solutie
            if(len>lenf){//daca contine cel mai lung drum
                utilf=util;
                lenf=len;
            }
            return;
        }
        for(Integer vecin:adjListArray.get(util)){//mai adaugam pe cineva la lant
            if(visited[vecin]==false){ //verificam sa nu fie vizitat(lant elementar)
                FindSolutions(adjListArray,visited,vecin,len+1,utilf,lenf);
                //stergem vecinul din lista cautarii
                visited[vecin]=false;
            }
        }


    }

    public void PrintBiggestComunity(){
        HashMap<Integer,ArrayList<Integer>> adjListArray = new HashMap<>();
        for (Utilizator utilizator: utilizatorService.getAll()) {
            adjListArray.put(utilizator.getId().intValue(), new ArrayList<>());
        }

        //adaugam toate componentele in lista de adiacenta
        for(Prietenie prietenie: prietenieService.getAll()){
            adjListArray.get(prietenie.getId().getLeft().intValue()).add(prietenie.getId().getRight().intValue());
            adjListArray.get(prietenie.getId().getRight().intValue()).add(prietenie.getId().getLeft().intValue());
        }
        boolean[] visited = new boolean[utilizatorService.maxId()+1];
        int utilf= utilizatorService.maxId();
        int lenf=0;
        for (Utilizator utilizator: utilizatorService.getAll()) {
            FindSolutions(adjListArray,visited,utilizator.getId().intValue(),1,utilf,lenf);
        }
        System.out.println("lungimea celei mai mari comunitati: "+ String.valueOf(lenf)+" cu utilizatorul "+ String.valueOf(utilf));
    }

}
