
//
// Created by Kuba on 29.11.2021.
//
#include <string>
#include "Mebel.h"
using namespace std;


Mebel::Mebel(string name, string material, float weight, float price):name(name), material(material), weight(weight), price(price){}

void Mebel::updateName(string nName) {
    name = nName;
}

void Mebel::updateMaterial(string nMaterial) {
    material = nMaterial;
}

void Mebel::updateWeight(float nWeight) {
    weight = nWeight;
}

void Mebel::updatePrice(float nPrice) {
    price = nPrice;
}

