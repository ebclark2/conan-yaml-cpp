#include <iostream>
#include <string>

#include <yaml-cpp/yaml.h>

int main() {
	YAML::Load("Hi").as<std::string>();
}
