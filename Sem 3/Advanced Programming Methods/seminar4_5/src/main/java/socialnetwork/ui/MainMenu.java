package socialnetwork.ui;


import socialnetwork.domain.Tuple;
import socialnetwork.domain.Utilizator;
import socialnetwork.domain.UtilizatorDTO;
import socialnetwork.domain.validators.ValidationException;
import socialnetwork.service.PrietenieService;
import socialnetwork.service.ReteaService;
import socialnetwork.service.UtilizatorService0;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class MainMenu {
    private ReteaService service;
    //private UtilizatorService0 utilizatorService;
    //private PrietenieService prietenieService;


    public MainMenu(ReteaService service) {
        this.service = service;
    }

    private void AddUser(){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Introduceti Numele utilizatorului: ");
        String nume = scanner.nextLine();
        System.out.println("Introduceti Prenumele utilizatorului: ");
        String prenume = scanner.nextLine();
        System.out.println("Introduceti username-ul utilizatorului: ");
        String userName = scanner.nextLine();
        Utilizator util = new Utilizator(userName,prenume,nume);
        try{
           if(service.utilizatorService.addUtilizator(util)!=null){
               System.out.println("Utilizator existent(ID duplicat)\n");
           }
        }catch (ValidationException ex){
            ex.printStackTrace();
        }
    }

    private void RemoveUser(){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Introduceti username-ul utilizatorului pe care doriti sa il stergeti(Un Long/Int): ");
        String username = scanner.nextLine();
        try{
            if(service.removeUtilizator(username)==null){
                System.out.println("Utilizator inexistent\n");
            }
        }catch (ValidationException ex){
            ex.printStackTrace();
        }
    }

    private void AddFriendship(){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Introduceti username-ul utilizatorului care sterge prietenia: ");
        String id1 = scanner.nextLine();
        System.out.println("Introduceti username-ul utilizatorului sters din lista de prieteni: ");
        String id2 = scanner.nextLine();
        try{
            //Tuple<Long> tpl =  new Tuple<>(id1,id2);
            service.AddPrietenie(id1,id2);
        }catch (ValidationException ex){
            ex.printStackTrace();
        }
    }

    private void RemoveFriendship(){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Introduceti username-ul utilizatorului care sterge prietenia: ");
        String id1 = scanner.nextLine();
        System.out.println("Introduceti username-ul utilizatorului sters din lista de prieteni: ");
        String id2 = scanner.nextLine();
        try{
            //Tuple<Long> tpl =  new Tuple<>(id1,id2);
            service.RemovePrietenie(id1,id2);
        }catch (ValidationException ex){
            ex.printStackTrace();
        }
    }

    public void ShowUsers(){
        List<UtilizatorDTO> lista = service.GetUsersAsDTO();
        for(UtilizatorDTO user:lista){
            System.out.println(user.toString()+"\n");
        }
    }

    public void run() {
        while (true) {
            Scanner scan = new Scanner(System.in);
            System.out.println("Alegeti o optiune:\n1.Adaugare user\n2.Stergere user\n3.Adaugare prietenie\n4.Stergere prietenie\n5.Afisare utilizatori\n6.Numar comunitati\n7.Cea mai mare comunitate\n8.Exit");
            int optiune = scan.nextInt();
            switch (optiune) {
                case (1): {
                    AddUser();
                    break;
                }
                case (2): {
                    RemoveUser();
                    break;
                }
                case (3): {
                    AddFriendship();
                    break;
                }
                case (4): {
                    RemoveFriendship();
                    break;
                }
                case (5): {
                    ShowUsers();
                    break;
                }
                case (6): {
                    System.out.println(service.NrOfComunities().getLeft());
                    break;
                }
                case (7): {
                    List<UtilizatorDTO> comunitate = service.NrOfComunities().getRight();
                    System.out.println(comunitate);
                    break;
                }
                case (8): {
                    return;
                }
                default: {
                    System.out.println("Nu ati introdus o optiune valida\n");
                }
            }
        }
    }
}
