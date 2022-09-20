#include <iostream>
#include <queue>
using namespace std;
class Pessoa
{
private:
    string nome;
    int idade;
public:
    Pessoa(string a, int b)
    {
        nome = a;
        idade = b;
    }
    string getNome()
    {
        return nome;
    }
    int getIdade()
    {
        return idade;
    }


};

class filaAtendimento
{
private:
    queue<Pessoa> fila;
    queue<Pessoa> filaP;
    int qtd;
public:
    filaAtendimento()
    {
        cout<<"Construtor da fila"<<endl;
        qtd=0;
    }
    ~filaAtendimento()
    {
        cout<<"Destrutor da Fila"<<endl;
        while(filaP.empty()!=1)filaP.pop();
        while(fila.empty()!=1)fila.pop();

        mostrarFila();
    }
    void adicionar(string nome, int idade)
    {
        Pessoa aux(nome,idade);
        if(idade>=60)filaP.push(aux);
        else fila.push(aux);
    }
    void atender()
    {
        if (filaP.size()==0)
        {
            Pessoa aux=fila.front();
            cout<<"Atendendo "<<aux.getNome()<<"- "<<aux.getIdade()<<" anos - atendimento normal"<<endl;
            fila.pop();
        }
        else
        {
            Pessoa aux=filaP.front();
            cout<<"Atendendo "<<aux.getNome()<<"- "<<aux.getIdade()<<" anos - atendimento prefencial"<<endl;
            filaP.pop();
        }
    }

    void mostrarFila()
    {
        if(filaP.size() == 0 and fila.size() == 0)cout<<"Lista vazia!"<<endl;
        else
        {
            if(filaP.size()>0)
            {
                cout<<"Os pacientes com atendimento preferencial nao atendidos:"<<endl;
                queue<Pessoa> aux=filaP;
                for(int i=0; i<filaP.size(); i++)
                {
                    Pessoa auxP= aux.front();
                    cout<<"Nome: "<<auxP.getNome()<<" idade: "<<auxP.getIdade()<<endl;
                    aux.pop();
                }
            }
            if(fila.size()>0)
            {
                cout<<"Os pacientes nao atendidos:"<<endl;
                queue<Pessoa> aux=fila;
                for(int i=0; i<fila.size(); i++)
                {
                    Pessoa auxP= aux.front();
                    cout<<"Nome: "<<auxP.getNome()<<" idade: "<<auxP.getIdade()<<endl;
                    aux.pop();
                }
            }

        }
    }
};

int main()
{
    filaAtendimento fila;
    fila.mostrarFila();
    fila.adicionar("Orlando", 34);
    fila.adicionar("Maria", 64);
    fila.adicionar("Ana", 33);
    fila.adicionar("Lucas", 4);
    fila.adicionar("Paulo", 65);
    fila.adicionar("Ilma", 70);
    fila.atender();
    fila.atender();
    fila.mostrarFila();
}
