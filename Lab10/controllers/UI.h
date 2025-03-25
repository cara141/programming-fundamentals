#pragma once
#include "Controller.h"

class UI{
public:
    UI() = default;

    void run();

    void add();

    void remove();

    void modify();

    void printAll();

    void find();

private:
    Controller ctrl = Controller();
};