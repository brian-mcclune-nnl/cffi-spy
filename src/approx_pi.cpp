#include <cassert>

#include "approx_pi.h"

double leibniz(int n) {
    assert(n >= 0);

    double pi_over_4{1.};
    double s{1.};
    for (int i = 1; i <= n; ++i) {
        s = -s;
        pi_over_4 += s / (2. * i + 1.);
    }
    return 4. * pi_over_4;
}

double wallis(int n) {
    assert(n >= 0);

    double pi_over_2{1.};
    for (int i = 1; i <= n; ++i) {
        pi_over_2 *= 4. * i * i / (4. * i * i - 1.);
    }
    return 2. * pi_over_2;
}
