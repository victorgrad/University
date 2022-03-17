package socialnetwork.repository.file;

import socialnetwork.domain.Entity;
import socialnetwork.domain.validators.Validator;
import socialnetwork.repository.memory.InMemoryRepository0;

import java.io.*;

import java.util.Arrays;
import java.util.List;
import java.util.Map;


///Aceasta clasa implementeaza sablonul de proiectare Template Method; puteti inlucui solutia propusa cu un Factori (vezi mai jos)
public abstract class AbstractFileRepository0<ID, E extends Entity<ID>> extends InMemoryRepository0<ID,E> {
    String fileName;
    public AbstractFileRepository0(String fileName, Validator<E> validator) {
        super(validator);
        this.fileName=fileName;
        loadData();

    }

    private void loadData() {
        try (BufferedReader br = new BufferedReader(new FileReader(fileName))) {
            String linie;
            while((linie=br.readLine())!=null){
                List<String> attr=Arrays.asList(linie.split(";"));
                E e=extractEntity(attr);
                super.save(e);
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }

    }

    /**
     *  extract entity  - template method design pattern
     *  creates an entity of type E having a specified list of @code attributes
     * @param attributes
     * @return an entity of type E
     */
    public abstract E extractEntity(List<String> attributes);

    /***
     * Functie care
     * @param entity
     * @return
     */
    protected abstract String createEntityAsString(E entity);

    @Override
    public E save(E entity){
        E e=super.save(entity);
        if (e==null)
        {
            writeToFile(entity);
        }
        return e;
    }

    @Override
    public E delete(ID id) {
        E e = super.delete(id);
        if(e!=null){
            writeAllToFile();
        }
        return e;
    }

    /***
     * Functie care scrie toate entitatile din repo in fisier (care da update fisierului)
     */
    protected void writeAllToFile(){
        try(PrintWriter writer = new PrintWriter(fileName)) { //golim fisierul
            writer.print("");
            writer.close();
        }catch (FileNotFoundException ex){
            ex.printStackTrace();
        }
        //incarcam iarasi toate elementele in fisier
        for(Map.Entry<ID,E> entity: super.entities.entrySet()){
            try (BufferedWriter bW = new BufferedWriter(new FileWriter(fileName, true))) {
                bW.write(createEntityAsString(entity.getValue()));
                bW.newLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    /***
     * Fucntie care adauga o entitate in fisier(append)
     * @param entity
     */
    protected void writeToFile(E entity){
        try (BufferedWriter bW = new BufferedWriter(new FileWriter(fileName,true))) {
            bW.write(createEntityAsString(entity));
            bW.newLine();
        } catch (IOException e) {
            e.printStackTrace();
        }

    }


}

