#数据导入与导出
import pandas as pd
import numpy as np

# 从CSV文件导入
df = pd.read_csv('文件路径.csv')

# 从Excel文件导入
df = pd.read_excel('文件路径.xlsx', sheet_name='Sheet1')

# 从SQL查询导入
from sqlalchemy import create_engine
engine = create_engine('sqlite:///数据库.db')
df = pd.read_sql('SELECT * FROM 表名', engine)

# 从字典创建DataFrame
data = {'姓名': ['张三', '李四', '王五'],
        '年龄': [25, 30, 35],
        '城市': ['北京', '上海', '广州']}
df = pd.DataFrame(data)
导出数据
# 导出到CSV
df.to_csv('输出文件.csv', index=False, encoding='utf-8-sig')

# 导出到Excel
df.to_excel('输出文件.xlsx', sheet_name='Sheet1', index=False)

# 导出到SQL
df.to_sql('表名', engine, if_exists='replace', index=False)
数据查看与基本信息
# 创建示例数据
data = {
    '姓名': ['张三', '李四', '王五', '赵六', '钱七'],
    '年龄': [25, 30, 35, 40, 45],
    '城市': ['北京', '上海', '广州', '深圳', '杭州'],
    '工资': [10000, 15000, 12000, 20000, 25000],
    '入职日期': ['2020-01-15', '2019-05-20', '2021-03-10', '2018-07-05', '2022-02-28']
}
df = pd.DataFrame(data)
df['入职日期'] = pd.to_datetime(df['入职日期'])

# 查看前几行数据
df.head(3)  # 默认显示前5行，这里指定显示前3行

# 查看后几行数据
df.tail(2)  # 显示最后2行

# 查看数据框的基本信息
df.info()  # 显示索引、数据类型和内存信息等

# 查看数值型数据的统计摘要
df.describe()  # 计算平均值、标准差、最小值、最大值等

# 查看数据框的形状（行数和列数）
df.shape  # 返回元组 (行数, 列数)

# 查看列名
df.columns

# 查看索引
df.index

# 检查缺失值
df.isnull().sum()  # 每列的缺失值数量
数据选择与过滤
选择列
# 选择单列（返回Series）
df['姓名']

# 选择多列（返回DataFrame）
df[['姓名', '年龄']]

# 使用点号选择列（仅适用于列名是有效Python标识符的情况）
df.年龄
选择行
# 使用位置索引选择行
df.iloc[0]  # 选择第一行
df.iloc[1:4]  # 选择第2-4行
df.iloc[[0, 2, 4]]  # 选择第1、3、5行

# 使用标签索引选择行（如果设置了索引）
df.set_index('姓名', inplace=True)  # 将'姓名'列设为索引
df.loc['张三']  # 选择索引为'张三'的行
df.loc[['张三', '王五']]  # 选择多行

# 重置索引
df.reset_index(inplace=True)  # 将索引重置为默认的整数索引
条件过滤
# 单条件过滤
df[df['年龄'] > 30]

# 多条件过滤（与）
df[(df['年龄'] > 30) & (df['工资'] > 15000)]

# 多条件过滤（或）
df[(df['城市'] == '北京') | (df['城市'] == '上海')]

# 使用isin()过滤
df[df['城市'].isin(['北京', '上海', '广州'])]

# 使用query()方法（更直观的语法）
df.query('年龄 > 30 and 工资 > 15000')
选择行和列（组合使用iloc和loc）
# 使用iloc选择特定位置的数据
df.iloc[0, 1]  # 第1行，第2列的值
df.iloc[0:2, 1:3]  # 第1-2行，第2-3列

# 使用loc选择特定标签的数据
df.loc[0, '年龄']  # 索引为0的行，'年龄'列的值
df.loc[0:2, ['姓名', '年龄']]  # 索引为0-2的行，'姓名'和'年龄'列
数据清洗与处理
处理缺失值
# 创建带有缺失值的数据
data_missing = {
    '姓名': ['张三', '李四', '王五', '赵六', None],
    '年龄': [25, None, 35, 40, 45],
    '城市': ['北京', '上海', None, '深圳', '杭州'],
    '工资': [10000, 15000, None, 20000, 25000]
}
df_missing = pd.DataFrame(data_missing)

