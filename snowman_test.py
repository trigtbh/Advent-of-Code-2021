import runner, helper
import snowman
import os, shutil
os.system("cls")

shutil.rmtree(helper.nrml("__pycache__"))
@runner.test(return_val=((0, 6), (2, 9)))
def test_int_char_1():
    return snowman.snowman(3, [[0, 0, 0, 6, 0, 6, 0, 0, 6, 6], [6, 9, 0, 0, 6, 9, 6, 6, 0, 0], [0, 0, 0, 0, 9, 9, 0, 0, 0, 6], [6, 0, 6, 0, 9, 0, 6, 6, 0, 6]])

@runner.test(return_val=((2, 0), (1, 1)))
def test_int_char_2():
    return snowman.snowman(2, [[0, 6, 9], [0, 6, 9], [0, 6, 9]])

@runner.test(return_val=(None, (1, 1)))
def test_int_char_3():
    return snowman.snowman(2, [[9, 9, 9], [9, 6, 9], [9, 9, 9]])

runner.linebreak()

@runner.test(return_val=((0, 6), (2, 9)))
def test_str_char_1():
    return snowman.snowman(3, [["0", "0", "0", "6", "0", "6", "0", "0", "6", "6"], ["6", "9", "0", "0", "6", "9", "6", "6", "0", "0"], ["0", "0", "0", "0", "9", "9", "0", "0", "0", "6"], ["6", "0", "6", "0", "9", "0", "6", "6", "0", "6"]])

@runner.test(return_val=((2, 0), (1, 1)))
def test_str_char_2():
    return snowman.snowman(2, [["0", "6", "9"], ["0", "6", "9"], ["0", "6", "9"]])

@runner.test(return_val=(None, (1, 1)))
def test_str_char_3():
    return snowman.snowman(2, [["9", "9", "9"], ["9", "6", "9"], ["9", "9", "9"]])

runner.linebreak()

@runner.test(return_val=((0, 6), (2, 9)))
def test_string_1():
    return snowman.snowman(3, [["0006060066"], ["6900696600"], ["0000990006"], ["6060906606"]])

@runner.test(return_val=((2, 0), (1, 1)))
def test_string_2():
    return snowman.snowman(2, [["069"], ["069"], ["069"]])

@runner.test(return_val=(None, (1, 1)))
def test_string_3():
    return snowman.snowman(2, [["999"], ["969"], ["999"]])

runner.linebreak()

