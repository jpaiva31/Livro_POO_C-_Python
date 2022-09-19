#include <iostream>

using namespace std;
class Politico
{
protected:
    string nome;
    string partido;
    string estado;
    string funcao;
    float salario;
public:
    Politico() {}
    ~Politico() {}
    void setNome(string a)
    {
        nome=a;
    }
    void setPartido(string a)
    {
        partido = a;
    }
    void setEstado(string a)
    {
        estado = a;
    }
    void setFuncao(string a)
    {
        funcao = a;
    }
    void apresentacao()
    {
        cout<<"Ola, sou "<<getNome()<<endl;
        cout<<"Meu partido eh "<<getPartido()<<endl;
    }
    void setSalario(float a)
    {
        salario = a;
    }
    float getSalario()
    {
        return salario;
    }
    string getPartido()
    {
        return partido;
    }
    string getNome()
    {
        return nome;
    }
    string getEstado()
    {
        return estado;
    }
    string getFuncao()
    {
        return funcao;
    }
};

class Prefeito:public Politico
{
private:
    string municipio;
public:
    Prefeito(string nome, string partido, string municipio, string estado)
    {
        setNome(nome);
        setPartido(partido);
        setMunicipio(municipio);
        setEstado(estado);
        setFuncao("administrar o IPTU visando o melhor para a cidade");
        setSalario(1000);
    }
    ~Prefeito()
    {
        setNome("");
        setPartido("");
        setEstado("");
        setMunicipio("");
    }

    void setMunicipio(string a)
    {
        municipio = a;
    }
    string getMunicipio()
    {
        return municipio;
    }
    void apresentacao()
    {
        Politico::apresentacao();
        cout<<"Sou prefeito em "<<getMunicipio()<<"/"<<getEstado()<<endl;
        cout<<"Minha funcao eh "<<getFuncao()<<endl;
        cout<<"Meu suposto salario eh "<<getSalario()<<endl;
    }
};

class Vereador:public Politico
{
private:
    string municipio;
public:
    Vereador(string nome, string partido, string municipio, string estado)
    {
        setNome(nome);
        setPartido(partido);
        setMunicipio(municipio);
        setEstado(estado);
        setFuncao("Propor leis em beneficio da populacao");
        setSalario(800);
    }
    ~Vereador()
    {
        setNome("");
        setPartido("");
        setEstado("");
        setMunicipio("");
    }
    void setMunicipio(string a)
    {
        municipio = a;
    }
    string getMunicipio()
    {
        return municipio;
    }
    void apresentacao()
    {
        Politico::apresentacao();
        cout<<"Sou vereador em "<<getMunicipio()<<"/"<<getEstado()<<endl;
        cout<<"Minha funcao eh "<<getFuncao()<<endl;
        cout<<"Meu suposto salario eh "<<getSalario()<<endl;
    }
};


int main()
{
    Prefeito *a = NULL;
    Vereador *b = NULL;
    a = new Prefeito("aa", "bb", "cc", "dd");
    b = new Vereador("ee", "ff", "gg", "hh");
    a->apresentacao();
    b->apresentacao();
    return 0;
}
