import os
import subprocess
import sys
import argparse
import re

# TODO: Maybe being able to build standalone as Release and Test with debug?

def install_and_import(package):
    try:
        __import__(package)
    except ImportError:
        print(f"{package} not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    finally:
        globals()[package] = __import__(package)

def parse_command_line_arguments(): 
    parser = argparse.ArgumentParser(description= "Utility tool for building the different targets of project easily 😎")

    parser.add_argument('-d', '--default', action='store_true', help='Launchs the default build which is Standalone | Debug')
    parser.add_argument('-n', '--no-run', action='store_true', help='Skip running the targets after building it. By default these are executed')
    parser.add_argument('-i', '--install', action='store_true', help='Clean the build directory and install Conan dependencies. If the build folder does not exist, we will install by default no need to add -i flag')

    return parser.parse_args()

def get_build_config(args):
    if args.default:
        build = ['standalone']
        config = 'Debug'
    else:
        builds_question = [
            inquirer.Checkbox("builds",
                message="What do you want to build?",
                choices=["standalone", "test", "benchmark"],
                default=["standalone"],
            ),
        ]

        config_question = [
            inquirer.List("config",
                message="Debug or Release?",
                choices=["Debug", "Release"],
            ),
        ]

        build = inquirer.prompt(builds_question)['builds']
        config = inquirer.prompt(config_question)['config']
        
    return build, config

def perform_building(builds, config, avoid_running, project_name):
    for build in builds:
        print(f"\033[92m\n === Building {build} with configuration {config}... ===\n\033[0m")
        
        cmake_setup = f"cmake -S {build} -B build/{build} -DCMAKE_PREFIX_PATH=../build -DCMAKE_BUILD_TYPE={config}"
        cmake_build = f"cmake --build build/{build} -j4"

        subprocess.run(cmake_setup, shell=True)
        subprocess.run(cmake_build, shell=True)
    
    if avoid_running: return

    for build in builds:
        target_name = project_name + "_" + build
        #if build == "standalone":
        #    target_name = project_name

        run_command = f"./build/{build}/{target_name}" 
        subprocess.run(run_command, shell=True)

def install_conan_dependencies(force_install):
    if force_install:
        subprocess.run("rm -rf ./build", shell=True)
    elif os.path.isdir('./build'):
        return
    
    subprocess.run("conan install . --output-folder=build --build=missing", shell=True)

def get_cmake_project_name():
    with open('./CMakeLists.txt', 'r') as cmake_file:
        cmake_content = cmake_file.read()
    
    match = re.search(r'project\((\w+)', cmake_content, re.IGNORECASE)

    if match: return match.group(1)
    else: return None

def main():
    install_and_import('inquirer')

    args = parse_command_line_arguments()

    builds, config = get_build_config(args)

    install_conan_dependencies(args.install)
    project_name = get_cmake_project_name()

    perform_building(builds, config, args.no_run, project_name)

if __name__ == "__main__":
    main()