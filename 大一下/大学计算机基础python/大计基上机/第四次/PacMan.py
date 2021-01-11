class PacMan():
    '''
    本类表示游戏过程：
    player属性为一个包含两个元素的列表，记录人的位置；
    food属性为一个包含两个元素的列表，记录食物的位置；
    monster属性为一个包含两个元素的列表，记录怪物的位置；
    is_alive属性记录是否存活；
    score属性记录得分。
    '''
    def __init__(self, px, py, fx, fy, mx, my):
        '''
        本方法为该类的构造方法，需使用PacMan(px, py, fx, fy, mx, my)来实例化对象。
        :param px: px参数表示人的初始位置的横坐标。
        :param py: py参数表示人的初始位置的纵坐标。
        :param fx: fx参数表示食物位置的横坐标。
        :param fy: fy参数表示食物位置的纵坐标。
        :param mx: mx参数表示怪物位置的横坐标。
        :param my: my参数表示怪物位置的纵坐标。
        '''
        self.player = [px, py]
        self.food = [fx, fy]
        self.monster = [mx, my]
        self.is_alive = True #
        self.score = 0
        self.check_status()
        self.check_score()
 
    def check_status(self):
        '''
        本方法检查人物是否存活。
        '''
        if self.player == self.monster:
            self.is_alive = False
 
    def check_score(self):
        '''
            本方法检查是否得分。
        '''
        if self.player == self.food:
            self.score = 1
 
    def move(self, direc):
        '''
        本方法对人物进行移动。
        :param direc: 参数direc为一个字符串，是'up'，'left'，'right'，'down'中的一种，表示运行方向
        '''
        if direc == 'up':
            self.player[1] += 1
        if direc == 'down':
            self.player[1] -= 1
        if direc == 'left':
            self.player[0] -= 1
        if direc == 'right':
            self.player[0] += 1
        self.check_status()
        self.check_score()
