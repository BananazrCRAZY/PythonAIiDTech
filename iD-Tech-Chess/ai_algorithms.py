# Import Modules & Libraries
import global_vars as G
import display_gui as gui
import chess, random, time

# Select Random Move
def select_random():
    move_list = list(G.BOARD.legal_moves)
    move_count = len(move_list)
    random_num = random.randint(0, move_count-1)
    return move_list[random_num]

# Get Game Status
def cal_game_status():
    if G.BOARD.is_checkmate():
        if G.BOARD.turn:
            return -9999
        else:
            return 9999
    elif G.BOARD.is_stalemate():
        return 0
    elif G.BOARD.is_insufficient_material():
        return 0
    elif G.BOARD.is_seventyfive_moves():
        return 0
    elif G.BOARD.is_fivefold_repetition():
        return 0
    else:
        return "CONTINUE"

# Get Board Score
def calc_board_score():
    game_status = cal_game_status()
    if game_status != "CONTINUE":
        return game_status

    w_pawns = G.BOARD.pieces(chess.PAWN, chess.WHITE)
    w_knights = G.BOARD.pieces(chess.KNIGHT, chess.WHITE)
    w_bishops = G.BOARD.pieces(chess.BISHOP, chess.WHITE)
    w_rooks = G.BOARD.pieces(chess.ROOK, chess.WHITE)
    w_queens = G.BOARD.pieces(chess.QUEEN, chess.WHITE)
    w_kings = G.BOARD.pieces(chess.KING, chess.WHITE)

    w_score_p = sum([G.pawn_score[p] for p in w_pawns])
    w_score_n = sum([G.knight_score[p] for p in w_knights])
    w_score_b = sum([G.bishop_score[p] for p in w_bishops])
    w_score_r = sum([G.rook_score[p] for p in w_rooks])
    w_score_q = sum([G.queen_score[p] for p in w_queens])
    w_score_k = sum([G.king_score[p] for p in w_kings])

    b_pawns = G.BOARD.pieces(chess.PAWN, chess.BLACK)
    b_knights = G.BOARD.pieces(chess.KNIGHT, chess.BLACK)
    b_bishops = G.BOARD.pieces(chess.BISHOP, chess.BLACK)
    b_rooks = G.BOARD.pieces(chess.ROOK, chess.BLACK)
    b_queens = G.BOARD.pieces(chess.QUEEN, chess.BLACK)
    b_kings = G.BOARD.pieces(chess.KING, chess.BLACK)

    b_score_p = sum([-G.pawn_score[chess.square_mirror(p)] for p in b_pawns])
    b_score_n = sum([-G.knight_score[chess.square_mirror(p)] for p in b_knights])
    b_score_b = sum([-G.bishop_score[chess.square_mirror(p)] for p in b_bishops])
    b_score_r = sum([-G.rook_score[chess.square_mirror(p)] for p in b_rooks])
    b_score_q = sum([-G.queen_score[chess.square_mirror(p)] for p in b_queens])
    b_score_k = sum([-G.king_score[chess.square_mirror(p)] for p in b_kings])

    pawns = len(w_pawns) - len(b_pawns)
    knights = len(w_knights) - len(b_knights)
    bishops = len(w_bishops) - len(b_bishops)
    rooks = len(w_rooks) - len(b_rooks)
    queens = len(w_queens) - len(b_queens)

    material = (100 * pawns) + (320 * knights) + (330 * bishops)
    material = material + (500 * rooks) + (900 * queens)
    final = material + w_score_p + b_score_p + w_score_n + b_score_n
    final = final + w_score_b + b_score_b + w_score_r + b_score_r
    final = final + w_score_q + b_score_q + w_score_k + b_score_k

    if G.BOARD.turn:
        return final
    else:
        return -final

# Select Positional Move
def select_positional():
    best_move = chess.Move.null()
    best_score = -99999

    for move in G.BOARD.legal_moves:
        G.BOARD.push(move)
        score = -calc_board_score()
        G.BOARD.pop()

        if score > best_score:
            best_score = score
            best_move = move
    return best_move

# Negamax with Alpha-Beta Pruning
def negamax_ab(alpha, beta, depthleft):
    high_score = -9999
    if depthleft == 0:
        return calc_board_score()

    for move in G.BOARD.legal_moves:
        G.BOARD.push(move)
        score = -negamax_ab(-beta, -alpha, depthleft-1)
        G.BOARD.pop()

        if score >= beta:
            return score
        if score > high_score:
            high_score = score
        if score > alpha:
            alpha = score
    return high_score

# Quiescence Search

# Select Predictive Move
def select_predictive(depth):
    alpha = -100000
    beta = 100000
    best_score = -99999
    best_move = chess.Move.null()

    for move in G.BOARD.legal_moves:
        G.BOARD.push(move)
        board_score = -negamax_ab(-beta, -alpha, depth-1)
        G.BOARD.pop()

        if board_score > best_score:
            best_score = board_score
            best_move = move
        if board_score > alpha:
            alpha = board_score
    return best_move

# Complete AI Move
def make_ai_move(move, delay):
    time.sleep(delay)
    if move != chess.Move.null():
        gui.draw_board()
        gui.draw_select_square(move.from_square)
        gui.draw_select_square(move.to_square)
    gui.print_san(move)
    G.BOARD.push(move)