//
// Created by Kuba on 29.11.2021.
//
#include <iostream>
#include <string>
#include <vector>
#include "Mebel.h"
#include "Krzeslo.h"
#include "Stol.h"
using namespace std;
#ifndef UNTITLED10_KASA_H
#define UNTITLED10_KASA_H



class Kasa {
private:
    /*bool run;
    char choice;

    void readChair();
    void readTable();

    void removeChair();
    void removeTable();

    void createChair();
    void createTable();

    void updateChair();
    void updateTable();*/
protected:
    vector<Krzeslo> krzesla;
    vector<Stol> stoly;

    bool run;
    char choice;


public:
    Kasa();
    void start();
    void readChair();
    void readTable();

    void removeChair();
    void removeTable();

    void createChair();
    void createTable();

    void updateChair();
    void updateTable();
};


#endif //UNTITLED10_KASA_H
