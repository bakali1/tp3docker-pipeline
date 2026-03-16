import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname("__file__"), "../app")))

def test_add_task():
    add_task("Learn Docker")
    assert "Learn Docker" in get_tasks()
def test_multiple_tasks():
    add_task("ci")
    add_task("cd")
    assert "ci" in get_tasks()
    assert "cd" in get_tasks()
def test_delete_task():
    add_task("hi")
    delete_task("hi")
    assert "hi" not in get_tasks()