import glm

class Camera:
    def __init__(self, win_size, size, transform):
        self.__win_size__ = win_size
        self.__size__ = size
        self.__transform__ = transform

        self.__changed__ = False

        self.__calc_proj__()
        self.__calc_view_proj__()
        
    def __calc_proj__(self):
        scale_w = self.__win_size__[0] / (self.__size__[0]*2)
        scale_h = self.__win_size__[1] / (self.__size__[1]*2)
        w, h = self.__win_size__
        self.__projection__ = glm.mat3(
            (scale_w,    0   , 0 ),
            (   0   , scale_h, 0 ),
            (  w//2 ,   h//2 , 1 )
        )
        self.__changed__ = True
    
    def __calc_view_proj__(self):
        self.__view_proj__ = self.__projection__ * glm.inverse(glm.translate(glm.mat3(self.__transform__.scale), self.__transform__.position))
        self.__changed__ = False

    def get_view_proj(self):
        if self.__changed__:
            self.__calc_view_proj__()
        return self.__view_proj__
    