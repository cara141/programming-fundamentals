#pragma once
#include "Domain.h"
#include <vector>
#include <ostream>

class Repository{
public:
    Repository() = default;

    Repository(const Repository &repo);

    Repository &operator=(const Repository &repo) = default;

    ~Repository() = default;

    Repository &operator=(Repository &&repo) = default;

    Repository(Repository &&repo) = default;

    [[nodiscard]] int size() const;

    [[nodiscard]] const Medication &element(const int &i) const;

    Repository &add(const Medication &med);

    Repository &remove(const Medication &med);

    [[nodiscard]] int find(const Medication &med) const;

    Repository &modify(const Medication &med, const Medication &new_med);

    [[nodiscard]] const std::vector<Medication> &getAll() const;


private:
    std::vector<Medication> list;
};