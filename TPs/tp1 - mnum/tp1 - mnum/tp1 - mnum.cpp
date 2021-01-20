#define _USE_MATH_DEFINES
#include <iostream>
#include<cmath>
using namespace std;

const double E_CONST = 2.718281828;

void tp1() {
    //double value = M_E - 1;
    double value = E_CONST - 1;

    for (int i = 1; i <= 25; i++) {
        value = value * (double)i - (double)1;
        cout << "fim de " << i << "ano multiplicamos o seu capital por " << i << " e subtraímos 1 euro para despesas administrativas -> "
            << value << endl << endl;
    }

    // With M_E: End Value = -2.2 ... e+9
    // With 2.718281828: End Value = -7.1 ... e+15
    // With 2.718: End Value = -4.3715e+21
    // With 2.72: End Value = 2.66509e+22
}

int main()
{
    tp1();
}
