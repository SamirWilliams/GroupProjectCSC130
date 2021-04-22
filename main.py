# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from developer import Developer


def main():
    # Use a breakpoint in the code line below to debug your script.
    print("Welcome to the Project Simulator")
    run_sim()


def run_sim():
    show_devs(create_developer_objects())


def create_developer_objects():
    developers = list()
    # create a list of 6 developer objects
    for i in range(0, 6):
        developers.append(Developer())

    return developers


def show_devs(list_of_devs):
    for dev in list_of_devs:
        print(dev)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
