//
// Created by Kuba on 29.11.2021.
//
#include <iostream>
#include <string>
#include "Kasa.h"
using namespace std;

Kasa::Kasa(){
    run = true;
}

void Kasa::createTable() {
    bool correct = false;
    string name, material, sWeight, sPrice, sId;
    float weight, price;
    int id;
    cout << "Enter properties of a table in given order: name, material, weight, price, id" << endl;
    while (!correct){
        cin >> name >> material >> sWeight >> sPrice >> sId;
        try{
            weight = stof(sWeight);
            price = stof(sPrice);
            id = stoi(sId);
            correct = true;
        }
        catch(...){
            cout << "Something went wrong, try again" << endl;
        }
    }
    stoly.emplace_back(name, material, weight, price, id);
    cout << "Table successfully created!\n";
}

void Kasa::createChair() {
    bool correct = false;
    string name, material, sWeight, sPrice, sId;
    float weight, price;
    int id;
    cout << "Enter properties of a chair in given order: name, material, weight, price, id" << endl;
    while (!correct){
        cin >> name >> material >> sWeight >> sPrice >> sId;
        try{
            weight = stof(sWeight);
            price = stof(sPrice);
            id = stoi(sId);
            correct = true;
        }
        catch(...){
            cout << "Something went wrong, try again" << endl;
        }
    }
    krzesla.emplace_back(name, material, weight, price, id);
    cout << "Chair successfully created! \n";
}

void Kasa::readChair(){
    for (int i = 0; i<krzesla.size(); i++){
        cout << "Krzeslo: " << i << endl;
        krzesla[i].showKrzesloData();
    }
}

void Kasa::readTable(){
    for (int i = 0; i<stoly.size(); i++){
        cout << "Stol: " << i << endl;
        stoly[i].showStolData();
    }
}

void Kasa::removeChair() {
    readChair();
    bool correct = false;
    bool deletionDone = false;
    int iDeleteChoice;
    while (!correct){
        string deleteChoice;
        cout << "Which chair would you like to delete? Type in the number of item you wish to delete.\n";
        cin >> deleteChoice;
        try{
            iDeleteChoice = stoi(deleteChoice);
            if (iDeleteChoice < 0 || iDeleteChoice > krzesla.size() - 1){
                continue;
            }
            correct = true;
        }
        catch(...){
            cout << "Something went wrong, try again\n";
        }

    while(!deletionDone && correct){
        try{
            krzesla.erase(krzesla.begin() + iDeleteChoice);
            deletionDone = true;
            cout << "Chair was deleted.\n" << endl;
            }
        catch(...){
            cout << "Something went wrong, try again";
        }
    }
    }

}

void Kasa::removeTable() {
    readTable();
    bool correct = false;
    bool deletionDone = false;
    int iDeleteChoice;
    while (!correct){
        string deleteChoice;
        cout << "Which table would you like to delete? Type in the number of item you wish to delete.\n";
        cin >> deleteChoice;
        try{
            iDeleteChoice = stoi(deleteChoice);
            if (iDeleteChoice < 0 || iDeleteChoice > stoly.size() - 1){
                continue;
            }
            correct = true;
        }
        catch(...){
            cout << "Something went wrong, try again\n";
        }

        while(!deletionDone && correct){
            try{
                stoly.erase(stoly.begin() + iDeleteChoice);
                deletionDone = true;
                cout << "Table was deleted.\n" << endl;
            }
            catch(...){
                cout << "Something went wrong, try again.\n";
            }
        }
    }

}

void Kasa::updateChair() {
    readChair();
    int iChairToUpdate;
    bool correct = false;
    bool updateDone = false;
    while (!correct){
        string chairToUpdate;
        cout << "Which chair would you like to update? Type in the number of item you wish to update.\n";
        try{
            cin >> chairToUpdate;
            iChairToUpdate = stoi(chairToUpdate);
            if (iChairToUpdate < 0 || iChairToUpdate > krzesla.size() - 1){
                continue;
            }
            correct = true;
        }
        catch(...){
            cout << "Something went wrong, try again.\n";
        }
    while (!updateDone && correct){
        string name, material, sWeight, sPrice, sId;
        float weight, price;
        int id;
        cout << "Enter the properties to update in given order: name, material, weight, price, id \n";
        cin >> name >> material >> sWeight >> sPrice >> sId;

        try{
            weight = stof(sWeight);
            price = stof(sPrice);
            id = stoi(sId);
        }
        catch(...){
            cout << "Something went wrong, try again.\n";
        }

        krzesla[iChairToUpdate].updateName(name);
        krzesla[iChairToUpdate].updateMaterial(material);
        krzesla[iChairToUpdate].updateWeight(weight);
        krzesla[iChairToUpdate].updatePrice(price);
        krzesla[iChairToUpdate].updateKrzesloId(id);
        cout << "Chair has been modified.\n";
        krzesla[iChairToUpdate].showKrzesloData();
        updateDone = true;

    }
    }
}

