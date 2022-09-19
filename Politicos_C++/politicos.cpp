#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include "politicos.h"
using namespace std;
Politico::Politico(){}
Politico::~Politico(){}
void Politico::setNome(string nome){
    this->nome = nome;
}
void Politico::setPartido(string partido){
    this->partido = partido;
}
void Politico::setEstado(string estado){
    this->estado = estado;
}
void Politico::setFuncao(string funcao){
    this->funcao = funcao;
}
void Politico::setSalario(float salario){
    this->salario = salario;
}
float Politico::getSalario(){
    return this->salario;
}
void Politico::apresentacao(){
cout<<"Olá, sou "<<this->getNome()<<endl;
cout<<"Meu partido é "<<this->getPartido()<<endl;
}
string Politico::getNome(){
    return this->nome;
}
string Politico::getPartido(){
    return this->partido;
}
string Politico::getEstado(){
    return this->estado;
}
string Politico::getFuncao(){
    return this->funcao;
}
