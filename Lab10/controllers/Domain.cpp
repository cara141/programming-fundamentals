#include "Domain.h"

const int &Medication::getId() const {
    return id;
}

const std::string &Medication::getName() const {
    return name;
}

const double &Medication::getPrice() const {
    return price;
}

const std::string &Medication::getProducer() const {
    return producer;
}

const std::string &Medication::getSubstance() const {
    return substance;
}

void Medication::setId(const int &newId) {
    this->id = newId;
}

void Medication::setName(const std::string &newName){
    this->name = newName;
}

void Medication::setPrice(const double &newPrice){
    this->price = newPrice;
}

void Medication::setProducer(const std::string &newProducer){
    this->producer = newProducer;
}

void Medication::setSubstance(const std::string &newSubstance){
    this->substance = newSubstance;
}

bool Medication::operator==(const Medication &medication) const {
    return id == medication.id;
}

bool Medication::operator!=(const Medication &medication) const {
    return !(medication == *this);
}




