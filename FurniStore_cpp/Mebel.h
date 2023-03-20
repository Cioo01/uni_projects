//
// Created by Kuba on 29.11.2021.
//
#include <iostream>
#include <string>
#include <vector>

using namespace std;
#ifndef UNTITLED10_MEBEL_H
#define UNTITLED10_MEBEL_H


class Mebel {
protected:

    string name, material;
    float weight, price;
public:

    void updateName(string nName);
    void updateMaterial(string nMaterial);
    void updateWeight(float nWeight);
    void updatePrice(float nPrice);

    Mebel(string name, string material, float weight, float price);
};


#endif //UNTITLED10_MEBEL_H
