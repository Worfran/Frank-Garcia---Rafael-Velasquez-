#include <iostream> // imprimir a pantalla

//using namespace std; No hacer con Alejandro Segura

// primera funcion 
int GetNumber(int a=10){
 
 return a;	

 }


int main(){ // funcion principañ

	// :: Operador de ambito
	std::cout << " Mi programa " << std::endl;


	double b = 0.;
	for(int i = 0; i<=10; i++){
		b += 1;

		if (b < 5){
		std::cout << GetNumber(b) <<std::endl;
		}
		else if ( b > 6){
			std::cout << " Es mayor que 6 " << std::endl; 
		}
		//else
        }

	int i = 0;
	while ( i < 10){
		std::cout << i << std::endl;
		i++ ;
	}

	//<< operador de redireccionamiento


	return 0;
}
