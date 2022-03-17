package socialnetwork.domain.validators;

import socialnetwork.domain.Utilizator;

public class UtilizatorValidator implements Validator<Utilizator> {
    @Override
    public void validate(Utilizator entity) throws ValidationException {
        if(entity.getLastName().isEmpty()){
            throw new ValidationException("Numele nu trebuie sa fie gol");
        }
        if(entity.getFirstName().isEmpty()){
            throw new ValidationException("Preumele nu trebuie sa fie gol");
        }
        char[] prenume = entity.getFirstName().toCharArray();
        char[] nume = entity.getLastName().toCharArray();

        for (char c : nume) {
            if(!Character.isLetter(c)) {
                throw new ValidationException("Numele trebuie sa contina doar litere(Sorry Elon)");
            }
        }
        for (char c : prenume) {
            if(!Character.isLetter(c)) {
                throw new ValidationException("Prenumele trebuie sa contina doar litere(Sorry Elon)");
            }
        }
    }
}
