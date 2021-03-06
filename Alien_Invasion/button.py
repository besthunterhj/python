import pygame.font


class Button():

    def __init__(self, ai_settings, screen, msg, offset, color):
        """初始化按钮属性"""
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.msg_image = None
        self.msg_image_rect = None

        # 设置按钮的尺寸和其他属性
        self.width, self.height = 200, 50
        self.button_color = color
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont("Consolas", 48)

        # 创建按钮的rect对象，并使其居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centery = self.screen_rect.centery
        self.rect.centerx = self.screen_rect.centerx + offset

        # 按钮的标签只需要创建一次
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """将msg渲染为图像，并使其在按钮上居中"""
        # 该语句为创建按钮的核心语句，利用的是msg形参和类的成员变量
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """绘制一个用颜色填充的按钮，再绘制文本"""
        self.screen.fill(self.button_color, self.rect)  # 用颜色填充矩形
        self.screen.blit(self.msg_image, self.msg_image_rect)   # 将图像放入矩形中
