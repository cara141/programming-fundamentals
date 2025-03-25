#pragma once
#include "Repository.h"

class Controller{
public:
    Controller() = default;

    [[nodiscard]] const Repository &getRepository() const;

    Controller &add(const Medication &med);

    Controller &remove(const Medication &med);

    Controller &modify(const Medication &med, const Medication &newMed);

    [[nodiscard]] const Medication &find(const Medication &med) const;

    [[nodiscard]] const std::vector<Medication> &getAll() const;


private:
    Repository repo = Repository();
};
