#include <catch2/catch_test_macros.hpp>
#include <lib_name/lib_name.h>

TEST_CASE("functionNameF") {
    REQUIRE(libname::functionNameF(1.0f));
    REQUIRE_FALSE(libname::functionNameF(-1.0f));
}
