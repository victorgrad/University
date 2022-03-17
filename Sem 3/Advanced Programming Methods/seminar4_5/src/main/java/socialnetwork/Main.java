package socialnetwork;

import socialnetwork.domain.validators.PrietenieValidator;
import socialnetwork.domain.validators.UtilizatorValidator;
import socialnetwork.repository.database.DBPrietenieRepository;
import socialnetwork.repository.database.DBUtilizatorRepository;
import socialnetwork.repository.file.PrietenieFile0;
import socialnetwork.service.PrietenieService;
import socialnetwork.service.ReteaService;
import socialnetwork.service.UtilizatorService0;
import socialnetwork.ui.MainMenu;

public class Main {
    public static void main(String[] args) {
        //String fileName=ApplicationContext.getPROPERTIES().getProperty("data.socialnetwork.users");
        String fileName1="data/users.csv";
        String fileName2="data/friendships.csv";
        MainMenu menu = new MainMenu(new ReteaService(new UtilizatorService0(new DBUtilizatorRepository("jdbc:postgresql://localhost:5432/Network","postgres","postgres",new UtilizatorValidator())),new PrietenieService(new DBPrietenieRepository("jdbc:postgresql://localhost:5432/Network","postgres","postgres",new PrietenieValidator()))));

        menu.run();
        System.out.println("ok");

    }
}