# 检查缺失值
df_missing.isnull().sum()

# 删除包含任何缺失值的行
df_clean1 = df_missing.dropna()

# 删除特定列中有缺失值的行
df_clean2 = df_missing.dropna(subset=['姓名', '年龄'])

# 填充缺失值 - 固定值
df_filled1 = df_missing.fillna({'姓名': '未知', '年龄': 0, '城市': '未知', '工资': 0})

# 填充缺失值 - 前向填充
df_filled2 = df_missing.fillna(method='ffill')

# 填充缺失值 - 后向填充
df_filled3 = df_missing.fillna(method='bfill')

# 填充缺失值 - 使用统计值
df_filled4 = df_missing.copy()
df_filled4['年龄'] = df_filled4['年龄'].fillna(df_filled4['年龄'].mean())
df_filled4['工资'] = df_filled4['工资'].fillna(df_filled4['工资'].median())
数据类型转换
# 查看数据类型
df.dtypes

# 转换数据类型
df['工资'] = df['工资'].astype('float')
df['年龄'] = df['年龄'].astype('int')

# 转换为日期类型
df['入职日期'] = pd.to_datetime(df['入职日期'])

# 转换为分类类型（节省内存）
df['城市'] = df['城市'].astype('category')
重命名列
# 重命名单个或多个列
df.rename(columns={'姓名': 'name', '年龄': 'age'}, inplace=True)

# 重命名所有列
df.columns = ['name', 'age', 'city', 'salary', 'hire_date']
删除重复行
# 创建带有重复行的数据
data_dup = {
    '姓名': ['张三', '李四', '张三', '王五', '李四'],
    '城市': ['北京', '上海', '北京', '广州', '上海']
}
df_dup = pd.DataFrame(data_dup)

# 查找重复行
df_dup.duplicated()

# 删除完全重复的行
df_unique = df_dup.drop_duplicates()

# 根据特定列删除重复行（保留第一次出现的）
df_unique_name = df_dup.drop_duplicates(subset=['姓名'])

# 根据特定列删除重复行（保留最后一次出现的）
df_unique_name_last = df_dup.drop_duplicates(subset=['姓名'], keep='last')
数据转换与重塑
排序
# 按单列排序
df.sort_values('年龄')

# 按多列排序
df.sort_values(['城市', '工资'], ascending=[True, False])  # 城市升序，工资降序

# 按索引排序
df.sort_index()
添加和删除列
# 添加新列
df['奖金'] = df['工资'] * 0.1

# 使用apply添加列
df['工资等级'] = df['工资'].apply(lambda x: 'A' if x > 20000 else ('B' if x > 10000 else 'C'))

# 删除列
df_reduced = df.drop(['奖金'], axis=1)

# 删除多列
df_reduced = df.drop(['奖金', '工资等级'], axis=1)
数据透视表
# 创建示例数据
sales_data = {
    '日期': pd.date_range(start='2023-01-01', periods=20),
    '产品': np.random.choice(['A产品', 'B产品', 'C产品'], 20),
    '区域': np.random.choice(['北区', '南区', '东区', '西区'], 20),
    '销售额': np.random.randint(1000, 10000, 20),
    '数量': np.random.randint(10, 100, 20)
}
df_sales = pd.DataFrame(sales_data)

# 创建数据透视表
pivot_table = pd.pivot_table(df_sales, 
                           values='销售额', 
                           index='区域',
                           columns='产品',
                           aggfunc='sum',
                           fill_value=0)

# 多值数据透视表
pivot_table_multi = pd.pivot_table(df_sales,
                                 values=['销售额', '数量'],
                                 index='区域',
                                 columns='产品',
                                 aggfunc={'销售额': 'sum', '数量': 'mean'},
                                 fill_value=0)
