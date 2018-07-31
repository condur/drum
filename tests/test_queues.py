from algo import queues


def test_numIslands():
    assert queues.numIslands([["1", "0", "1", "1", "0", "1", "1"]]) == 3
    assert queues.numIslands([["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]]) == 1
    assert (
        queues.numIslands(
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ]
        )
        == 1
    )
    assert (
        queues.numIslands(
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ]
        )
        == 3
    )
