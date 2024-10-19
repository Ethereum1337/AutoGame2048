import random
import time
import os
from twentyfortyeight.game import Game
from twentyfortyeight.display import Display

# 初始化游戏
game = Game(4)  # 4x4 网格
display = Display(game, keep_open=True)


def random_move(game):
    """随机选择一个有效的移动方向"""
    valid_moves = game.get_valid_moves()
    if valid_moves:
        return random.choice(valid_moves)
    return None


try:
    while True:
        # 打印当前游戏状态（可选）
        display.render()
        time.sleep(0.5)  # 等待一段时间，以便观察当前状态

        # 随机选择一个有效的移动
        move = random_move(game)
        if move is None:
            print("Game Over! No valid moves left.")
            break

            # 执行移动
        game.move(move)

        # 检查游戏是否结束
        if game.is_game_over():
            print("Game Over! Final score:", game.get_score())
            break

finally:
    # 清理窗口（如果使用pygame等图形库时需要）
    display.close()