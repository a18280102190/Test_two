import pytest
import yaml



class TestDome():
    @pytest.mark.parametrize(
        "env,",yaml.safe_load(open("./env.yaml"))
    )
    def test_dome(self, env):
        if "test" in env:
            print('这是测试环境')
            print("测试环境的ip:",env["test"])
        elif "dev" in env :
            print('这是开发环境')
            print("这是开发环境的ip：",env["dev"])
    def test_yaml(self):
        print(yaml.safe_load(open("./env.yaml")))