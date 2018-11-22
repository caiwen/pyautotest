from bootstrap.bootstrap import Bootstrap
from src.gui.scene import gb_login_scene


class Index:

    # 测试gb的登录场景
    @staticmethod
    def run():
        scene = gb_login_scene.GbLoginScene()
        scene.test_login()


if __name__ == "__main__":
    Bootstrap()
    Index.run()
