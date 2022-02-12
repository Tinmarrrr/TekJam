/*
** EPITECH PROJECT, 2022
** Jam1
** File description:
** Core
*/

#include "Core.hpp"

Core::Core() :
    _window(sf::VideoMode(1920, 1080), "My window")
{
}

Core::~Core()
{
}

void Core::run()
{
    while (_window.isOpen()) {
       handleEvents();
    }
}

void Core::handleEvents()
{
    while (_window.pollEvent(_event)) {
        if (_event.type == sf::Event::Closed)
            _window.close();
    }
}