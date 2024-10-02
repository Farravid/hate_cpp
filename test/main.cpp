// #define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN

// #include <doctest/doctest.h>

#include <gtest/gtest.h>

TEST(TestCategory, TestVersion) 
{
  	EXPECT_EQ(std::string("1.0"), std::string("1.0"));
}

int main(int argc, char **argv) {
  testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}