#include "UI.h"

#include <cmath>
#include <iostream>

std::ostream &operator<<(std::ostream &os, const Medication &medication) {
    os << " - id: " << medication.id << " - name: " << medication.name << " - price: "
       << medication.price << " - producer: " << medication.producer << " - substance: "
       << medication.substance;
    return os;
}

void UI::run(){

        std::string command;

        while(true){
            std::cout << "Enter a command: ";
            std::cin >> command;

            if(command == "add" || command == "1"){
                add();
            } else if(command == "remove" || command == "2"){
                remove();
            } else if(command == "modify" || command == "3"){
                modify();
            } else if(command == "printAll" || command == "4"){
                printAll();
            } else if(command == "find" || command == "5"){
                find();
            } else if(command == "exit" || command == "0"){
                break;
            } else {
                std::cout << "Invalid command!" << std::endl;
            }
        }

}

void UI::add(){

    int id = 0;
    std::string name, producer, substance;
    double price = NAN;

    std::cout << "Id: ";
    std::cin >> id;

    std::cout << "Name: ";
    std::cin >> name;

    std::cout << "Price: ";
    std::cin >> price;

    std::cout << "Producer: ";
    std::cin >> producer;

    std::cout << "Substance: ";
    std::cin >> substance;

    Medication med{id, name, price, producer, substance};

    ctrl.add(med);
}

void UI::remove(){

        int id = 0;
        std::cout << "Id: ";
        std::cin >> id;

        Medication med {id, "", 0, "", ""};

        ctrl.remove(med);

}

void UI::modify(){

    int id = 0;
    std::cout << "Id: ";
    std::cin >> id;

    Medication med {id, "", 0, "", ""};

    std::string newName, newProducer, newSubstance;
    double newPrice = NAN;

    std::cout << "Name: ";
    std::cin >> newName;

    std::cout << "Price: ";
    std::cin >> newPrice;

    std::cout << "Producer: ";
    std::cin >> newProducer;

    std::cout << "Substance: ";
    std::cin >> newSubstance;

    Medication newMed{id, newName, newPrice, newProducer, newSubstance};

    ctrl.modify(med, newMed);
}

void UI::printAll(){

    if(ctrl.getAll().empty()){
            std::cout << "No medications." << std::endl;
            return;
    }
    else
        for(const auto &med : ctrl.getAll()){
            std::cout << med << std::endl;
        }
}

void UI::find(){

        int id = 0;
        std::cout << "Id: ";
        std::cin >> id;

        Medication med{id, "", 0, "", ""};

        std::cout << ctrl.find(med) << std::endl;
}