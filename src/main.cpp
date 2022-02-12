/*
** EPITECH PROJECT, 2022
** Jam1
** File description:
** main
*/

#include "Core.hpp"

#define UNUSED __attribute((unused))

int main(UNUSED int ac, UNUSED char *av[])
{
    Core core;

    try {
        core.run();
    } catch (...) {
        return 84;
    }
    return 0;
}