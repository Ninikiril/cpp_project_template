#include <iostream>
#include <cmath>
#include <lib/lib.hpp>

#define ASSERT_APPROX_EQUAL(a, b, epsilon) \
    if (std::fabs((a) - (b)) > (epsilon)) { \
        std::cerr << "Assertion failed: (" << #a << " == " << #b << "), " \
                  << "actual: " << (a) << " vs " << (b) << std::endl; \
        return 1; \
    }

int main() {
    ASSERT_APPROX_EQUAL(Q_rsqrt(4.0), 0.5, 1e-2);
    ASSERT_APPROX_EQUAL(Q_rsqrt(9.0), 0.33, 1e-2);
    ASSERT_APPROX_EQUAL(Q_rsqrt(16.0), 0.25, 1e-2);
    ASSERT_APPROX_EQUAL(Q_rsqrt(1.0), 1.0, 1e-2);
    ASSERT_APPROX_EQUAL(Q_rsqrt(2.25), 0.67, 1e-2);

    std::cout << "All tests passed!" << std::endl;
    return 0;
}