//
// Created by Kuba on 29.11.2021.
//
#include <iostream>
#include <string>
using namespace std;
#include "Krzeslo.h"


Krzeslo::Krzeslo(string name, string material, float weight, float price, int id): Mebel(name, material, weight, price), id(id){}

void Krzeslo::updateKrzesloId(int nId) {
    id = nId;
}

void Krzeslo::showKrzesloData() {
    cout << "name: " << this -> name << " | " << "material: " << this -> material << " | " << "weight: " << this -> weight << " | " << "price: " << this -> price << " | " << "id: "  << this -> id << endl;
}
