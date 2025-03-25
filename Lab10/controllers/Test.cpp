#include "Test.h"
#include <iostream>

void testDomain(){

    auto med1 = Medication();
    auto med2 = Medication();
    auto med3 = Medication();

    assert(med1.getId() == 0);
    assert(med2.getName().empty());
    assert(med3.getPrice() == 0);
    assert(med1.getProducer().empty());
    assert(med2.getSubstance().empty());

    med1 = Medication(1, "Med1", 15.50, "Pharma1", "Subst1");

    assert(med1.getId() == 1);
    assert(med1.getName() == "Med1");
    assert(med1.getPrice() == 15.50);
    assert(med1.getProducer() == "Pharma1");
    assert(med1.getSubstance() == "Subst1");

    med2 = Medication(med1);

    assert(med1 == med2);

    assert(med1 != med3);

    med1.setId(11);
    assert(med1.getId() == 11);

    med1.setName("Med11");
    assert(med1.getName() == "Med11");

    med1.setPrice(30);
    assert(med1.getPrice() == 30);

    med1.setProducer("Pharma11");
    assert(med1.getProducer() == "Pharma11");

    med1.setSubstance("Subst11");
    assert(med1.getSubstance() == "Subst11");

}

void testRepo(){

    Medication med1 = Medication(1, "Med1", 115.50, "Pharma1", "Subst1");
    Medication med2 = Medication(2, "Med2", 165.50, "Pharma2", "Subst2");
    Medication med3 = Medication(3, "Med3", 135.50, "Pharma3", "Subst2");
    Medication med4 = Medication(4, "Med4", 145.50, "Pharma4", "Subst1");
    Medication med5 = Medication(5, "Med5", 115.50, "Pharma5", "Subst1");

    Repository repo1 = Repository();

    repo1.add(med1).add(med2).add(med3).add(med4);
    assert(repo1.size() == 4);
    assert(repo1.element(2).getId() == 3);
    repo1.remove(med2).remove(med3);
    assert(repo1.size() == 2);
    repo1.modify(med1, med5);
    assert(repo1.size() == 2);
    assert(repo1.element(0).getId() == 5);

    try{
        repo1.add(med4);
        assert(false);
    }
    catch(std::invalid_argument &e){
        ;
    }

    try{
        repo1.remove(med1);
        assert(false);
    }
    catch(std::invalid_argument &e){
        ;
    }

    try{
        repo1.modify(med1, med4);
        assert(false);
    }
    catch(std::invalid_argument &e){
        ;
    }

    Repository repo2 = Repository(repo1);
}

void testController(){

        Medication med1 = Medication(1, "Med1", 115.50, "Pharma1", "Subst1");
        Medication med2 = Medication(2, "Med2", 165.50, "Pharma2", "Subst2");
        Medication med3 = Medication(3, "Med3", 135.50, "Pharma3", "Subst2");
        Medication med4 = Medication(4, "Med4", 145.50, "Pharma4", "Subst1");
        Medication med5 = Medication(5, "Med5", 115.50, "Pharma5", "Subst1");

        Controller ctrl = Controller();

        ctrl.add(med1).add(med2).add(med3).add(med4);
        assert(ctrl.getAll().size() == 4);
        assert(ctrl.find(med3).getId() == 3);
        ctrl.remove(med2).remove(med3);
        assert(ctrl.getAll().size() == 2);
        ctrl.modify(med1, med5);
        assert(ctrl.getAll().size() == 2);
        assert(ctrl.find(med5).getId() == 5);

        //test getRepository
        assert(ctrl.getRepository().size() == 2);

        try{
            ctrl.add(med5);
            assert(false);
        }
        catch(std::invalid_argument &e){
            ;
        }

        try{
            ctrl.remove(med2);
            assert(false);
        }
        catch(std::invalid_argument &e){
            ;
        }

        try{
            ctrl.modify(med3, med4);
            assert(false);
        }
        catch(std::invalid_argument &e){
            ;
        }

        try{
            med1 = ctrl.find(med3);
            assert(false);
        }
        catch(std::invalid_argument &e){
            ;
        }

        Controller ctrl2 = Controller(ctrl);

}

void testAll(){
    testDomain();
    testRepo();
    testController();
}