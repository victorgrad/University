#pragma once

#include <string>

class Proiect
{
public:
	Proiect(const std::string& nume, const std::string& tip, const float& buget_alocat, const float& buget_estimat) :nume{ nume }, tip{ tip }, buget_alocat{ buget_alocat }, buget_estimat{ buget_estimat }{}

	std::string get_nume() const {
		return nume;
	}

	std::string get_tip() const {
		return tip;
	}

	float get_buget_alocat() const {
		return buget_alocat;
	}

	float get_buget_estimat() const {
		return buget_estimat;
	}

	void set_buget_alocat(const float& buget_nou) {
		buget_alocat = buget_nou;
	}


private:
	std::string nume, tip;
	float buget_alocat, buget_estimat;
};