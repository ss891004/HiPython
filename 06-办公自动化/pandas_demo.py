import numpy as np
import pandas as pd
from pandas import Series

##### 1. Series：一维带标签数组 
# 方式1：从列表创建（默认整数索引）
s1 = pd.Series([10, 20, 30, 40])
print("s1:\n", s1)
# 输出：
# 0    10
# 1    20
# 2    30
# 3    40
# dtype: int64

# 方式2：自定义索引（标签可重复、可非整数）
s2 = pd.Series([10, 20, 30], index=["北京", "上海", "广州"], name="温度")
print("\ns2:\n", s2)
# 输出：
# 北京    10
# 上海    20
# 广州    30
# Name: 温度, dtype: int64

# 方式3：从字典创建（键=索引，值=数据）
s3 = pd.Series({"苹果": 5.99, "香蕉": 3.99, "橙子": 4.99})
print("\ns3:\n", s3)

###################################################################
print("数据值：", s2.values)  # 底层 ndarray 数据（[10 20 30]）
print("索引：", s2.index)    # 索引对象（Index(['北京', '上海', '广州'], dtype='object')）
print("数据类型：", s2.dtype)# 数据类型（int64）
print("名称：", s2.name)     # 序列名称（温度）
print(s2["上海"])  # 输出：20. # 按索引标签取值（推荐，不受位置影响）
print(s2.iloc[1])  # 输出：20（索引"上海"在第1位，从0开始） # 按位置取值（类似列表）
print(s2["北京":"广州"])  # 输出所有元素  # 切片取值（含头含尾，与列表不同）


####2. DataFrame：二维带标签表格

# 方式1：从字典创建（键=列名，值=列表/Series）
data = {
    "姓名": ["张三", "李四", "王五", "赵六"],
    "年龄": [25, 30, 35, 28],
    "城市": ["北京", "上海", "广州", "深圳"],
    "薪资": [15000, 20000, 18000, 16000]
}
df = pd.DataFrame(data)  # 默认整数行索引（0,1,2,3）
print("df:\n", df)

# 方式2：自定义行索引（index 参数）
df2 = pd.DataFrame(data, index=["员工1", "员工2", "员工3", "员工4"])
print("\ndf2:\n", df2)

# 方式3：从 CSV/Excel 读取（实战常用，后续详解）
df3 = pd.read_csv("数据文件.csv")  # 读取 CSV
df4 = pd.read_excel("数据文件.xlsx")  # 读取 Excel（需安装 openpyxl：pip install openpyxl）

###########################################################
print("形状（行×列）：", df.shape)  # 输出：(4, 4)（4行4列）
print("列名：", df.columns)        # 输出列索引（Index(['姓名', '年龄', '城市', '薪资'], dtype='object')）
print("行索引：", df.index)        # 输出行索引（RangeIndex(start=0, stop=4, step=1)）
print("数据类型：\n", df.dtypes)   # 每列数据类型
print("前3行数据：\n", df.head(3)) # 快速查看前 N 行（默认5行）
print("后2行数据：\n", df.tail(2)) # 快速查看后 N 行


#1. 按列查询（取整列）
df_age = df["年龄"]  # 返回 Series # 方式1：直接用列名（推荐，最简单）
print("年龄列（Series）：\n", df_age)


df_sub = df[["姓名", "城市", "薪资"]]  # 返回 DataFrame # 方式2：取多列（列名用列表包裹）
print("\n多列数据（DataFrame）：\n", df_sub)

#2. 按行查询（取整行）
row1 = df.iloc[0]  # 取第0行（张三）. # 方式1：iloc 按位置取行（类似列表索引）
print("第0行：\n", row1)
row2_3 = df.iloc[1:3]  # 取第1-2行（左闭右开）
print("\n第1-2行：\n", row2_3)
row_emp2 = df2.loc["员工2"]  # 取"员工2"行 # 方式2：loc 按标签取行（自定义索引时常用）
print("\n员工2行：\n", row_emp2)

# 3. 按条件筛选（实战核心）
df_age_gt30 = df[df["年龄"] > 30] # 条件1：年龄>30
print("年龄>30的员工：\n", df_age_gt30)