数据重塑（melt）
# 从宽格式转为长格式
df_wide = pivot_table.reset_index()
df_long = pd.melt(df_wide, 
                id_vars=['区域'],
                value_vars=['A产品', 'B产品', 'C产品'],
                var_name='产品',
                value_name='销售额')
数据聚合与分组
基本聚合
# 计算整个DataFrame的统计量
df['工资'].mean()  # 平均值
df['工资'].median()  # 中位数
df['工资'].min()  # 最小值
df['工资'].max()  # 最大值
df['工资'].sum()  # 总和
df['工资'].std()  # 标准差
df['工资'].var()  # 方差
df['工资'].quantile(0.75)  # 75%分位数
df['工资'].count()  # 非缺失值计数
df['工资'].nunique()  # 唯一值数量
分组聚合
# 创建示例数据
data_group = {
    '部门': ['技术', '技术', '技术', '销售', '销售', '市场', '市场', '市场'],
    '性别': ['男', '女', '男', '女', '男', '女', '男', '女'],
    '工资': [12000, 15000, 10000, 8000, 9000, 7000, 8000, 6000],
    '年龄': [28, 26, 30, 29, 32, 25, 28, 24]
}
df_group = pd.DataFrame(data_group)

# 单列分组
df_group.groupby('部门')['工资'].mean()

# 多列分组
df_group.groupby(['部门', '性别'])['工资'].mean()

# 多个聚合函数
df_group.groupby('部门')['工资'].agg(['mean', 'median', 'min', 'max', 'count'])

# 对不同列应用不同的聚合函数
df_group.groupby('部门').agg({
    '工资': ['mean', 'max'],
    '年龄': ['mean', 'min']
})

# 自定义聚合函数
def range_diff(x):
    return x.max() - x.min()

df_group.groupby('部门')['工资'].agg(range_diff)

# 分组后应用转换
df_group['工资_部门占比'] = df_group['工资'] / df_group.groupby('部门')['工资'].transform('sum')
数据合并与连接
合并DataFrame
# 创建示例数据
df1 = pd.DataFrame({
    '员工ID': [1, 2, 3, 4, 5],
    '姓名': ['张三', '李四', '王五', '赵六', '钱七'],
    '部门ID': [101, 102, 101, 103, 102]
})

df2 = pd.DataFrame({
    '部门ID': [101, 102, 103],
    '部门名称': ['技术部', '销售部', '市场部'],
    '部门主管': ['刘一', '陈二', '孙三']
})

df3 = pd.DataFrame({
    '员工ID': [1, 2, 6, 7],
    '绩效': ['A', 'B', 'A', 'C']
})

# 内连接（只保留匹配的行）
merged_inner = pd.merge(df1, df2, on='部门ID', how='inner')

# 左连接（保留左表所有行）
merged_left = pd.merge(df1, df2, on='部门ID', how='left')

# 右连接（保留右表所有行）
merged_right = pd.merge(df1, df2, on='部门ID', how='right')

# 外连接（保留所有行）
merged_outer = pd.merge(df1, df2, on='部门ID', how='outer')

# 不同列名的连接
df2.rename(columns={'部门ID': 'dept_id'}, inplace=True)
merged = pd.merge(df1, df2, left_on='部门ID', right_on='dept_id')

# 基于索引的连接
df1.set_index('员工ID', inplace=True)
df3.set_index('员工ID', inplace=True)
merged_index = pd.merge(df1, df3, left_index=True, right_index=True, how='inner')
连接（Concatenate）DataFrame
# 垂直连接（行连接）
df_v1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df_v2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
df_vertical = pd.concat([df_v1, df_v2], axis=0)

# 水平连接（列连接）
df_h1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df_h2 = pd.DataFrame({'C': [5, 6], 'D': [7, 8]})
df_horizontal = pd.concat([df_h1, df_h2], axis=1)

