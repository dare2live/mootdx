# 安装方式

tdxhub 当前以 GitHub fork 为准维护。仓库名已经切到 `tdxhub`，但包名和命令行入口仍然保持为 `mootdx`。

## 推荐安装

### 直接从 GitHub 安装

```shell
pip install -U "git+https://github.com/dare2live/tdxhub.git"
```

如果需要 CLI：

```shell
pip install -U "mootdx[cli] @ git+https://github.com/dare2live/tdxhub.git"
```

如果需要 holiday / JS 扩展运行时：

```shell
pip install -U "mootdx[racer] @ git+https://github.com/dare2live/tdxhub.git"
```

如果两者都需要：

```shell
pip install -U "mootdx[cli,racer] @ git+https://github.com/dare2live/tdxhub.git"
```

适用场景：

- 需要直接使用当前 fork 的最新能力
- 不希望继续依赖上游 README 里的旧链接和旧说明

## 本地开发安装

```shell
git clone https://github.com/dare2live/tdxhub.git
cd tdxhub
pip install -e ".[cli,racer]"
```

如果使用 Poetry：

```shell
poetry install --extras cli --extras racer
```

## 安装后验证

```shell
python -c "from mootdx.quotes import Quotes; print(Quotes)"
```

如果安装了 `cli` extra，再验证：

```shell
mootdx --help
```

## 兼容性说明

- GitHub 仓库名：`tdxhub`
- Python 导入路径：`mootdx`
- CLI 命令：`mootdx`

这是兼容性选择，不代表当前文档仍以上游仓库为准。