void Kasa::updateTable() {
    readTable();
    int iTableToUpdate;
    bool correct = false;
    bool updateDone = false;
    while (!correct){
        string tableToUpdate;
        cout << "Which table would you like to update? Type in the number of item you wish to update.\n";
        try{
            cin >> tableToUpdate;
            iTableToUpdate = stoi(tableToUpdate);
            if (iTableToUpdate < 0 || iTableToUpdate > stoly.size() - 1){
                continue;
            }
            correct = true;
        }
        catch(...){
            cout << "Something went wrong, try again.\n";
        }
        while (!updateDone && correct){
            string name, material, sWeight, sPrice, sId;
            float weight, price;
            int id;
            cout << "Enter the properties to update in given order: name, material, weight, price, id \n";
            cin >> name >> material >> sWeight >> sPrice >> sId;

            try{
                weight = stof(sWeight);
                price = stof(sPrice);
                id = stoi(sId);
            }
            catch(...){
                cout << "Something went wrong, try again.\n";
            }

            stoly[iTableToUpdate].updateName(name);
            stoly[iTableToUpdate].updateMaterial(material);
            stoly[iTableToUpdate].updateWeight(weight);
            stoly[iTableToUpdate].updatePrice(price);
            stoly[iTableToUpdate].updateStolId(id);
            cout << "Table has been modified.\n";
            stoly[iTableToUpdate].showStolData();
            updateDone = true;

        }
    }
}


void Kasa::start() {
    while(run){
        cout << "Choose one from the below to continue:\nC - to create an object\nR - to read an object\nU - to update an object\nD - to delete an object\nQ - to quit the program" << endl;
        cin >> choice;
        switch (choice) {
            case 'C': {
                string createChoice;
                cout << "Pick option\n1 - create chair\n2 - create table\n3 - go back" << endl;
                bool correct = false;
                while (!correct){
                    cin >> createChoice;
                    if (createChoice == "1"){
                        createChair();
                        correct = true;
                    }
                    else if (createChoice == "2"){
                        createTable();
                        correct = true;
                    }
                    else if(createChoice == "3") {
                        break;
                    }
                    else {
                        cout << "Wrong value, try again" << endl;
                    }
                }
            }
                break;
            case 'R': {
                if (krzesla.empty() && stoly.empty()){
                    cout << "There are no items to read, sorry. Why don't you create one instead?\n";
                    break;
                }
                string readChoice;
                cout << "Pick option\n1 - read chair\n2 - read table\n3 - go back" << endl;
                bool correct = false;
                while (!correct){
                    cin >> readChoice;
                    if (readChoice == "1"){
                        if (krzesla.empty()){
                            cout << "Sorry, can't read chairs, because there isn't one yet.\n";
                            break;
                        }
                        readChair();
                        correct = true;
                    }
                    else if (readChoice == "2"){
                        if (stoly.empty()){
                            cout << "Sorry, can't read tables, because there isn't one yet.\n";
                            break;
                        }
                        readTable();
                        correct = true;
                    }
                    else if (readChoice == "3") {
                        break;
                    }
                    else {
                        cout << "Wrong value, try again" << endl;
                    }
                }
            }
                break;
            case 'U':{
                if (krzesla.empty() && stoly.empty()){
                    cout << "There are no items to update, sorry. Why don't you create one instead?\n";
                    break;
                }
                string updateChoice;
                cout << "Pick option\n1 - update chair\n2 - update table\n3 - go back" << endl;
                bool correct = false;
                while (!correct){
                    cin >> updateChoice;
                    if (updateChoice == "1"){
                        if (krzesla.empty()){
                            cout << "Sorry, can't update any chair, because there isn't one yet.\n";
                            break;
                        }
                        updateChair();
                        correct = true;
                    }
                    else if (updateChoice == "2"){
                        if (stoly.empty()){
                            cout << "Sorry, can't update any table, because there isn't one yet.\n";
                            break;
                        }
                        updateTable();
                        correct = true;
                    }
                    else if(updateChoice == "3") {
                        break;
                    }
                    else {
                        cout << "Wrong value, try again\n" << endl;
                    }
                }
                break;
            }

            case 'D':{
                if (krzesla.empty() && stoly.empty()){
                    cout << "There are no items to delete, sorry. Why don't you create one instead?\n";
                    break;
                }
                string removeChoice;
                cout << "Pick option\n1 - remove chair\n2 - remove table\n3 - go back" << endl;
                bool correct = false;
                while (!correct){
                    cin >> removeChoice;
                    if (removeChoice == "1"){
                        if (krzesla.empty()){
                            cout << "Sorry, can't remove any chair, because there isn't one yet.\n";
                            break;
                        }
                        removeChair();
                        correct = true;
                    }
                    else if (removeChoice == "2"){
                        if (stoly.empty()){
                            cout << "Sorry, can't remove any table, because there isn't one yet.\n";
                            break;
                        }
                        removeTable();
                        correct = true;
                    }
                    else if (removeChoice == "3"){
                        break;
                    }
                    else {
                        cout << "Wrong value, try again.\n" << endl;
                    }
                }
                break;
            }
            case 'Q':{
                cout << "Quitting the program...\n" << endl;
                run = false;
            }
        }
    }
}