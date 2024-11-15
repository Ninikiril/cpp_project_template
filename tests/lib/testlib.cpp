#include <catch2/catch_test_macros.hpp>
#include <lib/lib.hpp>

TEST_CASE("f_example") {
    REQUIRE(f_example(1.0f));
    REQUIRE_FALSE(f_example(-1.0f));
}