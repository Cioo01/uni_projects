//
// Created by Kuba on 29.11.2021.
//
#include <iostream>
#include <string>
#include <vector>
#include "Mebel.h"
using namespace std;
#ifndef UNTITLED10_KRZESLO_H
#define UNTITLED10_KRZESLO_H


class Krzeslo:public Mebel{
private:
    int id;
public:
    Krzeslo(string name, string material, float weight, float price, int id);
    void updateKrzesloId(int nId);
    void showKrzesloData();
};



#endif //UNTITLED10_KRZESLO_H
