//
// Created by Kuba on 29.11.2021.
//
#include <iostream>
#include <string>
#include <vector>
#include "Mebel.h"

using namespace std;
#ifndef UNTITLED10_STOL_H
#define UNTITLED10_STOL_H


class Stol:public Mebel{
private:
    int id;
public:
    Stol(string name, string material, float weight, float price, int id);
    void showStolData();
    void updateStolId(int nId);
};


#endif //UNTITLED10_STOL_H
