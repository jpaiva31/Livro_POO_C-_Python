#ifndef POLITICOS_H_INCLUDED
#define POLITICOS_H_INCLUDED
using namespace std;
class Politico{
private:
    string nome;
    string partido;
    string estado;
    string funcao;
    float salario;
public:
    Politico();
    ~Politico();
    void setNome(string);
    void setPartido(string);
    void setEstado(string);
    void setFuncao(string);
    void apresentacao();
    void setSalario(float);
    float getSalario();
    string getPartido();
    string getNome();
    string getEstado();
    string getFuncao();
};

#endif // POLITICOS_H_INCLUDED
