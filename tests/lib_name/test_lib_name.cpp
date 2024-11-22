#include <catch2/catch_test_macros.hpp>
#include <lib_name/lib_name.h>

TEST_CASE("lib_name::functionName" ){
    REQUIRE(lib_name::functionNameF(1.0f));
    REQUIRE_FALSE(lib_name::functionNameF(-1.0f));
}
