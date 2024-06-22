import pygame
pygame.init()
WIDTH = 800

HEIGHT = 800

screen = pygame.display.set_mode([WIDTH, HEIGHT])

pygame.display.set_caption('Trò chơi Cờ vua 2 người chơi')

font = pygame.font.Font('freesansbold.ttf', 20)

medium_font = pygame.font.Font('freesansbold.ttf', 40)

big_font = pygame.font.Font('freesansbold.ttf', 50)

timer = pygame.time.Clock()

fps = 60


white_pieces = ['xe', 'mã', 'tượng', 'vua', 'hậu', 'tượng', 'mã', 'xe',

                'tốt', 'tốt', 'tốt', 'tốt', 'tốt', 'tốt', 'tốt', 'tốt']

white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]

black_pieces = ['xe', 'mã', 'tượng', 'vua', 'hậu', 'tượng', 'mã', 'xe',

                'tốt', 'tốt', 'tốt', 'tốt', 'tốt', 'tốt', 'tốt', 'tốt']

black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),(0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]

captured_pieces_white = []

captured_pieces_black = []

# 0 - lượt của người chơi trắng, chưa chọn quân cờ: 1 - lượt của người chơi trắng, đã chọn quân cờ:

# 2 - lượt của người chơi đen, chưa chọn quân cờ, 3 - lượt của người chơi đen, đã chọn quân cờ

turn_step = 0

selection = 100

valid_moves = []

hinh_anh_hau_trang = pygame.image.load('./images/hau_trang.png')

hinh_anh_hau_trang = pygame.transform.scale(hinh_anh_hau_trang, (80, 80))

hinh_anh_hau_trang_nho = pygame.transform.scale(hinh_anh_hau_trang, (45, 45))

hinh_anh_vua_trang = pygame.image.load('./images/vua_trang.png')

hinh_anh_vua_trang = pygame.transform.scale(hinh_anh_vua_trang, (80, 80))

hinh_anh_vua_trang_nho = pygame.transform.scale(hinh_anh_vua_trang, (45, 45))

hinh_anh_xe_trang = pygame.image.load('./images/xe_trang.png')

hinh_anh_xe_trang = pygame.transform.scale(hinh_anh_xe_trang, (80, 80))

hinh_anh_xe_trang_nho = pygame.transform.scale(hinh_anh_xe_trang, (45, 45))

hinh_anh_tuong_trang = pygame.image.load('./images/tuong_trang.png')

hinh_anh_tuong_trang = pygame.transform.scale(hinh_anh_tuong_trang, (80, 80))

hinh_anh_tuong_trang_nho = pygame.transform.scale(hinh_anh_tuong_trang, (45, 45))

hinh_anh_ma_trang = pygame.image.load('./images/ma_trang.png')

hinh_anh_ma_trang = pygame.transform.scale(hinh_anh_ma_trang, (80, 80))

hinh_anh_ma_trang_nho = pygame.transform.scale(hinh_anh_ma_trang, (45, 45))

hinh_anh_tot_trang = pygame.image.load('./images/tot_trang.png')

hinh_anh_tot_trang = pygame.transform.scale(hinh_anh_tot_trang, (65, 65))

hinh_anh_tot_trang_nho = pygame.transform.scale(hinh_anh_tot_trang, (45, 45))

hinh_anh_hau_den = pygame.image.load('./images/hau_den.png')

hinh_anh_hau_den = pygame.transform.scale(hinh_anh_hau_den, (80, 80))

hinh_anh_hau_den_nho = pygame.transform.scale(hinh_anh_hau_den, (45, 45))

hinh_anh_vua_den = pygame.image.load('./images/vua_den.png')

hinh_anh_vua_den = pygame.transform.scale(hinh_anh_vua_den, (80, 80))

hinh_anh_vua_den_nho = pygame.transform.scale(hinh_anh_vua_den, (45, 45))

hinh_anh_xe_den = pygame.image.load('./images/xe_den.png')

hinh_anh_xe_den = pygame.transform.scale(hinh_anh_xe_den, (80, 80))

hinh_anh_xe_den_nho = pygame.transform.scale(hinh_anh_xe_den, (45, 45))

hinh_anh_tuong_den = pygame.image.load('./images/tuong_den.png')

hinh_anh_tuong_den = pygame.transform.scale(hinh_anh_tuong_den, (80, 80))

hinh_anh_tuong_den_nho = pygame.transform.scale(hinh_anh_tuong_den, (45, 45))

hinh_anh_ma_den = pygame.image.load('./images/ma_den.png')

hinh_anh_ma_den = pygame.transform.scale(hinh_anh_ma_den, (80, 80))

hinh_anh_ma_den_nho = pygame.transform.scale(hinh_anh_ma_den, (45, 45))

hinh_anh_tot_den = pygame.image.load('./images/tot_den.png')

hinh_anh_tot_den = pygame.transform.scale(hinh_anh_tot_den, (65, 65))

hinh_anh_tot_den_nho = pygame.transform.scale(hinh_anh_tot_den, (45, 45))

board = pygame.image.load('./images/chess_board.jpg')

board = pygame.transform.scale(board, (800, 800))

# Hàm vẽ bàn cờ chính của trò chơi

def ve_ban_co():

    screen.blit(board, (0, 0))

# Hàm vẽ các quân cờ trên bàn cờ

def ve_quan_co():

    for i in range(len(white_pieces)):

        if white_pieces[i] == 'hậu':

            screen.blit(hinh_anh_hau_trang, (white_locations[i][0] * 100, white_locations[i][1] * 100))

        if white_pieces[i] == 'vua':

            screen.blit(hinh_anh_vua_trang, (white_locations[i][0] * 100, white_locations[i][1] * 100))

        if white_pieces[i] == 'xe':

            screen.blit(hinh_anh_xe_trang, (white_locations[i][0] * 100, white_locations[i][1] * 100))

        if white_pieces[i] == 'tượng':

            screen.blit(hinh_anh_tuong_trang, (white_locations[i][0] * 100, white_locations[i][1] * 100))

        if white_pieces[i] == 'ma':

            screen.blit(hinh_anh_ma_trang, (white_locations[i][0] * 100, white_locations[i][1] * 100))

        if white_pieces[i] == 'tốt':

            screen.blit(hinh_anh_tot_trang, (white_locations[i][0] * 100, white_locations[i][1] * 100))

    for i in range(len(black_pieces)):

        if black_pieces[i] == 'hậu':

            screen.blit(hinh_anh_hau_den, (black_locations[i][0] * 100, black_locations[i][1] * 100))

        if black_pieces[i] == 'vua':

            screen.blit(hinh_anh_vua_den, (black_locations[i][0] * 100, black_locations[i][1] * 100))

        if black_pieces[i] == 'xe':

            screen.blit(hinh_anh_xe_den, (black_locations[i][0] * 100, black_locations[i][1] * 100))

        if black_pieces[i] == 'tượng':

            screen.blit(hinh_anh_tuong_den, (black_locations[i][0] * 100, black_locations[i][1] * 100))

        if black_pieces[i] == 'ma':

            screen.blit(hinh_anh_ma_den, (black_locations[i][0] * 100, black_locations[i][1] * 100))

        if black_pieces[i] == 'tốt':

            screen.blit(hinh_anh_tot_den, (black_locations[i][0] * 100, black_locations[i][1] * 100))