#include <catch2/catch_test_macros.hpp>
#include <toto/toto.h>

TEST_CASE("toto::functionName" ){
    REQUIRE(toto::functionNameF(1.0f));
    REQUIRE_FALSE(toto::functionNameF(-1.0f));
}
