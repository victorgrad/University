package socialnetwork.domain.validators;

import socialnetwork.domain.Prietenie;


public class PrietenieValidator implements Validator<Prietenie>{
    @Override
    public void validate(Prietenie entity) throws ValidationException {
        if(entity.getId1() == entity.getId2())
            throw new ValidationException("Nu poti crea o prietenie intre acelasi utilizator");
        if(entity.getId().getLeft()==null)
            throw new ValidationException("Id-ul stang nu poate fi null");
        if(entity.getId().getRight()==null)
            throw new ValidationException("Id-ul drept nu poate fi null");
    }
}
