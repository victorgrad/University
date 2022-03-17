#pragma once

#include "dom.h"
#include <vector>
#include <fstream>
#include <exception>

class Repository
{
public:
	Repository(std::string filename) :filename{ filename } {
		loadFromFile();
	}
	std::string filename;
	std::vector<Proiect>& get_all();
	friend class Service;

private:
	std::vector<Proiect> proiecte;
	void loadFromFile();
};