# 条件2：城市是北京 且 薪资>15000（多条件用 &，每个条件加括号）
df_beijing_highsalary = df[(df["城市"] == "北京") & (df["薪资"] > 15000)]
print("\n北京且薪资>15000的员工：\n", df_beijing_highsalary)

# 条件3：城市是上海或深圳（用 | 表示“或”）
df_sh_sz = df[df["城市"].isin(["上海", "深圳"])]
print("\n上海或深圳的员工：\n", df_sh_sz)


# 1. 缺失值处理
# 先创建含缺失值的 DataFrame
df_missing = pd.DataFrame({
    "A": [1, 2, None, 4],
    "B": [5, None, 7, 8],
    "C": [9, 10, 11, 12]
})
print("含缺失值的 DataFrame：\n", df_missing)

print("\n每列缺失值个数：\n", df_missing.isnull().sum()) # （1）查看缺失值（每列缺失个数）

df_drop = df_missing.dropna(axis=0, how="any")  # 删除含缺失值的行 # （2）删除缺失值（axis=0删行，axis=1删列；how="any"有一个缺失就删）
print("\n删除缺失值后的 DataFrame：\n", df_drop)

# （3）填充缺失值（用均值/固定值填充）
df_fill = df_missing.fillna({
    "A": df_missing["A"].mean(),  # A列用均值填充
    "B": 0  # B列用0填充
})
print("\n填充缺失值后的 DataFrame：\n", df_fill)

# 2. 重复值处理
# 创建含重复值的 DataFrame
df_duplicate = pd.DataFrame({
    "姓名": ["张三", "李四", "张三", "王五"],
    "年龄": [25, 30, 25, 35],
    "城市": ["北京", "上海", "北京", "广州"]
})
print("含重复值的 DataFrame：\n", df_duplicate)

# （1）查看重复值（默认判断所有列都相同）
print("\n重复行：\n", df_duplicate.duplicated())

# （2）删除重复值（keep="first"保留第一行，keep=False删除所有重复行）
df_unique = df_duplicate.drop_duplicates(keep="first")
print("\n删除重复值后的 DataFrame：\n", df_unique)

#### 1. 列级运算（加减乘除
# 新增列：薪资税后（假设税率20%）
df["薪资税后"] = df["薪资"] * 0.8
print("新增税后薪资列：\n", df[["姓名", "薪资", "薪资税后"]])

# 列与列运算：年龄+5
df["年龄+5"] = df["年龄"] + 5
print("\n年龄+5列：\n", df[["姓名", "年龄", "年龄+5"]])

##### 2. 统计分析（描述性统计）
# 数值列的基础统计（均值、标准差、最值等）
print("数值列统计信息：\n", df[["年龄", "薪资", "薪资税后"]].describe())

# 单独计算统计量
print("\n薪资均值：", df["薪资"].mean())  # 均值
print("薪资中位数：", df["薪资"].median())  # 中位数
print("薪资最大值：", df["薪资"].max())  # 最大值
print("薪资最小值：", df["薪资"].min())  # 最小值
print("薪资总和：", df["薪资"].sum())  # 总和
print("城市分布：\n", df["城市"].value_counts())  # 分类计数（非数值列可用）


#### 数据保存：导出为 CSV/Excel
# 保存为 CSV（默认不保存索引，index=False 避免冗余）
df.to_csv("员工数据分析结果.csv", index=False, encoding="utf-8-sig")

# 保存为 Excel（需安装 openpyxl 库）
df.to_excel("员工数据分析结果.xlsx", index=False, sheet_name="员工数据")

print("文件保存成功！")


'''
1. 入门核心要点
记住两个数据结构：Series（一维）、DataFrame（二维）；
掌握三大查询方式：[]（列/条件）、loc（标签）、iloc（位置）；
数据清洗核心：缺失值（dropna/fillna）、重复值（duplicated/drop_duplicates）；
统计分析：describe() 一键获取基础统计，groupby() 分组分析。

2. 进阶方向
数据合并：merge()（类似 SQL 连接）、concat()（拼接）；
时间序列：to_datetime() 处理时间数据，resample() 时间采样；
透视表：pivot_table() 快速生成汇总表格；
性能优化：astype() 优化数据类型（如 category 压缩字符串）、apply() 批量处理数据。

'''