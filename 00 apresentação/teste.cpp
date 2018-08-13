#include <string>
#include <iostream>
#include <filesystem>
#define _UNICODE
#define UNICODE
// namespace fs = std::experimental::filesystem;

int main()
{
    std::string path = ".";
    for (auto & p : std::experimental::filesystem::directory_iterator(path))
        std::cout << p << std::endl;
    system("PAUSE");
}