package domain.validators;

import domain.exceptions.ValidationException;

public interface Validator<T>{
    void validate(T entity) throws ValidationException;
}