@runner.test(return_val=((1, 50), (18, 34))) # i'm sorry in advance
def test_large_1():
    return snowman.snowman(3, [[6, 9, 6, 6, 9, 9, 6, 9, 0, 6, 6, 0, 6, 0, 0, 0, 6, 6, 0, 0, 0, 0, 6, 6, 9, 0, 9, 6, 0, 9, 9, 6, 6, 0, 9, 9, 9, 0, 6, 0, 6, 0, 9, 0, 9, 0, 9, 9, 9, 0, 6, 6, 6, 0, 6, 9, 9, 6, 0, 6, 6, 6, 0, 0, 6, 0, 6, 6, 9, 9, 6, 6, 9, 6, 6, 9, 6, 0, 0, 0, 9, 6, 0, 9, 6, 0, 0, 0, 9, 0, 0, 9, 6, 6, 6, 9, 9, 9, 0, 0], [9, 6, 0, 0, 9, 6, 6, 0, 0, 6, 9, 9, 0, 0, 9, 0, 9, 0, 6, 9, 0, 6, 9, 9, 9, 9, 0, 9, 0, 0, 9, 9, 9, 9, 0, 6, 6, 6, 6, 0, 9, 6, 6, 6, 0, 9, 0, 9, 6, 6, 0, 0, 0, 6, 6, 0, 6, 0, 6, 0, 0, 9, 9, 9, 0, 9, 0, 9, 6, 0, 0, 9, 0, 9, 0, 0, 6, 6, 9, 9, 9, 9, 0, 9, 6, 0, 9, 0, 6, 6, 0, 0, 9, 6, 6, 9, 0, 0, 6, 9], [6, 9, 0, 9, 6, 0, 6, 0, 9, 9, 6, 0, 9, 0, 9, 9, 6, 9, 9, 6, 0, 9, 9, 6, 6, 9, 6, 6, 0, 6, 6, 9, 9, 0, 6, 0, 0, 0, 6, 9, 9, 6, 6, 6, 9, 0, 0, 9, 9, 0, 6, 9, 6, 6, 9, 0, 6, 9, 9, 9, 9, 6, 6, 9, 9, 9, 0, 6, 0, 0, 9, 0, 6, 0, 9, 0, 9, 6, 0, 9, 0, 6, 6, 9, 9, 0, 0, 0, 6, 9, 6, 0, 0, 6, 6, 9, 9, 0, 0, 0], [9, 6, 0, 0, 6, 0, 6, 6, 9, 6, 6, 6, 9, 9, 9, 0, 6, 6, 0, 6, 9, 9, 6, 0, 9, 9, 0, 9, 6, 6, 0, 6, 9, 6, 0, 6, 6, 0, 6, 9, 0, 0, 6, 0, 0, 9, 0, 9, 0, 9, 6, 0, 6, 9, 9, 0, 0, 0, 6, 0, 9, 9, 9, 6, 9, 9, 9, 0, 0, 9, 9, 6, 9, 0, 0, 9, 9, 0, 6, 6, 6, 0, 0, 6, 6, 0, 0, 0, 6, 6, 9, 6, 9, 6, 9, 9, 6, 0, 0, 9], [9, 9, 9, 9, 6, 6, 6, 6, 6, 0, 0, 0, 6, 6, 0, 0, 0, 0, 0, 0, 6, 0, 6, 0, 9, 6, 0, 6, 0, 9, 6, 9, 6, 9, 0, 9, 6, 6, 9, 6, 0, 6, 0, 0, 9, 9, 6, 0, 6, 0, 6, 6, 6, 0, 9, 9, 0, 6, 9, 9, 0, 0, 0, 6, 9, 6, 0, 9, 0, 9, 0, 6, 6, 6, 0, 6, 6, 6, 0, 6, 9, 0, 0, 9, 9, 0, 6, 9, 0, 9, 0, 0, 6, 9, 9, 9, 9, 6, 9, 9], [9, 6, 9, 0, 6, 6, 9, 9, 6, 6, 0, 0, 0, 0, 0, 9, 0, 0, 0, 6, 0, 9, 0, 9, 9, 9, 0, 6, 9, 9, 0, 9, 9, 9, 0, 0, 0, 0, 6, 0, 6, 9, 9, 9, 0, 0, 6, 9, 9, 0, 0, 9, 0, 9, 9, 0, 9, 9, 6, 6, 0, 9, 0, 0, 6, 0, 0, 9, 0, 0, 9, 6, 6, 9, 6, 0, 9, 9, 0, 9, 6, 6, 0, 6, 9, 9, 9, 0, 6, 6, 6, 6, 0, 0, 6, 6, 6, 0, 6, 0], [6, 0, 6, 9, 0, 6, 9, 9, 0, 9, 6, 0, 9, 0, 6, 6, 6, 9, 9, 0, 9, 9, 9, 6, 9, 0, 0, 0, 6, 9, 0, 6, 6, 9, 0, 9, 0, 9, 0, 6, 9, 9, 6, 6, 0, 0, 9, 0, 9, 6, 6, 9, 9, 6, 9, 0, 0, 0, 9, 0, 0, 0, 6, 6, 0, 9, 0, 0, 6, 0, 6, 0, 6, 9, 6, 0, 9, 6, 6, 6, 9, 6, 6, 9, 6, 0, 0, 0, 0, 6, 6, 9, 6, 6, 0, 6, 6, 0, 9, 6], [9, 9, 0, 9, 9, 9, 0, 9, 0, 9, 6, 6, 0, 6, 0, 6, 9, 9, 0, 9, 0, 6, 0, 6, 9, 9, 6, 0, 0, 9, 9, 9, 6, 9, 0, 6, 9, 0, 9, 9, 0, 0, 6, 6, 9, 0, 6, 0, 6, 0, 9, 9, 6, 9, 6, 0, 9, 9, 0, 0, 6, 0, 6, 6, 9, 6, 6, 0, 0, 9, 6, 9, 9, 9, 9, 6, 9, 0, 9, 0, 0, 6, 0, 0, 0, 9, 9, 9, 9, 9, 9, 6, 9, 6, 6, 0, 9, 0, 0, 6], [6, 9, 0, 0, 9, 0, 6, 9, 0, 9, 6, 0, 0, 6, 0, 9, 6, 6, 6, 9, 6, 6, 0, 9, 0, 6, 6, 6, 9, 0, 6, 0, 0, 6, 9, 0, 9, 0, 0, 6, 6, 9, 9, 0, 6, 6, 0, 9, 6, 0, 9, 6, 9, 0, 6, 9, 0, 0, 0, 9, 0, 6, 0, 6, 6, 6, 0, 6, 9, 9, 0, 9, 6, 6, 0, 9, 6, 6, 6, 6, 6, 6, 6, 0, 0, 6, 9, 9, 6, 9, 6, 9, 0, 9, 9, 6, 6, 6, 6, 0], [0, 6, 9, 9, 9, 6, 9, 0, 6, 0, 9, 6, 0, 0, 0, 9, 6, 6, 6, 0, 9, 0, 9, 0, 6, 6, 6, 9, 9, 6, 6, 6, 0, 6, 0, 9, 9, 9, 9, 0, 9, 6, 6, 6, 9, 9, 0, 0, 0, 9, 6, 6, 6, 9, 0, 0, 0, 6, 0, 0, 9, 6, 0, 6, 9, 6, 9, 0, 6, 9, 9, 9, 6, 6, 6, 0, 6, 6, 0, 6, 9, 9, 6, 9, 9, 0, 0, 9, 9, 6, 6, 6, 9, 6, 0, 0, 6, 6, 6, 9], [0, 0, 6, 0, 9, 0, 6, 9, 0, 0, 9, 6, 6, 0, 0, 0, 9, 0, 0, 0, 6, 9, 6, 9, 0, 9, 6, 9, 0, 6, 0, 9, 6, 9, 9, 0, 9, 6, 0, 0, 9, 0, 6, 6, 6, 6, 0, 9, 9, 0, 0, 6, 9, 6, 0, 9, 0, 6, 9, 6, 9, 0, 0, 0, 6, 0, 6, 6, 6, 9, 0, 6, 0, 6, 9, 6, 9, 6, 6, 0, 6, 0, 9, 9, 6, 6, 6, 6, 0, 6, 0, 0, 0, 9, 0, 9, 9, 9, 6, 9], [0, 9, 6, 0, 6, 0, 9, 9, 9, 6, 0, 6, 6, 0, 9, 6, 9, 9, 0, 9, 9, 6, 0, 9, 9, 9, 0, 0, 9, 6, 9, 9, 0, 9, 0, 0, 9, 9, 0, 6, 9, 9, 0, 0, 9, 6, 6, 6, 6, 9, 0, 0, 0, 6, 6, 9, 6, 6, 0, 0, 0, 6, 9, 6, 6, 6, 9, 0, 0, 0, 6, 6, 6, 0, 6, 6, 0, 9, 6, 6, 0, 6, 6, 6, 0, 0, 0, 9, 6, 0, 0, 6, 9, 6, 0, 9, 6, 6, 9, 9], [6, 6, 0, 6, 0, 9, 0, 0, 9, 0, 9, 6, 6, 0, 0, 0, 6, 6, 6, 9, 0, 6, 6, 9, 9, 6, 0, 0, 6, 9, 6, 0, 0, 6, 9, 9, 0, 0, 0, 0, 6, 9, 9, 9, 6, 6, 9, 6, 0, 0, 9, 0, 9, 6, 6, 0, 0, 9, 6, 6, 6, 0, 0, 6, 6, 6, 6, 9, 9, 6, 9, 6, 0, 9, 0, 9, 9, 9, 0, 0, 0, 0, 0, 0, 6, 9, 9, 9, 6, 6, 0, 6, 6, 0, 0, 0, 0, 0, 6, 9], [0, 6, 0, 6, 0, 0, 6, 6, 0, 0, 0, 9, 9, 9, 6, 6, 0, 0, 0, 0, 9, 6, 6, 9, 9, 9, 9, 0, 6, 9, 9, 9, 9, 0, 9, 6, 9, 0, 6, 9, 6, 6, 0, 6, 9, 9, 9, 0, 6, 6, 9, 9, 0, 9, 9, 9, 0, 9, 0, 9, 9, 0, 6, 9, 6, 9, 9, 0, 0, 0, 0, 6, 6, 6, 9, 0, 9, 0, 6, 0, 0, 9, 0, 9, 6, 6, 9, 9, 0, 0, 0, 9, 6, 0, 6, 9, 6, 9, 9, 6], [6, 0, 9, 9, 9, 0, 6, 0, 6, 6, 6, 0, 9, 6, 0, 9, 6, 9, 6, 6, 0, 6, 6, 0, 6, 9, 9, 9, 9, 0, 0, 9, 0, 9, 9, 0, 6, 0, 6, 0, 0, 6, 6, 0, 6, 0, 9, 6, 6, 9, 9, 9, 9, 9, 0, 0, 0, 9, 0, 0, 9, 0, 0, 6, 6, 0, 9, 9, 6, 0, 0, 6, 0, 6, 9, 9, 0, 9, 6, 9, 9, 9, 0, 9, 0, 9, 9, 0, 6, 9, 0, 0, 0, 6, 9, 0, 6, 9, 6, 9], [0, 9, 9, 6, 6, 6, 9, 0, 0, 9, 0, 6, 9, 6, 9, 0, 9, 9, 9, 9, 9, 6, 9, 0, 0, 9, 0, 6, 6, 9, 6, 9, 6, 0, 9, 9, 9, 0, 6, 6, 0, 6, 0, 6, 0, 6, 6, 9, 9, 0, 9, 9, 6, 9, 0, 9, 6, 6, 6, 0, 6, 6, 6, 9, 9, 9, 6, 9, 6, 0, 6, 9, 9, 0, 9, 0, 0, 6, 0, 0, 0, 0, 9, 0, 9, 9, 0, 6, 0, 6, 6, 0, 0, 9, 9, 9, 9, 6, 0, 0], [9, 0, 6, 6, 9, 9, 0, 9, 0, 0, 9, 9, 0, 9, 6, 9, 6, 0, 9, 9, 6, 0, 0, 6, 9, 0, 9, 0, 0, 0, 0, 9, 0, 6, 0, 0, 0, 9, 0, 0, 0, 9, 6, 0, 0, 0, 9, 9, 6, 9, 9, 9, 0, 6, 0, 0, 9, 6, 9, 6, 9, 0, 0, 9, 0, 0, 0, 0, 0, 0, 9, 9, 6, 0, 9, 9, 9, 0, 9, 6, 0, 0, 0, 0, 0, 0, 6, 9, 6, 0, 0, 9, 0, 9, 0, 9, 0, 9, 9, 6], [9, 9, 6, 0, 0, 9, 6, 0, 6, 6, 9, 0, 0, 6, 9, 9, 9, 9, 9, 6, 0, 9, 9, 9, 0, 9, 9, 6, 0, 6, 9, 0, 9, 9, 6, 0, 6, 0, 6, 0, 6, 0, 9, 0, 0, 6, 9, 9, 0, 9, 0, 9, 0, 9, 0, 0, 9, 9, 9, 9, 0, 6, 0, 9, 6, 9, 0, 9, 9, 0, 9, 9, 0, 0, 6, 6, 0, 9, 9, 6, 0, 6, 6, 6, 9, 9, 6, 9, 6, 9, 0, 6, 9, 0, 0, 6, 0, 6, 9, 6], [6, 0, 9, 0, 6, 0, 9, 9, 9, 6, 9, 6, 0, 0, 0, 6, 0, 9, 6, 9, 9, 6, 0, 0, 6, 9, 6, 0, 9, 6, 9, 9, 0, 0, 6, 6, 6, 0, 0, 0, 6, 0, 9, 9, 6, 9, 6, 0, 9, 0, 6, 6, 9, 0, 0, 0, 0, 6, 6, 0, 9, 9, 6, 6, 9, 9, 0, 6, 9, 9, 0, 6, 6, 0, 0, 6, 9, 9, 6, 0, 6, 6, 0, 9, 9, 6, 6, 9, 9, 0, 0, 0, 9, 0, 0, 0, 9, 6, 9, 9], [0, 0, 9, 9, 0, 9, 0, 9, 0, 6, 0, 9, 9, 9, 0, 6, 9, 9, 6, 6, 0, 6, 0, 6, 6, 9, 0, 0, 9, 6, 6, 6, 9, 0, 0, 0, 9, 0, 6, 6, 6, 6, 0, 9, 0, 9, 6, 6, 9, 6, 6, 6, 6, 6, 0, 6, 6, 9, 9, 6, 9, 6, 0, 6, 0, 9, 0, 0, 9, 9, 6, 9, 6, 0, 6, 6, 9, 6, 0, 6, 6, 6, 6, 0, 9, 6, 0, 6, 6, 6, 6, 0, 0, 0, 6, 0, 0, 6, 0, 0], [0, 6, 6, 9, 9, 0, 6, 0, 6, 9, 0, 9, 0, 0, 9, 0, 6, 0, 0, 9, 9, 9, 6, 6, 9, 6, 9, 9, 0, 6, 6, 9, 6, 9, 0, 0, 0, 6, 9, 0, 9, 9, 9, 0, 6, 9, 0, 0, 0, 6, 9, 0, 0, 6, 6, 9, 0, 9, 0, 6, 6, 0, 0, 6, 9, 0, 0, 0, 0, 0, 6, 9, 0, 6, 0, 0, 6, 9, 0, 0, 6, 9, 0, 6, 0, 9, 9, 6, 9, 9, 9, 0, 0, 0, 0, 9, 9, 0, 6, 6], [9, 0, 9, 0, 0, 0, 6, 0, 6, 0, 0, 0, 6, 0, 9, 6, 9, 0, 0, 9, 0, 9, 6, 6, 0, 9, 0, 0, 9, 0, 6, 6, 9, 0, 6, 6, 9, 6, 6, 0, 9, 0, 6, 6, 0, 6, 0, 0, 6, 6, 9, 9, 0, 6, 0, 9, 0, 9, 9, 9, 6, 6, 9, 6, 6, 9, 6, 0, 6, 0, 6, 0, 0, 6, 6, 9, 6, 0, 6, 0, 0, 9, 9, 6, 0, 6, 6, 0, 0, 9, 0, 9, 9, 0, 6, 6, 0, 6, 9, 6], [0, 6, 9, 9, 9, 6, 6, 6, 6, 9, 9, 6, 9, 0, 9, 0, 9, 6, 9, 6, 9, 6, 9, 9, 6, 9, 9, 6, 0, 6, 6, 0, 9, 0, 6, 0, 0, 0, 9, 9, 6, 6, 6, 9, 0, 9, 0, 6, 6, 6, 0, 6, 6, 6, 0, 0, 0, 0, 0, 9, 9, 9, 6, 9, 0, 9, 9, 6, 9, 0, 6, 9, 0, 0, 6, 6, 6, 6, 6, 9, 0, 9, 0, 0, 9, 9, 6, 0, 0, 9, 6, 9, 6, 9, 0, 0, 9, 6, 0, 6], [0, 0, 9, 6, 9, 6, 6, 6, 9, 9, 6, 9, 6, 9, 0, 6, 9, 0, 9, 9, 0, 9, 0, 0, 0, 0, 6, 9, 0, 0, 0, 9, 9, 6, 0, 0, 0, 6, 6, 0, 0, 6, 6, 9, 9, 6, 0, 0, 6, 9, 6, 0, 0, 6, 6, 0, 6, 6, 9, 6, 6, 9, 9, 0, 9, 9, 0, 6, 6, 9, 9, 0, 9, 6, 9, 6, 0, 0, 9, 0, 0, 0, 6, 6, 6, 6, 9, 9, 6, 0, 0, 0, 0, 6, 9, 9, 0, 9, 9, 9], [9, 6, 0, 6, 6, 9, 6, 9, 6, 9, 0, 0, 9, 9, 6, 9, 6, 6, 0, 0, 6, 6, 6, 6, 0, 9, 9, 0, 9, 0, 6, 9, 9, 9, 0, 0, 6, 6, 6, 9, 6, 0, 6, 0, 9, 0, 9, 0, 6, 6, 9, 0, 9, 9, 0, 6, 9, 9, 0, 9, 9, 6, 6, 6, 0, 6, 9, 0, 9, 9, 6, 0, 6, 6, 6, 0, 9, 0, 0, 9, 0, 6, 0, 9, 9, 9, 6, 9, 9, 6, 6, 6, 6, 0, 6, 0, 9, 0, 9, 6], [9, 0, 0, 6, 0, 6, 6, 0, 6, 0, 6, 6, 0, 6, 0, 0, 0, 9, 9, 9, 9, 9, 0, 0, 0, 6, 9, 9, 0, 0, 9, 0, 0, 0, 0, 0, 0, 9, 6, 0, 6, 0, 9, 9, 0, 6, 9, 9, 6, 9, 0, 6, 9, 6, 9, 9, 9, 6, 6, 9, 0, 6, 0, 0, 0, 9, 0, 0, 9, 6, 6, 6, 9, 6, 6, 0, 6, 9, 9, 6, 9, 0, 9, 0, 6, 6, 6, 9, 6, 6, 6, 9, 9, 6, 9, 6, 6, 0, 6, 0], [6, 6, 6, 0, 9, 0, 9, 6, 6, 9, 0, 6, 6, 6, 6, 6, 6, 9, 0, 9, 0, 0, 0, 6, 6, 0, 9, 0, 0, 9, 0, 6, 0, 9, 9, 0, 9, 6, 9, 9, 0, 9, 6, 6, 9, 6, 9, 9, 0, 0, 0, 9, 0, 0, 6, 9, 6, 0, 9, 9, 9, 0, 9, 9, 0, 6, 9, 6, 9, 9, 0, 0, 9, 9, 9, 6, 6, 0, 0, 6, 6, 9, 6, 9, 9, 6, 6, 9, 0, 0, 6, 6, 6, 9, 6, 9, 0, 9, 0, 6], [9, 6, 6, 9, 0, 0, 9, 9, 6, 0, 6, 9, 0, 9, 6, 6, 6, 6, 6, 6, 6, 6, 9, 0, 6, 9, 9, 0, 9, 9, 0, 0, 9, 0, 6, 9, 0, 9, 9, 9, 9, 0, 9, 6, 9, 9, 6, 0, 0, 0, 0, 6, 9, 6, 9, 0, 6, 6, 6, 6, 0, 6, 6, 9, 9, 0, 6, 6, 9, 9, 9, 0, 0, 0, 9, 0, 9, 6, 9, 9, 6, 9, 9, 9, 6, 9, 9, 0, 6, 9, 6, 6, 0, 0, 6, 9, 6, 6, 6, 6], [0, 6, 0, 6, 6, 9, 6, 6, 9, 6, 0, 6, 0, 6, 6, 0, 6, 9, 0, 6, 6, 9, 0, 9, 0, 0, 9, 6, 0, 9, 6, 6, 9, 9, 0, 6, 9, 9, 9, 9, 6, 0, 6, 6, 0, 6, 0, 0, 6, 6, 6, 0, 0, 9, 6, 9, 0, 6, 0, 6, 9, 6, 6, 6, 0, 9, 0, 9, 9, 6, 0, 6, 0, 6, 6, 6, 0, 9, 9, 0, 9, 9, 6, 9, 0, 0, 6, 6, 0, 6, 9, 0, 9, 9, 6, 0, 0, 9, 6, 9], [0, 0, 0, 6, 0, 6, 6, 9, 0, 6, 6, 0, 6, 0, 6, 9, 6, 0, 9, 6, 6, 9, 9, 0, 6, 6, 6, 0, 0, 9, 9, 9, 9, 0, 9, 9, 6, 0, 9, 0, 9, 0, 6, 0, 9, 6, 0, 9, 9, 9, 0, 6, 9, 9, 6, 0, 9, 9, 0, 0, 0, 9, 0, 6, 0, 0, 0, 6, 6, 0, 0, 9, 0, 6, 9, 0, 9, 6, 0, 9, 9, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 9, 6, 0, 9, 9, 9, 0, 9, 0], [6, 0, 9, 9, 9, 9, 0, 6, 9, 9, 0, 6, 6, 6, 0, 0, 9, 9, 9, 9, 0, 6, 9, 6, 9, 0, 9, 6, 9, 0, 9, 0, 6, 6, 0, 9, 6, 6, 6, 0, 0, 9, 9, 0, 6, 9, 9, 9, 6, 0, 6, 0, 0, 0, 9, 0, 9, 9, 6, 6, 0, 9, 6, 9, 6, 9, 9, 0, 9, 9, 6, 9, 9, 6, 9, 9, 6, 9, 0, 6, 0, 0, 9, 0, 9, 6, 0, 6, 9, 6, 0, 0, 0, 9, 0, 6, 0, 0, 6, 6], [0, 6, 6, 0, 0, 0, 6, 0, 9, 6, 0, 6, 6, 9, 6, 6, 0, 6, 9, 6, 6, 9, 6, 6, 9, 0, 6, 0, 9, 9, 9, 9, 6, 9, 9, 6, 0, 0, 9, 9, 9, 0, 9, 6, 0, 6, 6, 6, 6, 6, 6, 9, 6, 9, 6, 6, 9, 0, 0, 6, 9, 6, 6, 9, 9, 0, 0, 9, 9, 9, 9, 0, 9, 9, 0, 6, 9, 6, 9, 6, 6, 0, 6, 6, 9, 6, 6, 6, 9, 0, 0, 6, 9, 6, 0, 6, 9, 0, 6, 6], [0, 6, 9, 0, 6, 9, 0, 0, 6, 6, 6, 6, 6, 6, 9, 0, 9, 6, 0, 0, 6, 6, 9, 9, 9, 6, 9, 6, 0, 0, 9, 9, 9, 0, 6, 6, 6, 0, 6, 6, 6, 9, 0, 6, 6, 6, 9, 6, 6, 0, 6, 6, 6, 9, 9, 0, 0, 9, 9, 0, 0, 0, 0, 9, 6, 6, 0, 0, 9, 6, 0, 0, 9, 6, 9, 0, 6, 6, 6, 6, 6, 6, 6, 6, 6, 0, 6, 0, 6, 6, 6, 9, 6, 9, 6, 0, 9, 6, 0, 6], [0, 0, 9, 9, 0, 9, 0, 6, 9, 9, 6, 0, 9, 0, 0, 9, 9, 6, 0, 9, 9, 9, 0, 0, 6, 6, 9, 9, 0, 6, 9, 6, 9, 6, 6, 9, 0, 6, 0, 9, 9, 6, 9, 0, 0, 0, 6, 9, 0, 6, 0, 0, 9, 0, 6, 0, 9, 0, 0, 9, 0, 0, 9, 6, 6, 0, 9, 9, 9, 6, 9, 6, 6, 0, 9, 0, 9, 9, 0, 6, 9, 6, 0, 0, 9, 9, 0, 9, 6, 6, 6, 9, 6, 9, 6, 6, 6, 6, 6, 6], [6, 6, 0, 6, 0, 6, 0, 9, 6, 0, 9, 6, 0, 0, 9, 6, 9, 6, 6, 9, 6, 6, 6, 0, 9, 9, 0, 6, 0, 6, 0, 9, 6, 9, 9, 0, 6, 6, 9, 0, 0, 0, 6, 9, 6, 6, 6, 0, 9, 6, 0, 6, 6, 6, 9, 9, 9, 6, 6, 0, 0, 9, 6, 6, 6, 6, 0, 6, 9, 9, 9, 9, 6, 0, 0, 6, 6, 9, 0, 9, 0, 9, 9, 9, 9, 9, 6, 6, 0, 0, 6, 9, 0, 0, 0, 9, 9, 9, 9, 9], [6, 6, 6, 0, 9, 6, 9, 6, 9, 9, 9, 9, 0, 9, 6, 6, 0, 9, 0, 0, 6, 0, 6, 0, 0, 6, 9, 9, 0, 9, 0, 0, 6, 0, 0, 9, 9, 0, 9, 6, 9, 0, 0, 0, 0, 9, 6, 9, 9, 9, 9, 9, 6, 9, 0, 0, 0, 6, 9, 0, 9, 6, 0, 0, 6, 0, 0, 0, 0, 9, 9, 6, 9, 0, 9, 9, 0, 0, 0, 9, 9, 0, 6, 6, 9, 6, 9, 0, 9, 9, 9, 9, 9, 9, 0, 6, 9, 0, 0, 0], [6, 6, 9, 6, 6, 0, 0, 9, 0, 0, 0, 0, 9, 9, 0, 0, 0, 6, 0, 9, 6, 9, 9, 0, 6, 6, 0, 0, 6, 0, 6, 6, 6, 0, 0, 0, 6, 9, 0, 9, 6, 9, 6, 9, 6, 9, 6, 0, 0, 6, 0, 6, 9, 6, 0, 6, 0, 0, 0, 6, 6, 0, 9, 0, 0, 9, 9, 6, 6, 6, 9, 6, 0, 0, 9, 9, 9, 9, 9, 9, 9, 0, 6, 9, 0, 6, 9, 9, 0, 9, 6, 6, 6, 9, 9, 0, 0, 0, 9, 6], [6, 0, 6, 0, 6, 9, 9, 9, 0, 6, 6, 9, 6, 6, 9, 6, 6, 6, 6, 0, 9, 0, 6, 0, 6, 6, 9, 6, 6, 6, 6, 0, 6, 9, 6, 6, 9, 6, 6, 6, 0, 0, 9, 6, 6, 6, 9, 6, 9, 9, 9, 9, 6, 6, 0, 9, 6, 6, 9, 6, 6, 0, 0, 9, 6, 0, 0, 9, 6, 9, 6, 6, 9, 9, 0, 9, 0, 6, 6, 9, 0, 9, 6, 6, 0, 9, 6, 6, 9, 0, 9, 9, 6, 0, 6, 9, 9, 6, 9, 6], [0, 6, 6, 9, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 6, 9, 0, 6, 6, 9, 6, 6, 0, 0, 6, 9, 9, 6, 0, 0, 9, 0, 6, 0, 9, 6, 9, 0, 9, 9, 9, 9, 9, 6, 0, 0, 9, 0, 0, 9, 9, 6, 9, 0, 0, 6, 6, 9, 9, 9, 0, 6, 9, 9, 0, 9, 9, 6, 0, 0, 6, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 9, 6, 9, 0, 6, 9, 0, 9, 6, 9, 6, 0, 9, 6, 6, 6, 0, 0, 6], [0, 6, 9, 9, 9, 9, 6, 0, 9, 9, 9, 6, 0, 0, 0, 6, 6, 9, 0, 0, 9, 6, 6, 6, 6, 0, 6, 6, 6, 9, 6, 9, 0, 9, 9, 0, 9, 6, 0, 6, 9, 6, 0, 6, 9, 0, 6, 6, 6, 0, 6, 9, 6, 9, 0, 9, 0, 0, 0, 9, 0, 0, 9, 0, 9, 9, 0, 9, 6, 9, 6, 9, 9, 6, 6, 0, 6, 9, 9, 9, 9, 9, 0, 6, 6, 0, 0, 6, 9, 9, 0, 6, 0, 6, 6, 0, 0, 0, 9, 0], [0, 9, 6, 6, 0, 9, 0, 6, 6, 6, 6, 9, 9, 9, 6, 9, 9, 6, 9, 0, 6, 6, 0, 0, 0, 6, 0, 0, 0, 6, 0, 9, 9, 6, 6, 9, 6, 9, 0, 9, 0, 0, 6, 0, 9, 6, 6, 0, 0, 6, 0, 9, 9, 9, 6, 9, 0, 0, 6, 0, 9, 0, 0, 9, 6, 0, 0, 9, 6, 0, 0, 0, 9, 9, 6, 0, 6, 0, 9, 6, 6, 9, 0, 0, 0, 6, 6, 9, 0, 6, 6, 0, 6, 9, 6, 0, 6, 9, 9, 0], [6, 0, 6, 0, 9, 6, 0, 9, 6, 6, 6, 9, 9, 0, 6, 9, 0, 0, 6, 6, 0, 9, 6, 6, 6, 6, 6, 0, 9, 9, 9, 9, 9, 0, 0, 9, 0, 6, 0, 0, 6, 9, 9, 9, 6, 9, 9, 0, 0, 9, 9, 0, 9, 0, 0, 0, 9, 9, 9, 6, 6, 6, 9, 6, 0, 9, 6, 6, 0, 6, 0, 9, 6, 0, 6, 9, 0, 0, 6, 0, 0, 6, 9, 0, 9, 9, 9, 6, 9, 0, 6, 9, 6, 0, 9, 0, 0, 9, 0, 6], [9, 0, 6, 0, 6, 0, 0, 9, 6, 9, 9, 9, 0, 9, 9, 6, 6, 9, 6, 0, 6, 9, 9, 6, 9, 0, 0, 9, 9, 0, 6, 6, 0, 6, 9, 0, 0, 9, 6, 9, 6, 9, 9, 9, 6, 9, 6, 6, 6, 9, 0, 9, 6, 0, 6, 0, 9, 9, 0, 6, 6, 9, 6, 0, 9, 6, 9, 6, 6, 9, 9, 0, 6, 9, 6, 6, 9, 6, 6, 9, 6, 0, 6, 6, 6, 0, 0, 0, 9, 9, 0, 9, 0, 6, 6, 6, 6, 9, 9, 6], [9, 0, 0, 9, 6, 0, 6, 0, 9, 0, 6, 6, 6, 0, 0, 0, 0, 9, 6, 6, 6, 0, 0, 9, 9, 9, 6, 0, 6, 6, 9, 6, 9, 6, 9, 0, 6, 9, 9, 6, 6, 0, 0, 6, 6, 0, 9, 9, 0, 0, 6, 0, 6, 0, 6, 9, 6, 0, 0, 9, 9, 9, 6, 6, 6, 0, 9, 0, 0, 9, 9, 9, 0, 9, 6, 0, 0, 6, 9, 0, 6, 6, 6, 9, 6, 0, 6, 0, 0, 6, 9, 0, 0, 0, 0, 9, 9, 0, 0, 6], [9, 0, 0, 9, 0, 6, 6, 9, 9, 0, 0, 0, 6, 6, 0, 6, 6, 6, 9, 0, 0, 0, 6, 0, 9, 0, 6, 0, 6, 6, 9, 6, 6, 6, 9, 6, 9, 0, 0, 9, 6, 0, 0, 9, 9, 6, 0, 0, 0, 9, 0, 6, 6, 9, 9, 9, 6, 0, 6, 0, 6, 9, 6, 9, 0, 9, 6, 0, 9, 6, 9, 6, 6, 0, 0, 0, 0, 9, 6, 0, 6, 0, 6, 0, 0, 9, 0, 0, 6, 6, 6, 6, 6, 0, 0, 6, 6, 6, 0, 0], [6, 6, 0, 0, 9, 9, 0, 0, 9, 6, 0, 9, 0, 6, 9, 6, 0, 0, 9, 9, 6, 9, 0, 9, 9, 9, 6, 0, 0, 0, 9, 6, 0, 6, 6, 0, 6, 6, 6, 6, 9, 6, 6, 0, 9, 0, 6, 0, 9, 9, 0, 9, 0, 6, 6, 9, 6, 9, 6, 0, 0, 0, 9, 9, 6, 0, 6, 0, 6, 0, 0, 9, 0, 9, 9, 9, 6, 0, 0, 0, 9, 6, 6, 6, 0, 0, 6, 0, 6, 0, 9, 6, 9, 0, 9, 6, 0, 0, 0, 0], [6, 9, 6, 0, 9, 6, 0, 9, 6, 9, 9, 6, 9, 6, 6, 9, 0, 0, 0, 0, 6, 0, 9, 6, 6, 9, 6, 6, 0, 0, 6, 9, 0, 6, 9, 0, 9, 0, 0, 0, 6, 6, 0, 6, 0, 0, 9, 9, 0, 0, 9, 0, 6, 9, 9, 9, 6, 0, 0, 6, 6, 9, 9, 9, 9, 6, 9, 6, 0, 6, 0, 0, 6, 9, 9, 6, 6, 9, 6, 6, 0, 9, 9, 0, 9, 9, 6, 6, 6, 0, 6, 9, 0, 9, 9, 0, 6, 0, 6, 9], [9, 6, 0, 0, 9, 0, 0, 9, 0, 0, 0, 9, 0, 6, 0, 9, 9, 9, 6, 9, 0, 0, 6, 6, 6, 9, 6, 6, 0, 0, 0, 6, 0, 9, 0, 6, 9, 6, 9, 0, 6, 6, 0, 0, 9, 6, 6, 0, 6, 6, 0, 0, 6, 0, 9, 0, 9, 6, 0, 9, 6, 0, 9, 9, 0, 9, 9, 6, 0, 6, 9, 9, 6, 9, 9, 0, 0, 0, 9, 0, 9, 9, 9, 0, 9, 6, 0, 0, 9, 6, 0, 9, 6, 0, 9, 6, 0, 9, 0, 0], [0, 9, 6, 9, 6, 9, 0, 6, 6, 9, 0, 0, 0, 0, 9, 0, 6, 9, 0, 0, 6, 9, 9, 0, 9, 9, 9, 6, 0, 9, 9, 6, 0, 6, 0, 9, 9, 9, 9, 9, 9, 6, 6, 6, 6, 9, 9, 9, 6, 6, 6, 9, 0, 6, 0, 0, 0, 9, 6, 0, 0, 0, 0, 6, 9, 6, 6, 6, 0, 9, 9, 0, 6, 9, 6, 9, 6, 0, 6, 0, 6, 9, 0, 0, 9, 0, 0, 6, 9, 0, 6, 0, 6, 9, 9, 0, 6, 6, 0, 6], [0, 0, 9, 6, 0, 0, 9, 6, 0, 0, 9, 0, 0, 0, 6, 6, 0, 9, 6, 0, 0, 9, 9, 6, 6, 6, 6, 0, 9, 0, 0, 0, 6, 0, 6, 0, 0, 6, 0, 9, 9, 9, 6, 6, 9, 0, 0, 0, 0, 9, 0, 6, 0, 6, 6, 6, 9, 0, 0, 0, 6, 6, 6, 6, 6, 0, 9, 6, 9, 6, 6, 6, 9, 0, 0, 0, 0, 9, 6, 0, 9, 0, 6, 0, 9, 9, 0, 9, 0, 0, 6, 0, 6, 9, 9, 0, 6, 9, 9, 0], [9, 9, 6, 6, 6, 6, 0, 9, 0, 0, 0, 9, 9, 9, 0, 9, 9, 0, 9, 9, 0, 0, 0, 9, 9, 9, 9, 6, 0, 6, 0, 6, 6, 0, 9, 0, 9, 0, 9, 6, 0, 0, 0, 6, 9, 9, 0, 0, 6, 9, 0, 9, 0, 0, 9, 0, 0, 0, 0, 6, 6, 0, 6, 9, 9, 6, 0, 6, 6, 6, 0, 9, 0, 9, 9, 9, 9, 9, 9, 6, 6, 9, 0, 6, 9, 0, 9, 6, 6, 9, 6, 6, 0, 6, 9, 0, 6, 9, 0, 9], [9, 9, 0, 6, 0, 6, 9, 0, 6, 9, 9, 6, 9, 6, 0, 6, 9, 6, 6, 9, 9, 6, 9, 0, 0, 9, 9, 0, 0, 9, 6, 6, 6, 9, 0, 0, 6, 6, 0, 6, 9, 6, 0, 0, 9, 0, 0, 6, 9, 0, 6, 6, 0, 0, 0, 6, 0, 6, 0, 9, 6, 9, 9, 6, 0, 0, 6, 6, 9, 9, 9, 0, 6, 0, 9, 9, 6, 0, 0, 0, 0, 6, 9, 9, 6, 0, 6, 0, 6, 6, 9, 0, 6, 6, 6, 0, 6, 6, 0, 0], [0, 9, 6, 6, 0, 9, 0, 9, 6, 6, 0, 0, 0, 0, 6, 6, 0, 9, 0, 9, 9, 6, 9, 0, 0, 9, 6, 0, 9, 0, 6, 9, 6, 6, 0, 0, 6, 6, 6, 9, 6, 0, 9, 0, 0, 6, 9, 6, 0, 6, 0, 0, 9, 6, 9, 9, 9, 9, 6, 0, 9, 0, 9, 0, 0, 6, 0, 0, 6, 9, 6, 6, 9, 0, 9, 6, 0, 6, 9, 0, 9, 0, 6, 6, 6, 9, 6, 0, 0, 0, 9, 0, 6, 6, 6, 6, 0, 9, 6, 0], [6, 9, 0, 6, 6, 9, 6, 9, 9, 6, 6, 6, 0, 9, 0, 6, 6, 9, 0, 0, 6, 9, 9, 6, 0, 0, 6, 0, 0, 6, 6, 9, 9, 9, 6, 6, 9, 6, 9, 6, 9, 0, 6, 9, 0, 6, 9, 0, 9, 6, 9, 9, 9, 9, 9, 9, 0, 9, 0, 6, 9, 0, 9, 0, 6, 6, 9, 9, 6, 0, 0, 0, 0, 9, 9, 0, 0, 6, 9, 0, 9, 0, 6, 6, 9, 9, 0, 0, 0, 0, 0, 9, 9, 0, 9, 9, 0, 0, 9, 6], [9, 0, 0, 6, 6, 0, 0, 9, 6, 0, 6, 9, 9, 9, 9, 0, 9, 9, 9, 6, 6, 6, 0, 9, 0, 9, 6, 6, 0, 9, 9, 0, 6, 0, 6, 0, 0, 0, 6, 0, 6, 9, 0, 0, 9, 0, 6, 9, 9, 9, 6, 0, 9, 9, 0, 6, 9, 6, 0, 6, 6, 9, 9, 9, 9, 0, 0, 6, 6, 6, 6, 9, 6, 6, 6, 6, 9, 0, 6, 9, 9, 9, 0, 9, 6, 9, 9, 6, 9, 0, 0, 0, 0, 9, 9, 9, 0, 6, 9, 0], [6, 0, 0, 0, 0, 0, 9, 6, 6, 0, 6, 0, 6, 0, 0, 9, 0, 9, 6, 9, 9, 0, 6, 9, 0, 6, 6, 9, 6, 9, 9, 6, 0, 9, 0, 9, 9, 6, 6, 0, 9, 9, 9, 9, 6, 9, 9, 9, 0, 6, 0, 6, 9, 9, 6, 0, 6, 0, 9, 0, 0, 6, 0, 6, 6, 6, 0, 0, 0, 6, 0, 6, 0, 6, 6, 9, 6, 6, 0, 6, 6, 9, 0, 6, 0, 0, 0, 0, 0, 9, 6, 6, 9, 9, 0, 6, 6, 6, 6, 9], [0, 6, 6, 9, 9, 0, 9, 6, 6, 6, 6, 0, 9, 9, 0, 6, 6, 6, 6, 6, 0, 9, 0, 6, 6, 0, 6, 9, 6, 6, 0, 9, 6, 0, 0, 0, 0, 6, 9, 6, 0, 0, 6, 6, 9, 0, 9, 0, 0, 9, 9, 6, 6, 6, 0, 0, 0, 6, 9, 9, 9, 9, 6, 9, 0, 6, 6, 0, 0, 0, 0, 9, 9, 6, 6, 6, 6, 9, 6, 0, 9, 9, 0, 0, 0, 6, 6, 9, 9, 6, 9, 6, 6, 0, 0, 6, 9, 6, 9, 6], [9, 9, 0, 9, 0, 9, 6, 6, 6, 0, 9, 0, 0, 0, 0, 9, 9, 0, 0, 9, 9, 9, 9, 9, 9, 6, 9, 6, 0, 6, 6, 0, 0, 9, 0, 0, 9, 6, 0, 6, 6, 9, 9, 6, 6, 0, 6, 9, 6, 9, 0, 6, 9, 6, 6, 0, 9, 9, 0, 0, 6, 6, 6, 9, 0, 9, 6, 6, 9, 9, 6, 0, 9, 0, 6, 9, 0, 9, 6, 0, 6, 0, 0, 0, 0, 9, 9, 6, 0, 6, 9, 0, 9, 6, 9, 9, 0, 9, 0, 9], [9, 9, 6, 6, 0, 9, 6, 0, 6, 0, 0, 0, 0, 6, 9, 0, 0, 0, 0, 9, 6, 6, 0, 0, 0, 6, 0, 6, 0, 0, 0, 9, 0, 6, 0, 6, 0, 6, 6, 0, 0, 9, 6, 6, 9, 0, 0, 9, 9, 9, 6, 9, 9, 9, 0, 9, 6, 9, 0, 6, 0, 9, 9, 6, 9, 0, 0, 9, 6, 6, 0, 9, 0, 6, 0, 6, 6, 0, 9, 0, 6, 9, 0, 0, 6, 9, 6, 6, 9, 9, 9, 6, 0, 0, 0, 6, 9, 6, 6, 6], [9, 0, 0, 6, 0, 6, 0, 6, 9, 6, 0, 6, 6, 6, 6, 0, 0, 6, 6, 9, 9, 0, 6, 6, 0, 9, 6, 6, 6, 0, 6, 0, 0, 0, 6, 0, 0, 6, 6, 0, 0, 6, 0, 0, 0, 0, 6, 0, 9, 9, 9, 0, 9, 0, 0, 0, 6, 0, 9, 0, 6, 0, 0, 9, 0, 9, 0, 6, 6, 0, 9, 0, 0, 9, 0, 0, 0, 6, 9, 0, 0, 9, 9, 9, 0, 9, 6, 6, 0, 9, 0, 6, 0, 6, 0, 6, 6, 6, 6, 9], [0, 9, 9, 9, 0, 9, 0, 9, 6, 9, 9, 6, 9, 6, 0, 0, 6, 0, 6, 0, 9, 6, 9, 6, 9, 0, 9, 6, 9, 9, 0, 6, 6, 0, 9, 9, 0, 0, 0, 6, 0, 0, 9, 6, 9, 9, 6, 0, 9, 0, 9, 0, 6, 9, 0, 0, 6, 9, 0, 6, 0, 6, 6, 6, 0, 6, 6, 0, 6, 0, 9, 9, 0, 0, 6, 9, 6, 0, 9, 6, 0, 6, 6, 6, 9, 0, 0, 9, 9, 0, 6, 0, 6, 9, 9, 0, 9, 6, 6, 0], [6, 6, 6, 6, 9, 9, 9, 9, 6, 6, 9, 0, 9, 0, 6, 6, 0, 0, 0, 0, 0, 6, 9, 6, 0, 6, 0, 6, 0, 0, 9, 6, 9, 0, 6, 0, 9, 6, 6, 6, 0, 9, 0, 0, 0, 0, 9, 9, 0, 0, 9, 6, 0, 6, 0, 0, 0, 6, 0, 6, 9, 6, 6, 6, 6, 0, 9, 6, 9, 0, 9, 9, 9, 0, 6, 0, 9, 0, 9, 9, 6, 9, 0, 6, 9, 0, 0, 6, 6, 0, 0, 6, 0, 9, 0, 9, 6, 6, 9, 6], [9, 0, 6, 9, 0, 0, 9, 0, 9, 6, 9, 0, 6, 9, 6, 0, 0, 9, 0, 6, 0, 6, 6, 9, 9, 0, 9, 9, 0, 6, 0, 9, 9, 0, 6, 6, 6, 6, 9, 0, 0, 6, 9, 0, 6, 0, 0, 0, 6, 9, 9, 6, 6, 6, 6, 6, 9, 0, 9, 0, 0, 0, 6, 6, 0, 9, 0, 6, 0, 6, 0, 6, 6, 6, 0, 0, 0, 0, 9, 0, 6, 6, 0, 9, 9, 6, 9, 9, 6, 6, 0, 9, 9, 9, 6, 0, 6, 9, 0, 6], [0, 0, 9, 6, 9, 0, 6, 0, 9, 0, 9, 6, 9, 0, 0, 0, 0, 9, 6, 6, 6, 9, 6, 6, 0, 9, 6, 0, 0, 6, 0, 0, 9, 6, 6, 0, 6, 9, 0, 6, 9, 9, 9, 9, 9, 0, 0, 0, 9, 0, 9, 0, 6, 0, 0, 0, 9, 0, 9, 6, 9, 6, 6, 6, 6, 0, 0, 9, 9, 9, 6, 9, 9, 6, 9, 9, 0, 0, 0, 0, 9, 6, 0, 9, 9, 6, 9, 0, 6, 0, 9, 9, 0, 6, 9, 0, 6, 6, 9, 9], [6, 0, 0, 9, 6, 6, 0, 6, 0, 0, 9, 0, 9, 6, 6, 0, 9, 9, 9, 0, 9, 9, 0, 6, 9, 0, 6, 0, 9, 6, 6, 9, 6, 6, 9, 0, 9, 0, 9, 9, 0, 9, 6, 9, 9, 0, 6, 6, 0, 6, 9, 9, 6, 0, 9, 0, 6, 0, 0, 9, 9, 6, 9, 0, 9, 9, 0, 6, 0, 0, 0, 0, 6, 6, 6, 6, 9, 6, 6, 0, 0, 0, 0, 6, 6, 0, 6, 0, 6, 6, 6, 6, 0, 6, 6, 9, 0, 0, 0, 6], [6, 0, 0, 6, 6, 9, 9, 9, 6, 0, 9, 9, 6, 9, 0, 6, 0, 0, 6, 0, 6, 0, 9, 0, 6, 6, 0, 6, 0, 0, 6, 0, 0, 9, 6, 9, 0, 0, 0, 6, 6, 0, 9, 6, 9, 6, 0, 6, 6, 9, 9, 0, 9, 9, 0, 0, 9, 0, 0, 0, 6, 0, 9, 6, 6, 6, 9, 6, 6, 0, 9, 0, 9, 0, 0, 6, 9, 6, 9, 6, 9, 6, 9, 9, 6, 6, 9, 0, 6, 9, 6, 0, 0, 6, 0, 6, 9, 0, 0, 6], [9, 9, 0, 9, 9, 6, 0, 6, 9, 9, 6, 0, 0, 6, 9, 6, 9, 9, 6, 6, 0, 0, 0, 6, 9, 0, 0, 0, 9, 9, 6, 9, 0, 6, 0, 6, 6, 0, 9, 6, 9, 9, 9, 9, 6, 9, 0, 9, 9, 6, 6, 9, 0, 0, 0, 9, 9, 9, 9, 6, 0, 9, 9, 0, 0, 6, 6, 0, 0, 6, 6, 6, 9, 9, 6, 6, 0, 9, 9, 6, 6, 0, 9, 9, 0, 0, 0, 9, 6, 9, 9, 9, 0, 0, 6, 9, 9, 9, 9, 0], [9, 6, 6, 6, 6, 6, 9, 0, 6, 0, 0, 9, 6, 9, 0, 6, 0, 6, 0, 0, 6, 6, 0, 0, 0, 0, 0, 9, 9, 6, 9, 6, 9, 9, 0, 6, 0, 9, 9, 9, 0, 6, 9, 9, 6, 6, 9, 0, 9, 9, 0, 0, 0, 0, 6, 0, 0, 9, 6, 6, 0, 6, 9, 6, 0, 6, 6, 0, 9, 9, 0, 0, 6, 9, 9, 6, 0, 0, 9, 6, 9, 0, 9, 0, 9, 6, 6, 9, 0, 0, 0, 9, 6, 6, 9, 0, 0, 0, 0, 9], [0, 6, 9, 0, 0, 9, 6, 0, 0, 9, 0, 6, 0, 0, 6, 0, 6, 9, 9, 0, 9, 9, 0, 0, 6, 9, 0, 6, 0, 0, 6, 0, 0, 6, 6, 6, 0, 0, 0, 9, 9, 6, 6, 6, 6, 0, 9, 9, 0, 6, 0, 0, 9, 6, 0, 6, 0, 9, 0, 9, 9, 0, 0, 9, 9, 0, 6, 9, 9, 0, 9, 0, 9, 6, 0, 9, 6, 9, 9, 0, 6, 9, 0, 0, 0, 0, 9, 0, 6, 9, 6, 6, 0, 0, 6, 6, 0, 0, 9, 0], [9, 0, 9, 6, 9, 0, 9, 0, 9, 6, 6, 9, 6, 6, 9, 6, 0, 0, 0, 6, 9, 9, 9, 9, 9, 0, 6, 6, 9, 9, 9, 6, 9, 0, 0, 0, 6, 6, 0, 0, 9, 0, 6, 9, 0, 9, 9, 0, 6, 0, 9, 9, 0, 6, 6, 9, 6, 6, 6, 9, 6, 0, 6, 0, 6, 6, 9, 6, 0, 9, 6, 6, 0, 6, 9, 0, 6, 0, 6, 6, 9, 0, 6, 6, 9, 0, 6, 0, 6, 9, 6, 0, 0, 0, 0, 9, 6, 9, 0, 0], [0, 0, 9, 6, 6, 6, 9, 6, 6, 6, 0, 0, 9, 6, 9, 9, 6, 6, 0, 6, 9, 0, 0, 9, 6, 6, 9, 0, 0, 9, 0, 0, 9, 9, 6, 0, 9, 6, 0, 6, 6, 9, 9, 0, 9, 0, 9, 6, 6, 0, 0, 6, 9, 0, 9, 9, 0, 9, 6, 6, 6, 0, 6, 6, 0, 0, 9, 0, 6, 9, 0, 0, 6, 9, 6, 0, 9, 6, 0, 0, 9, 0, 9, 0, 6, 6, 0, 0, 6, 6, 6, 0, 0, 9, 6, 0, 6, 0, 9, 9], [9, 6, 0, 6, 6, 0, 9, 6, 9, 0, 6, 9, 0, 0, 0, 0, 9, 0, 6, 9, 0, 9, 6, 6, 9, 9, 0, 6, 6, 0, 9, 0, 9, 9, 6, 6, 6, 6, 0, 9, 9, 6, 9, 6, 6, 9, 6, 0, 0, 9, 9, 9, 9, 9, 6, 0, 9, 6, 0, 9, 0, 0, 6, 9, 6, 0, 0, 6, 0, 9, 6, 0, 6, 6, 6, 0, 9, 9, 0, 9, 0, 9, 0, 6, 0, 0, 0, 9, 6, 0, 6, 6, 6, 0, 9, 9, 6, 0, 9, 6], [0, 9, 6, 9, 0, 6, 9, 0, 9, 0, 9, 9, 0, 0, 9, 0, 0, 9, 6, 9, 6, 6, 0, 9, 0, 0, 9, 6, 6, 9, 0, 9, 0, 9, 6, 9, 6, 9, 6, 0, 6, 0, 9, 6, 9, 6, 6, 0, 0, 6, 0, 6, 6, 9, 6, 9, 0, 9, 0, 9, 9, 0, 6, 6, 6, 0, 9, 0, 9, 6, 0, 0, 6, 0, 0, 6, 6, 9, 9, 6, 0, 9, 9, 6, 6, 0, 0, 6, 6, 0, 9, 0, 0, 9, 0, 9, 0, 0, 0, 9], [0, 9, 0, 0, 6, 0, 9, 9, 9, 9, 6, 6, 6, 0, 9, 0, 6, 6, 0, 6, 9, 0, 9, 6, 6, 9, 9, 9, 6, 6, 9, 9, 0, 6, 6, 0, 9, 9, 6, 9, 6, 9, 0, 0, 0, 9, 0, 6, 0, 0, 9, 9, 9, 6, 6, 6, 0, 6, 9, 0, 6, 6, 0, 6, 9, 6, 9, 9, 9, 0, 0, 6, 6, 9, 9, 0, 0, 0, 0, 0, 9, 9, 0, 6, 9, 0, 0, 9, 9, 0, 0, 6, 6, 6, 6, 6, 0, 6, 0, 6], [0, 9, 6, 0, 9, 9, 0, 0, 6, 6, 6, 6, 9, 0, 6, 6, 0, 0, 9, 0, 6, 9, 6, 9, 6, 9, 0, 9, 6, 6, 6, 9, 6, 0, 9, 0, 6, 0, 6, 6, 0, 0, 0, 9, 0, 6, 0, 0, 6, 9, 6, 6, 9, 6, 9, 6, 6, 6, 6, 9, 6, 6, 0, 9, 0, 0, 0, 9, 0, 9, 0, 6, 6, 0, 0, 9, 0, 6, 6, 0, 6, 9, 6, 0, 0, 9, 9, 9, 0, 6, 9, 9, 6, 0, 0, 0, 6, 0, 0, 9], [9, 9, 9, 6, 0, 6, 6, 6, 9, 9, 9, 9, 6, 9, 0, 6, 6, 0, 9, 6, 6, 9, 0, 0, 9, 6, 6, 0, 6, 9, 0, 0, 6, 9, 9, 9, 6, 0, 6, 0, 0, 6, 0, 9, 0, 6, 0, 9, 9, 9, 6, 6, 6, 9, 0, 6, 9, 9, 9, 9, 6, 0, 6, 9, 9, 0, 0, 6, 6, 6, 9, 9, 6, 9, 0, 6, 9, 0, 0, 0, 0, 6, 6, 0, 0, 6, 0, 9, 6, 6, 9, 6, 6, 6, 0, 6, 0, 9, 6, 6], [9, 6, 0, 0, 0, 6, 6, 0, 0, 6, 6, 0, 0, 0, 9, 6, 6, 9, 0, 6, 9, 6, 6, 6, 9, 6, 6, 6, 9, 6, 0, 6, 9, 9, 9, 9, 6, 6, 0, 9, 6, 9, 9, 0, 9, 0, 0, 0, 0, 0, 6, 9, 6, 9, 6, 0, 9, 6, 0, 0, 9, 9, 9, 6, 0, 0, 0, 0, 6, 0, 9, 9, 0, 6, 9, 0, 9, 6, 9, 6, 6, 0, 6, 0, 6, 9, 0, 6, 0, 6, 0, 9, 9, 6, 6, 0, 0, 6, 6, 9], [6, 6, 0, 9, 9, 9, 9, 0, 6, 0, 0, 0, 0, 0, 0, 0, 6, 0, 9, 0, 0, 6, 9, 6, 6, 6, 6, 0, 6, 9, 6, 0, 9, 9, 0, 9, 0, 0, 9, 6, 9, 6, 9, 9, 0, 6, 6, 9, 9, 9, 9, 0, 6, 9, 6, 6, 0, 9, 6, 0, 9, 9, 6, 0, 6, 6, 9, 9, 6, 9, 6, 0, 9, 0, 9, 6, 6, 0, 6, 9, 6, 6, 9, 9, 9, 9, 9, 6, 6, 0, 0, 9, 0, 0, 9, 6, 6, 0, 0, 0], [9, 0, 9, 6, 9, 6, 0, 6, 6, 0, 6, 6, 6, 9, 6, 0, 0, 0, 9, 6, 9, 9, 9, 6, 9, 6, 6, 0, 6, 9, 9, 6, 0, 0, 0, 6, 0, 9, 0, 0, 9, 6, 0, 0, 9, 9, 6, 6, 6, 6, 9, 0, 0, 6, 0, 6, 9, 0, 9, 9, 6, 9, 0, 6, 9, 9, 9, 6, 9, 6, 9, 0, 6, 6, 9, 6, 6, 0, 6, 0, 6, 9, 0, 9, 0, 0, 6, 6, 6, 9, 9, 9, 6, 6, 0, 6, 9, 9, 0, 6], [6, 0, 6, 0, 6, 6, 9, 0, 0, 0, 0, 9, 0, 0, 9, 6, 9, 6, 6, 6, 6, 0, 0, 9, 6, 6, 9, 6, 0, 6, 0, 6, 6, 6, 6, 6, 9, 0, 9, 6, 6, 0, 9, 0, 9, 9, 6, 0, 0, 0, 0, 9, 6, 6, 0, 6, 9, 6, 9, 0, 9, 6, 9, 9, 9, 6, 9, 6, 0, 9, 0, 9, 9, 9, 0, 9, 9, 0, 6, 6, 0, 6, 9, 9, 9, 0, 9, 6, 6, 9, 0, 0, 0, 0, 9, 9, 0, 9, 0, 9], [6, 9, 6, 9, 6, 6, 9, 0, 9, 6, 0, 9, 9, 9, 9, 6, 0, 0, 9, 6, 6, 0, 6, 9, 0, 0, 0, 0, 0, 0, 6, 0, 9, 9, 6, 0, 6, 6, 6, 9, 6, 6, 6, 6, 6, 0, 0, 0, 9, 9, 6, 0, 0, 9, 9, 6, 9, 9, 9, 9, 0, 9, 6, 6, 9, 0, 9, 9, 6, 9, 6, 0, 9, 6, 9, 9, 9, 9, 9, 6, 6, 6, 6, 0, 6, 9, 6, 6, 6, 0, 0, 6, 9, 9, 6, 6, 9, 9, 0, 6], [6, 0, 6, 6, 0, 6, 0, 9, 9, 0, 6, 9, 0, 6, 0, 0, 6, 0, 6, 6, 6, 9, 0, 9, 9, 6, 0, 6, 6, 6, 0, 0, 0, 0, 0, 9, 6, 0, 9, 6, 9, 0, 0, 9, 6, 9, 0, 0, 6, 6, 0, 0, 6, 0, 0, 0, 0, 6, 0, 9, 0, 6, 6, 0, 0, 9, 0, 6, 0, 6, 0, 0, 0, 6, 6, 0, 9, 0, 9, 0, 9, 9, 6, 9, 9, 6, 9, 0, 0, 9, 0, 9, 0, 6, 9, 9, 6, 6, 0, 9], [9, 0, 6, 0, 9, 6, 9, 0, 9, 9, 0, 6, 0, 0, 0, 9, 6, 6, 9, 6, 0, 9, 0, 9, 6, 6, 6, 9, 6, 0, 6, 6, 6, 0, 0, 0, 0, 6, 0, 6, 0, 6, 6, 6, 6, 0, 9, 0, 0, 9, 0, 9, 6, 6, 9, 9, 9, 9, 9, 0, 9, 0, 6, 0, 0, 6, 6, 6, 0, 9, 0, 0, 6, 6, 9, 0, 6, 6, 6, 9, 6, 6, 0, 6, 0, 9, 9, 6, 6, 6, 0, 0, 0, 9, 6, 6, 9, 6, 0, 9], [9, 6, 9, 0, 6, 0, 0, 6, 6, 9, 0, 9, 6, 6, 6, 0, 6, 9, 0, 9, 9, 9, 0, 6, 0, 0, 9, 0, 9, 0, 0, 0, 0, 0, 0, 0, 6, 9, 6, 0, 6, 0, 9, 6, 6, 9, 0, 0, 6, 0, 6, 6, 9, 9, 0, 0, 9, 0, 9, 9, 6, 0, 0, 6, 9, 6, 6, 0, 9, 9, 0, 9, 6, 9, 9, 0, 9, 9, 0, 0, 0, 0, 0, 9, 9, 6, 6, 9, 0, 9, 6, 9, 9, 9, 6, 0, 9, 9, 9, 9], [9, 9, 9, 9, 6, 9, 9, 0, 0, 0, 0, 6, 9, 0, 6, 9, 6, 0, 0, 6, 9, 0, 0, 6, 0, 0, 6, 0, 6, 6, 9, 6, 6, 0, 9, 0, 6, 0, 9, 6, 6, 9, 6, 6, 9, 9, 9, 0, 0, 9, 0, 6, 6, 6, 9, 0, 9, 6, 0, 0, 9, 6, 9, 0, 9, 0, 9, 9, 0, 6, 0, 6, 6, 6, 9, 9, 6, 9, 6, 9, 6, 9, 6, 9, 9, 0, 0, 9, 0, 0, 9, 6, 6, 9, 0, 0, 6, 9, 6, 6], [6, 0, 0, 0, 6, 0, 0, 0, 9, 0, 9, 0, 6, 0, 6, 0, 6, 6, 9, 9, 6, 9, 0, 0, 6, 6, 0, 6, 6, 9, 0, 0, 9, 6, 0, 9, 9, 6, 9, 9, 6, 9, 6, 0, 9, 9, 6, 0, 9, 6, 9, 9, 0, 9, 0, 0, 9, 9, 9, 6, 6, 6, 6, 6, 6, 6, 0, 6, 9, 9, 9, 0, 0, 6, 6, 0, 9, 0, 9, 6, 6, 6, 9, 9, 9, 6, 9, 9, 0, 0, 6, 9, 0, 0, 0, 6, 6, 0, 6, 9], [6, 0, 0, 0, 0, 0, 0, 0, 0, 6, 9, 9, 9, 6, 9, 6, 0, 6, 6, 0, 6, 9, 0, 6, 0, 6, 0, 6, 6, 9, 6, 9, 9, 9, 9, 9, 6, 0, 0, 0, 6, 9, 6, 9, 9, 6, 9, 0, 9, 6, 0, 6, 9, 6, 6, 9, 6, 9, 9, 6, 9, 0, 0, 6, 6, 0, 9, 6, 6, 6, 6, 6, 0, 6, 6, 0, 9, 6, 9, 0, 9, 0, 0, 6, 9, 0, 6, 0, 9, 6, 9, 9, 0, 9, 0, 9, 6, 6, 9, 9], [6, 6, 9, 0, 6, 6, 6, 0, 6, 9, 6, 6, 9, 6, 9, 6, 6, 9, 9, 9, 9, 9, 0, 0, 9, 9, 0, 6, 9, 6, 9, 0, 9, 0, 9, 0, 0, 6, 0, 9, 0, 0, 9, 9, 9, 9, 0, 6, 9, 0, 9, 0, 6, 0, 9, 9, 6, 9, 0, 0, 9, 9, 0, 6, 9, 0, 6, 0, 6, 0, 6, 0, 0, 0, 0, 9, 9, 6, 9, 0, 0, 6, 9, 6, 6, 0, 9, 6, 0, 0, 0, 6, 0, 0, 0, 6, 0, 0, 6, 6], [0, 0, 6, 0, 0, 9, 0, 9, 9, 9, 0, 9, 9, 0, 9, 0, 0, 6, 6, 9, 0, 0, 6, 0, 9, 0, 0, 6, 0, 0, 0, 0, 9, 6, 9, 6, 6, 9, 9, 9, 0, 6, 6, 9, 9, 0, 9, 6, 9, 6, 6, 9, 6, 6, 9, 9, 6, 0, 6, 9, 6, 0, 0, 0, 0, 0, 0, 0, 6, 9, 0, 9, 6, 9, 9, 0, 6, 9, 6, 9, 9, 6, 9, 9, 6, 9, 9, 9, 6, 9, 0, 9, 0, 9, 0, 9, 0, 0, 0, 0], [6, 9, 6, 6, 0, 6, 6, 6, 0, 9, 9, 0, 9, 0, 9, 6, 6, 9, 0, 6, 6, 0, 9, 9, 9, 9, 9, 9, 6, 6, 9, 6, 0, 0, 6, 0, 0, 9, 6, 0, 6, 9, 6, 6, 0, 6, 6, 0, 0, 6, 9, 6, 9, 0, 0, 6, 0, 0, 9, 0, 6, 6, 6, 9, 0, 9, 6, 6, 6, 0, 6, 9, 0, 0, 0, 0, 9, 0, 6, 0, 9, 6, 0, 6, 6, 9, 6, 6, 0, 9, 0, 9, 0, 6, 0, 6, 9, 6, 0, 0], [6, 6, 0, 6, 9, 6, 9, 9, 0, 9, 9, 6, 6, 6, 9, 6, 6, 0, 0, 0, 0, 6, 9, 0, 0, 9, 0, 9, 6, 9, 9, 0, 6, 9, 6, 9, 0, 9, 6, 9, 6, 0, 0, 6, 6, 9, 0, 0, 9, 9, 0, 6, 6, 6, 9, 6, 0, 0, 0, 9, 6, 9, 6, 0, 0, 0, 6, 0, 9, 6, 9, 0, 0, 6, 6, 6, 0, 0, 0, 0, 6, 6, 9, 6, 6, 9, 9, 0, 9, 6, 9, 6, 6, 9, 0, 9, 0, 6, 9, 9], [6, 9, 9, 6, 0, 0, 0, 6, 9, 6, 6, 6, 0, 0, 6, 0, 9, 9, 0, 9, 9, 6, 9, 6, 6, 6, 0, 0, 0, 0, 6, 0, 9, 0, 6, 9, 9, 0, 9, 6, 6, 9, 0, 6, 6, 6, 6, 6, 6, 9, 6, 9, 6, 9, 0, 9, 0, 6, 9, 0, 6, 6, 0, 0, 9, 6, 6, 0, 9, 0, 6, 6, 0, 6, 0, 6, 9, 0, 9, 9, 0, 9, 9, 0, 6, 0, 6, 0, 9, 9, 9, 9, 0, 0, 6, 6, 9, 9, 0, 0], [6, 0, 0, 9, 9, 0, 0, 9, 9, 6, 6, 9, 9, 9, 9, 0, 0, 0, 6, 6, 6, 9, 9, 6, 6, 0, 0, 0, 9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 9, 6, 6, 6, 0, 9, 0, 9, 0, 6, 0, 6, 0, 6, 6, 6, 9, 9, 6, 6, 0, 0, 6, 0, 6, 0, 0, 0, 9, 9, 0, 0, 9, 0, 0, 9, 0, 6, 6, 9, 0, 9, 0, 9, 0, 9, 9, 6, 6, 6, 6, 6, 0, 6, 9, 9, 6, 9, 0, 0, 6, 6], [6, 6, 0, 6, 9, 6, 9, 9, 9, 0, 0, 6, 6, 0, 9, 6, 0, 0, 0, 6, 0, 0, 9, 6, 9, 6, 0, 6, 0, 0, 6, 9, 6, 6, 6, 9, 9, 0, 9, 0, 0, 9, 6, 6, 6, 9, 0, 0, 9, 9, 0, 0, 9, 9, 0, 0, 9, 6, 6, 6, 0, 6, 0, 6, 6, 6, 6, 6, 6, 0, 0, 0, 0, 0, 6, 6, 6, 9, 9, 0, 0, 6, 6, 6, 0, 9, 0, 0, 0, 0, 0, 9, 6, 9, 0, 9, 0, 9, 0, 9], [6, 6, 0, 9, 0, 9, 9, 0, 0, 9, 6, 6, 9, 9, 6, 0, 6, 0, 0, 6, 0, 9, 6, 6, 9, 9, 6, 9, 0, 6, 6, 6, 6, 9, 9, 6, 6, 6, 6, 6, 6, 9, 0, 6, 9, 0, 6, 0, 9, 0, 6, 0, 6, 6, 6, 0, 0, 6, 9, 9, 9, 9, 6, 0, 9, 6, 9, 0, 0, 9, 6, 9, 6, 6, 0, 9, 9, 0, 6, 6, 6, 0, 0, 6, 6, 0, 6, 9, 0, 6, 9, 6, 0, 0, 9, 0, 0, 6, 9, 6], [0, 6, 0, 6, 0, 0, 6, 0, 6, 6, 9, 6, 9, 0, 0, 0, 9, 0, 0, 0, 9, 9, 6, 0, 9, 0, 0, 9, 9, 9, 9, 9, 0, 9, 0, 6, 9, 0, 9, 9, 0, 0, 0, 0, 0, 0, 6, 0, 0, 6, 6, 0, 0, 6, 6, 9, 0, 0, 6, 9, 0, 6, 0, 6, 9, 6, 0, 0, 6, 6, 0, 9, 0, 0, 9, 6, 0, 0, 6, 9, 6, 0, 6, 0, 6, 0, 6, 6, 0, 9, 9, 0, 9, 9, 0, 0, 6, 6, 9, 9], [0, 6, 0, 0, 9, 0, 6, 0, 6, 6, 6, 6, 6, 0, 6, 9, 6, 0, 0, 9, 9, 0, 9, 9, 0, 9, 6, 9, 6, 6, 9, 6, 9, 6, 9, 0, 0, 6, 6, 0, 9, 9, 6, 6, 9, 0, 0, 6, 0, 0, 9, 6, 9, 0, 0, 6, 9, 6, 9, 9, 0, 9, 0, 9, 9, 6, 6, 0, 9, 6, 9, 9, 0, 9, 0, 9, 0, 9, 0, 0, 9, 9, 0, 0, 6, 9, 9, 9, 9, 0, 6, 6, 6, 9, 0, 6, 9, 9, 9, 6], [6, 6, 6, 0, 0, 6, 6, 6, 9, 9, 9, 9, 6, 9, 9, 9, 6, 9, 6, 0, 9, 9, 9, 0, 9, 9, 9, 6, 0, 0, 9, 9, 6, 6, 9, 6, 6, 6, 9, 0, 0, 6, 9, 9, 9, 9, 0, 6, 6, 0, 9, 6, 6, 9, 9, 0, 9, 6, 0, 0, 6, 6, 9, 0, 0, 9, 0, 0, 6, 0, 9, 0, 9, 9, 6, 6, 9, 0, 0, 0, 9, 6, 0, 6, 6, 6, 6, 9, 6, 9, 0, 0, 6, 6, 0, 9, 0, 0, 9, 9], [0, 0, 0, 9, 9, 9, 0, 0, 6, 0, 9, 6, 9, 0, 9, 9, 9, 0, 0, 0, 6, 9, 9, 9, 0, 0, 9, 6, 9, 6, 6, 0, 0, 6, 9, 0, 6, 0, 9, 9, 6, 0, 6, 9, 0, 6, 6, 9, 0, 6, 6, 9, 0, 6, 9, 0, 6, 9, 9, 0, 0, 6, 0, 0, 0, 0, 0, 0, 9, 9, 9, 0, 6, 9, 6, 0, 0, 0, 0, 0, 0, 6, 6, 9, 9, 0, 0, 9, 9, 0, 0, 6, 9, 6, 6, 9, 9, 6, 9, 9], [0, 0, 9, 6, 6, 0, 0, 9, 0, 6, 9, 9, 6, 0, 9, 9, 0, 6, 9, 6, 9, 0, 0, 9, 0, 9, 0, 0, 0, 0, 9, 9, 0, 9, 6, 6, 6, 0, 0, 0, 6, 9, 0, 6, 6, 0, 0, 9, 9, 0, 9, 6, 6, 6, 0, 0, 9, 0, 0, 0, 6, 6, 9, 6, 0, 9, 0, 0, 9, 9, 0, 0, 9, 0, 6, 6, 0, 9, 0, 6, 6, 0, 6, 6, 6, 0, 0, 9, 0, 6, 9, 6, 9, 0, 0, 6, 9, 9, 0, 9]])

runner.render(time_limit=6.0)