#pragma once

#include "repo.h"
#include <vector>

class Service
{
public:
	Service(Repository& repo) :repo{ repo } {}
	std::vector<Proiect>& get_all() {
		return repo.get_all();
	}
	friend class GUI;

	float get_pierderi() {
		float pierdere = 0;
		for (const Proiect& pr : repo.get_all()) {
			if (pr.get_buget_estimat() > pr.get_buget_alocat())
				pierdere += pr.get_buget_estimat() - pr.get_buget_alocat();
		}
		return pierdere;
	}
private:
	Repository& repo;
};