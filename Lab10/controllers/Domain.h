#pragma once
#include <string>
#include <ostream>
#include <utility>
#include <iostream>
//
class Medication{
public:

    Medication() = default;

    Medication(const Medication &medication) : id(medication.id), name(medication.name), price(medication.price),
                                               producer(medication.producer), substance(medication.substance){

        std::cout << "Copy constructor called" << std::endl;
    }

    Medication(const int &id, std::string name, const double &price,
                           std::string producer, std::string substance) : id(id), name(std::move(name)),
                           price(price), producer(std::move(producer)), substance(std::move(substance)) {

    }

    ~Medication() = default;

    Medication(Medication &&medication) noexcept = default;

    Medication &operator=(Medication &&medication) noexcept = default;

    Medication &operator=(const Medication& other){
        if(this == &other){
            return *this;
        }
        this->id = other.id;
        this->name = other.name;
        this->price = other.price;
        this->producer = other.producer;
        this->substance = other.substance;

        std::cout << "Assignment operator called" << std::endl;
        return *this;

    }

    [[nodiscard]] const int &getId() const;

    [[nodiscard]] const std::string &getName() const;

    [[nodiscard]] const double &getPrice() const;

    [[nodiscard]] const std::string &getProducer() const;

    [[nodiscard]] const std::string &getSubstance() const;

    void setId(const int &newId);

    void setName(const std::string &newName);

    void setPrice(const double &newPrice);

    void setProducer(const std::string &newProducer);

    void setSubstance(const std::string &newSubstance);

    bool operator==(const Medication &rhs) const;

    bool operator!=(const Medication &rhs) const;

    friend std::ostream &operator<<(std::ostream &os, const Medication &medication);

private:

    int id = 0;
    std::string name;
    double price = 0;
    std::string producer;
    std::string substance;

};
