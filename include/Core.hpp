/*
** EPITECH PROJECT, 2022
** Jam1
** File description:
** Core
*/

#ifndef CORE_HPP_
#define CORE_HPP_

#include <SFML/Window.hpp>

class Core {
    public:
        Core();
        ~Core();

        void run();

    private:
        void handleEvents();

        sf::Window _window;
        sf::Event _event;
};

#endif /* !CORE_HPP_ */