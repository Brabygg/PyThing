import ui

locs = {
    "test_window_1": ui.window(1, "balls1", ["balls2", "balls3"], [2, 3]),
    "test_window_2": ui.window(2, "balls2", ["balls1", "balls3"], [1, 3]),
    "test_window_3": ui.window(3, "balls3", ["balls1", "balls2"], [1, 2])
}