# 重置索引
df_vertical_reset = pd.concat([df_v1, df_v2], axis=0, ignore_index=True)
时间序列处理
# 创建时间序列数据
date_range = pd.date_range(start='2023-01-01', end='2023-01-31', freq='D')
ts_data = pd.Series(np.random.randn(31).cumsum() * 100 + 1000, index=date_range)

# 重采样 - 降采样（日数据到周数据）
weekly_data = ts_data.resample('W').mean()

# 重采样 - 升采样（日数据到小时数据）
hourly_data = ts_data.resample('H').ffill()  # 前向填充

# 移动窗口计算（滚动平均）
rolling_mean = ts_data.rolling(window=7).mean()

# 移动窗口计算（指数加权移动平均）
exp_weighted_mean = ts_data.ewm(span=7).mean()

# 时间偏移
ts_data.shift(1)  # 向后偏移1天
ts_data.shift(-1)  # 向前偏移1天

# 日期提取
time_df = pd.DataFrame({'date': date_range})
time_df['year'] = time_df['date'].dt.year
time_df['month'] = time_df['date'].dt.month
time_df['day'] = time_df['date'].dt.day
time_df['weekday'] = time_df['date'].dt.weekday
time_df['weekday_name'] = time_df['date'].dt.day_name()
实用案例
案例1：销售数据分析
# 创建销售数据
sales_data = {
    '日期': pd.date_range(start='2023-01-01', periods=100),
    '产品': np.random.choice(['手机', '电脑', '平板', '配件'], 100),
    '销售员': np.random.choice(['张三', '李四', '王五'], 100),
    '销售额': np.random.randint(1000, 10000, 100),
    '成本': np.random.randint(500, 5000, 100)
}
df_sales = pd.DataFrame(sales_data)

# 添加利润列
df_sales['利润'] = df_sales['销售额'] - df_sales['成本']
df_sales['利润率'] = df_sales['利润'] / df_sales['销售额']

# 按产品分组统计
product_stats = df_sales.groupby('产品').agg({
    '销售额': 'sum',
    '利润': 'sum',
    '利润率': 'mean'
}).sort_values('销售额', ascending=False)

# 按销售员和产品分组统计
salesperson_product = df_sales.pivot_table(
    values=['销售额', '利润'],
    index='销售员',
    columns='产品',
    aggfunc='sum',
    fill_value=0
)

# 时间趋势分析
df_sales['月份'] = df_sales['日期'].dt.month
monthly_sales = df_sales.groupby('月份')[['销售额', '利润']].sum()

# 找出销售额最高的前10天
top_sales_days = df_sales.groupby('日期')['销售额'].sum().nlargest(10)
案例2：用户行为分析
# 创建用户行为数据
user_data = {
    '用户ID': np.random.randint(1001, 1101, 1000),
    '日期': pd.date_range(start='2023-01-01', periods=50).repeat(20),
    '页面': np.random.choice(['首页', '产品页', '购物车', '结算页', '支付页'], 1000),
    '停留时间': np.random.randint(5, 300, 1000),
    '是否购买': np.random.choice([0, 1], 1000, p=[0.8, 0.2])
}
df_user = pd.DataFrame(user_data)

# 计算每个用户的访问次数
user_visits = df_user.groupby('用户ID').size().sort_values(ascending=False)

# 计算每个用户的平均停留时间
user_time = df_user.groupby('用户ID')['停留时间'].mean()

# 计算每个页面的转化率
page_conversion = df_user.groupby('页面')['是否购买'].mean()

# 计算每日活跃用户数
daily_active = df_user.groupby('日期')['用户ID'].nunique()

# 用户行为路径分析
user_path = df_user.sort_values(['用户ID', '日期'])
user_path['下一页面'] = user_path.groupby('用户ID')['页面'].shift(-1)

# 计算页面转换矩阵
page_transition = pd.crosstab(
    user_path['页面'], 
    user_path['下一页面'],
    normalize='index'
)
