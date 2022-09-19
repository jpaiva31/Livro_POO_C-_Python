#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include "prefeito.h"
using namespace std;
Prefeito::Prefeito(string nome, string partido, string municipio, string estado){
    setNome(nome);
    setPartido(partido);
    setMunicipio(municipio);
    setEstado(estado);
    setFuncao("administrar o IPTU visando o melhor para a cidade\n");
}
Prefeito::~Prefeito(){
    setNome("");
    setPartido("");
    setEstado("");
    setMunicipio("");
}
void Prefeito::setMunicipio(string municipio){
    this->municipio = municipio;
}
string Prefeito::getMunicipio(){
    return this->municipio;
}
void Prefeito::apresentacao(){
Politico::apresentacao();
cout<<"Sou prefeito em "<<this->getNome()<<endl;
cout<<"Minha funcao é "<<this->getPartido()<<endl;
}
