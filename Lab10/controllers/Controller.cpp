#include "Controller.h"

[[nodiscard]] const Repository &Controller::getRepository() const{
    return this->repo;
}

Controller &Controller::add(const Medication &med){
    try{
        this->repo.add(med);
    }
    catch(std::invalid_argument &e){
        throw std::invalid_argument("Medication already exists.");
    }
    return *this;
}

Controller &Controller::remove(const Medication &med){
    try{
        this->repo.remove(med);
    }
    catch(std::invalid_argument &e){
        throw std::invalid_argument("Medication does not exist.");
    }
    return *this;
}
Controller &Controller::modify(const Medication &med, const Medication &newMed){
    try{
        this->repo.modify(med, newMed);
    }
    catch(std::invalid_argument &e){
        throw std::invalid_argument("Medication does not exist.");
    }
    return *this;
}

[[nodiscard]] const Medication &Controller::find(const Medication &med) const{
    int i = this->repo.find(med);
    if(i == -1)
        throw std::invalid_argument("Medication does not exist.");
    else
        return this->repo.element(i);
}

const std::vector<Medication> &Controller::getAll() const{
    return this->repo.getAll();
}