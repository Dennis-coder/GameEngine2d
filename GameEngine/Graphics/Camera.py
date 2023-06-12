import glm
import pygame as pg

class Camera:
    def __init__(self, win_size, size, transform):
        self.__win_size__ = win_size
        self.__size__ = size
        self.__transform__ = transform

        self.__changed__ = False

        self.__calc_proj__()
        self.__calc_view_proj__()
        
    def __calc_proj__(self):
        _, h = self.__win_size__
        scale = h / (self.__size__*2)
        self.__projection__ = glm.transpose(glm.mat4(
            (scale,   0  ,  0 , 320),
            (  0  , scale,  0 , 180),
            (  0  ,   0  , -1 ,  0 ),
            (  0  ,   0  ,  0 ,  1 )
        ))
        self.__changed__ = True
    
    def __calc_view_proj__(self):
        self.__view_proj__ = self.__projection__ * glm.inverse(self.__transform__.__matrix__)
        self.__changed__ = False

    def get_view_proj(self):
        if self.__changed__:
            self.__calc_view_proj__()
        return self.__view_proj__
    