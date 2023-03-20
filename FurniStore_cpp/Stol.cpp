//
// Created by Kuba on 29.11.2021.
//
#include <iostream>
#include <string>
#include "Mebel.h"
using namespace std;
#include "Stol.h"

Stol::Stol(string name, string material, float weight, float price, int id): Mebel(name, material, weight, price), id(id){}

void Stol::updateStolId(int nId){
    id = nId;
}

void Stol::showStolData() {
    cout << "name: " << this -> name << " | " << "material: " << this -> material << " | " << "weight: " << this -> weight << " | " << "price: " << this -> price << " | " << "id: "  << this -> id << endl;
}