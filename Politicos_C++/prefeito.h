#ifndef PREFEITO_H_INCLUDED
#define PREFEITO_H_INCLUDED
#include "politicos.h"
using namespace std;

class Prefeito:public Politico(){
private:
    string municipio;
public:
    Prefeito(string, string, string, string);
    ~Prefeito();

    void setMunicipio(string);
    string getMunicipio();
    void apresentacao();
};


#endif // PREFEITO_H_INCLUDED
