#include <test_lib/lib.hpp>
#include <vector>

int main() {
    std::vector<float> input = {1.2, 2.3, 3.4, 4.5};
    std::vector<float> output(input.size());
    for(size_t i = 0; i < input.size(); ++i) {
        output[i] = Q_rsqrt(input[i]);
    }
    printf("Output: ");
    for(auto& o : output) {
        printf("%f ", o);
    }

    return 0;
}
