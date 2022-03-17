package socialnetwork.repository.file;

import socialnetwork.domain.Entity;
import socialnetwork.domain.Prietenie;
import socialnetwork.domain.Tuple;
import socialnetwork.domain.Utilizator;
import socialnetwork.domain.validators.Validator;

import java.util.List;

public class PrietenieFile0 extends AbstractFileRepository0<Tuple<Long>, Prietenie>{
    public PrietenieFile0(String fileName, Validator<Prietenie> validator) {
        super(fileName, validator);
    }

    @Override
    public Prietenie extractEntity(List<String> attributes) {
        Prietenie prietenie = new Prietenie();
        prietenie.setId(new Tuple<Long>(Long.parseLong(attributes.get(0)),Long.parseLong(attributes.get(1))));
        return prietenie;
    }

    @Override
    protected String createEntityAsString(Prietenie entity) {
        return entity.getId().getLeft().toString()+";"+entity.getId().getRight().toString();
    }
}
