
# wrf-domain-tool

`wrf-domain-tool` 是一个用于自动从多个 Shapefile 文件生成 WRF 模拟的多层嵌套 Domain 的工具，并自动输出 `namelist.wps` 配置文件。适用于需要快速构建嵌套网格的区域数值模拟工作流程。

## 特性

- 支持多个 Shapefile 输入，自动识别嵌套层级
- 自动生成 WPS 所需的 `namelist.wps`
- 易于集成至现有的 WRF 前处理流程中

## 安装

建议使用 Conda 创建独立环境并通过源代码安装：

```bash
# 创建 Conda 环境
conda create -n wrfdom python=3.10 geopandas shapely -c conda-forge

# 克隆项目仓库
git clone https://github.com/yourusername/wrf-domain-tool.git
cd wrf-domain-tool

# 安装项目
pip install .
```

## 使用说明

请参考项目中的示例 Shapefile 及文档说明，确保输入文件格式正确（必须包含投影信息等关键字段）。

## Git 操作指南（如需初始化远程仓库）

以下命令用于设置远程仓库、推送本地分支以及提交代码：

```bash
# 设置远程仓库地址（请将 your_token 替换为你的访问令牌）
git remote set-url origin https://your_token@github.com/yourusername/wrf-domain-tool.git

# 拉取远程仓库（用于合并历史）
git pull origin master --allow-unrelated-histories

# 重命名分支为 master 并推送
git branch -M master
git push -u origin master
```

```bash
# 提交和推送本地更改
git add .
git commit -m "简要描述本次提交"
git push -u origin master
```

## 许可证

本项目基于 [MIT License](LICENSE) 许可协议开放源代码。

## 联系方式

如有问题或建议，欢迎通过 Issue 或 Pull Request 与我们联系。
