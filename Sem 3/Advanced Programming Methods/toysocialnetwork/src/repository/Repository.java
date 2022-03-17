package repository;

import domain.Entity;

public interface Repository<ID, E extends Entity<ID>> {
    E findOne(ID id);
    Iterable<E> findAll();
    void save(E entity);
    void delete(ID id);
    void update(E entity);
    boolean exists(ID id);
}
