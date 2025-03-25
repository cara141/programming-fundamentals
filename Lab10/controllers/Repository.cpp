#include "Repository.h"
#include <stdexcept>

Repository::Repository(const Repository &repo) = default;

int Repository::size() const{
    return (int) this->list.size();
}

const Medication &Repository::element(const int &i) const{
    return this->getAll()[i];
}

Repository &Repository::add(const Medication &med) {
    if(find(med) == -1){
        this->list.push_back(med);
        return *this;
    }
    else
        throw std::invalid_argument("Medication already exists.");
}

Repository &Repository::remove(const Medication &med){
    int i = find(med);
    if(i == -1)
        throw std::invalid_argument("Medication does not exist.");
    else
        this->list.erase(this->list.begin() + i);
    return *this;
}


int Repository::find(const Medication &med) const{
    for(int i = 0; i < this->size(); i++){
        if(this->element(i) == med)
            return i;
    }
    return -1;
}

Repository &Repository::modify(const Medication &med, const Medication &new_med){
    int i = find(med);
    if(i == -1)
        throw std::invalid_argument("Medication does not exist.");
    else
        this->list[i] = new_med;
    return *this;
}

const std::vector<Medication> &Repository::getAll() const{
    return this->list;
}