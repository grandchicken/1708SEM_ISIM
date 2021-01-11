import d2lzh as d2l
from mxnet import autograd, gluon, nd
from mxnet.gluon import data as gdata, loss as gloss, nn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import RobustScaler
from sklearn.pipeline import Pipeline
from scipy.stats import skew
from sklearn.decomposition import PCA
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import Lasso

from sklearn.base import BaseEstimator, TransformerMixin, RegressorMixin, clone
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import RobustScaler, StandardScaler
from sklearn.metrics import mean_squared_error
from sklearn.pipeline import Pipeline, make_pipeline
from scipy.stats import skew
from sklearn.decomposition import PCA, KernelPCA
from sklearn.preprocessing import Imputer

from sklearn.model_selection import cross_val_score, GridSearchCV, KFold
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, ExtraTreesRegressor
from sklearn.svm import SVR, LinearSVR
from sklearn.linear_model import ElasticNet, SGDRegressor, BayesianRidge
from sklearn.kernel_ridge import KernelRidge
from xgboost import XGBRegressor

warnings.filterwarnings('ignore')
plt.style.use('ggplot')  # 样式美化

trainF = 'train.csv'
testF = 'test.csv'

train = pd.read_csv(trainF)
test = pd.read_csv(testF)
# print(train)

# 数据可视化
# ***用rapidMiner对整体的数据做一个可视化，再选出标志性的数据用python进行可视化即可。***
plt.figure(figsize=(15, 8))
sns.scatterplot(train.GarageYrBlt, train.SalePrice)
plt.show()
sns.boxplot(train.GarageYrBlt, train.SalePrice)
plt.show()

# 数据清洗
# 没有去除相隔很远的值（不知道有必要吗？）

# 缺失值
isNull_train = train.isnull().sum()
print("train数据集的缺失情况")
print(isNull_train[isNull_train > 0])

isNull_test = test.isnull().sum()
print("test数据集的缺失情况")
print(isNull_test[isNull_test > 0])

# 把训练集和测试集合并
all = pd.concat([train, test], ignore_index=True)
print(all.shape)  # (2917, 81)
all.drop(['Id'], axis=1, inplace=True)

# 以下为填充特征部分
# 没有Pool...数值型 用None填充
cols = ["MasVnrArea", "BsmtUnfSF", "TotalBsmtSF", "GarageCars", "BsmtFinSF2", "BsmtFinSF1", "GarageArea"]
for col in cols:
    all[col].fillna(0, inplace=True)

# 没有Pool...字符 用None填充
cols1 = ["PoolQC", "MiscFeature", "Alley", "Fence", "FireplaceQu", "GarageQual", "GarageCond", "GarageFinish",
         "GarageYrBlt", "GarageType", "BsmtExposure", "BsmtCond", "BsmtQual", "BsmtFinType2", "BsmtFinType1",
         "MasVnrType"]
for col in cols1:
    all[col].fillna("None", inplace=True)

# 众数填充
cols2 = ["MSZoning", "BsmtFullBath", "BsmtHalfBath", "Utilities", "Functional", "Electrical", "KitchenQual", "SaleType",
         "Exterior1st", "Exterior2nd"]
for col in cols2:
    all[col].fillna(all[col].mode()[0], inplace=True)

# group by 'Neighborhood'   25组
a = all.groupby(['Neighborhood'])[['LotFrontage']].agg(['mean', 'median', 'count'])
print(a)
# group by 'Neighborhood'
# 10（组） ***参数可调节***
all["LotAreaCut"] = pd.qcut(all.LotArea, 10)
b = all.groupby(['LotAreaCut'])[['LotFrontage']].agg(['mean', 'median', 'count'])
print(b)
# 小于 25*10组
c = all.groupby(['LotAreaCut', 'Neighborhood'])['LotFrontage'].agg(['mean', 'median', 'count'])
print(c)

# mean, median, count三个参数可调节
all['LotFrontage'] = all.groupby(['LotAreaCut', 'Neighborhood'])['LotFrontage'].transform(
    lambda x: x.fillna(x.median()))
# 还有9个空缺的
all['LotFrontage'] = all.groupby(['LotAreaCut'])['LotFrontage'].transform(lambda x: x.fillna(x.median()))

isNull_all = all.isnull().sum()
print("数据填充后，all数据集的缺失情况")
print(isNull_all[isNull_all > 0].sort_values(ascending=False))

# 离散数据的排序
# 将数值类型变为str型，为后面做准备
NumStr = ["MSSubClass", "BsmtFullBath", "BsmtHalfBath", "HalfBath", "BedroomAbvGr", "KitchenAbvGr", "MoSold", "YrSold",
          "YearBuilt", "YearRemodAdd", "LowQualFinSF", "GarageYrBlt"]
for col in NumStr:
    all[col] = all[col].astype(str)


# 有尽可能多的属性，让模型自己选择需要的属性。

# value-mapping, 增加了很多属性
# all.groupby(['MSSubClass'])[['SalePrice']].agg(['mean', 'median', 'count'])
# a = all.groupby(['MSSubClass'])[['SalePrice']].agg(['mean', 'median', 'count'])
# print(a)
def map_values():
    all["oMSSubClass"] = all.MSSubClass.map({'180': 1,
                                             '30': 2, '45': 2,
                                             '190': 3, '50': 3, '90': 3,
                                             '85': 4, '40': 4, '160': 4,
                                             '70': 5, '20': 5, '75': 5, '80': 5, '150': 5,
                                             '120': 6, '60': 6})

    all["oMSZoning"] = all.MSZoning.map({'C (all)': 1, 'RH': 2, 'RM': 2, 'RL': 3, 'FV': 4})

    all["oNeighborhood"] = all.Neighborhood.map({'MeadowV': 1,
                                                 'IDOTRR': 2, 'BrDale': 2,
                                                 'OldTown': 3, 'Edwards': 3, 'BrkSide': 3,
                                                 'Sawyer': 4, 'Blueste': 4, 'SWISU': 4, 'NAmes': 4,
                                                 'NPkVill': 5, 'Mitchel': 5,
                                                 'SawyerW': 6, 'Gilbert': 6, 'NWAmes': 6,
                                                 'Blmngtn': 7, 'CollgCr': 7, 'ClearCr': 7, 'Crawfor': 7,
                                                 'Veenker': 8, 'Somerst': 8, 'Timber': 8,
                                                 'StoneBr': 9,
                                                 'NoRidge': 10, 'NridgHt': 10})

    all["oCondition1"] = all.Condition1.map({'Artery': 1,
                                             'Feedr': 2, 'RRAe': 2,
                                             'Norm': 3, 'RRAn': 3,
                                             'PosN': 4, 'RRNe': 4,
                                             'PosA': 5, 'RRNn': 5})

    all["oBldgType"] = all.BldgType.map({'2fmCon': 1, 'Duplex': 1, 'Twnhs': 1, '1Fam': 2, 'TwnhsE': 2})

    all["oHouseStyle"] = all.HouseStyle.map({'1.5Unf': 1,
                                             '1.5Fin': 2, '2.5Unf': 2, 'SFoyer': 2,
                                             '1Story': 3, 'SLvl': 3,
                                             '2Story': 4, '2.5Fin': 4})

    all["oExterior1st"] = all.Exterior1st.map({'BrkComm': 1,
                                               'AsphShn': 2, 'CBlock': 2, 'AsbShng': 2,
                                               'WdShing': 3, 'Wd Sdng': 3, 'MetalSd': 3, 'Stucco': 3, 'HdBoard': 3,
                                               'BrkFace': 4, 'Plywood': 4,
                                               'VinylSd': 5,
                                               'CemntBd': 6,
                                               'Stone': 7, 'ImStucc': 7})

    all["oMasVnrType"] = all.MasVnrType.map({'BrkCmn': 1, 'None': 1, 'BrkFace': 2, 'Stone': 3})

    all["oExterQual"] = all.ExterQual.map({'Fa': 1, 'TA': 2, 'Gd': 3, 'Ex': 4})

    all["oFoundation"] = all.Foundation.map({'Slab': 1,
                                             'BrkTil': 2, 'CBlock': 2, 'Stone': 2,
                                             'Wood': 3, 'PConc': 4})

    all["oBsmtQual"] = all.BsmtQual.map({'Fa': 2, 'None': 1, 'TA': 3, 'Gd': 4, 'Ex': 5})

    all["oBsmtExposure"] = all.BsmtExposure.map({'None': 1, 'No': 2, 'Av': 3, 'Mn': 3, 'Gd': 4})

    all["oHeating"] = all.Heating.map({'Floor': 1, 'Grav': 1, 'Wall': 2, 'OthW': 3, 'GasW': 4, 'GasA': 5})

    all["oHeatingQC"] = all.HeatingQC.map({'Po': 1, 'Fa': 2, 'TA': 3, 'Gd': 4, 'Ex': 5})

    all["oKitchenQual"] = all.KitchenQual.map({'Fa': 1, 'TA': 2, 'Gd': 3, 'Ex': 4})

    all["oFunctional"] = all.Functional.map(
        {'Maj2': 1, 'Maj1': 2, 'Min1': 2, 'Min2': 2, 'Mod': 2, 'Sev': 2, 'Typ': 3})

    all["oFireplaceQu"] = all.FireplaceQu.map({'None': 1, 'Po': 1, 'Fa': 2, 'TA': 3, 'Gd': 4, 'Ex': 5})

    all["oGarageType"] = all.GarageType.map({'CarPort': 1, 'None': 1,
                                             'Detchd': 2,
                                             '2Types': 3, 'Basment': 3,
                                             'Attchd': 4, 'BuiltIn': 5})

    all["oGarageFinish"] = all.GarageFinish.map({'None': 1, 'Unf': 2, 'RFn': 3, 'Fin': 4})

    all["oPavedDrive"] = all.PavedDrive.map({'N': 1, 'P': 2, 'Y': 3})

    all["oSaleType"] = all.SaleType.map({'COD': 1, 'ConLD': 1, 'ConLI': 1, 'ConLw': 1, 'Oth': 1, 'WD': 1,
                                         'CWD': 2, 'Con': 3, 'New': 3})

    all["oSaleCondition"] = all.SaleCondition.map(
        {'AdjLand': 1, 'Abnorml': 2, 'Alloca': 2, 'Family': 2, 'Normal': 3, 'Partial': 4})

    return "Done!"


print(all.shape)  # 103

# drop 2个刚才创建的辅助属性
all.drop("LotAreaCut", axis=1, inplace=True)
all.drop(['SalePrice'], axis=1, inplace=True)


# Pipeline模式
class labelenc(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        lab = LabelEncoder()  # LabelEncoder是对不连续的数字或文本编号。
        X["YearBuilt"] = lab.fit_transform(X["YearBuilt"])
        X["YearRemodAdd"] = lab.fit_transform(X["YearRemodAdd"])
        X["GarageYrBlt"] = lab.fit_transform(X["GarageYrBlt"])
        return X


# dummy 编码
class skew_dummies(BaseEstimator, TransformerMixin):
    def __init__(self, skew=0.5):
        self.skew = skew

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X_numeric = X.select_dtypes(exclude=["object"])
        skewness = X_numeric.apply(lambda x: skew(x))
        skewness_features = skewness[abs(skewness) >= self.skew].index
        X[skewness_features] = np.log1p(X[skewness_features])
        X = pd.get_dummies(X)  # 哑变量编码
        return X


# 建立 pipeline
pipe = Pipeline([
    ('labenc', labelenc()),
    ('skew_dummies', skew_dummies(skew=1)),
])

# 数据定义、存储
all2 = all.copy()
data_pipe = pipe.fit_transform(all2)
print(data_pipe.shape)

scaler = RobustScaler()

# 增加属性后的所有的数据
n_train = train.shape[0]  # 训练集的个数
X = data_pipe[:n_train]  # 训练集的特征
test_X = data_pipe[n_train:]  # 测试集的特征
y = train.SalePrice  # 训练集的label
X_scaled = scaler.fit(X).transform(X)  # 归一化后的训练集的特征
y_log = np.log(y)  # 取对数后的y
test_X_scaled = scaler.transform(test_X)  # 归一化后的测试集的特征

# 用Lasso做属性选择
# 压缩估计。强制系数绝对值之和小于某个固定值。

lasso = Lasso(alpha=0.001)  # 0.001参数可以调整
lasso.fit(X_scaled, y_log)
FI_lasso = pd.DataFrame({"Feature Importance": lasso.coef_}, index=data_pipe.columns)

# FI_lasso.sort_values("Feature Importance",ascending=False)
FI_lasso[FI_lasso["Feature Importance"] != 0].sort_values("Feature Importance").plot(kind="barh", figsize=(15, 25))
plt.xticks(rotation=90)
plt.show()

pipe = Pipeline([
    ('labenc', labelenc()),
    ('skew_dummies', skew_dummies(skew=1)),
])

# PCA
all_pipe = pipe.fit_transform(all)
print(all_pipe.shape)  # 427

n_train = train.shape[0]
X = all_pipe[:n_train]  # 把训练集和测试集分开了
test_X = all_pipe[n_train:]
y = train.SalePrice
X_scaled = scaler.fit(X).transform(X)
test_X_scaled = scaler.transform(test_X)

pca = PCA(n_components=300)  # 300这个参数调整****
X_scaled = pca.fit_transform(X_scaled)
test_X_scaled = pca.transform(test_X_scaled)
print(X_scaled.shape, test_X_scaled.shape)


# 交叉验证函数
def rmse_cv(model, X, y):  # 这个函数之后没用到
    rmse = np.sqrt(-cross_val_score(model, X, y, scoring="neg_mean_squared_error", cv=5))
    return rmse


'''
X_scaled,y 来训练模型
test_X_scaled 套用模型，最终得到提交结果
'''

n_train = X_scaled.shape[0]
train_features = nd.array(X_scaled)
test_features = nd.array(test_X_scaled)
train_labels = nd.array(y).reshape((-1, 1))

'''
----------以上数据预处理完毕了----------
'''
'''
----------模型训练----------
'''

'''
13个模型，5折交叉检验
模型包括

LinearRegression
Ridge
Lasso
Random Forrest
Gradient Boosting Tree
Support Vector Regression
Linear Support Vector Regression
ElasticNet
Stochastic Gradient Descent
BayesianRidge
KernelRidge
ExtraTreesRegressor
XgBoost
'''

models = [LinearRegression(), Ridge(), Lasso(alpha=0.01, max_iter=10000), RandomForestRegressor(),
          GradientBoostingRegressor(), SVR(), LinearSVR(),
          ElasticNet(alpha=0.001, max_iter=10000), SGDRegressor(max_iter=1000, tol=1e-3), BayesianRidge(),
          KernelRidge(alpha=0.6, kernel='polynomial', degree=2, coef0=2.5),
          ExtraTreesRegressor(), XGBRegressor()]

names = ["LR", "Ridge", "Lasso", "RF", "GBR", "SVR", "LinSVR", "Ela", "SGD", "Bay", "Ker", "Extra", "Xgb"]
for name, model in zip(names, models):
    score = rmse_cv(model, X_scaled, y_log)
    print("{}: {:.6f}, {:.4f}".format(name, score.mean(), score.std()))


class grid():
    def __init__(self, model):
        self.model = model

    def grid_get(self, X, y, param_grid):
        grid_search = GridSearchCV(self.model, param_grid, cv=5, scoring="neg_mean_squared_error")
        grid_search.fit(X, y)
        print(grid_search.best_params_, np.sqrt(-grid_search.best_score_))
        grid_search.cv_results_['mean_test_score'] = np.sqrt(-grid_search.cv_results_['mean_test_score'])
        print(pd.DataFrame(grid_search.cv_results_)[['params', 'mean_test_score', 'std_test_score']])


# Lasso


grid(Lasso()).grid_get(X_scaled, y_log,
                       {'alpha': [0.0004, 0.0005, 0.0007, 0.0006, 0.0009, 0.0008], 'max_iter': [10000]})

# Ridge

grid(Ridge()).grid_get(X_scaled, y_log, {'alpha': [35, 40, 45, 50, 55, 60, 65, 70, 80, 90]})

# SVR

grid(SVR()).grid_get(X_scaled, y_log, {'C': [11, 12, 13, 14, 15], 'kernel': ["rbf"], "gamma": [0.0003, 0.0004],
                                       "epsilon": [0.008, 0.009]})

# Kernel Ridge

param_grid = {'alpha': [0.2, 0.3, 0.4, 0.5], 'kernel': ["polynomial"], 'degree': [3], 'coef0': [0.8, 1, 1.2]}
grid(KernelRidge()).grid_get(X_scaled, y_log, param_grid)

# ElasticNet

grid(ElasticNet()).grid_get(X_scaled, y_log,
                            {'alpha': [0.0005, 0.0008, 0.004, 0.005], 'l1_ratio': [0.08, 0.1, 0.3, 0.5, 0.7],
                             'max_iter': [10000]})


# 集成方法

# 加权平均


class AverageWeight(BaseEstimator, RegressorMixin):
    def __init__(self, mod, weight):
        self.mod = mod
        self.weight = weight

    def fit(self, X, y):
        self.models_ = [clone(x) for x in self.mod]
        for model in self.models_:
            model.fit(X, y)
        return self

    def predict(self, X):
        w = list()
        pred = np.array([model.predict(X) for model in self.models_])
        # for every data point, single model prediction times weight, then add them together
        for data in range(pred.shape[1]):
            single = [pred[model, data] * weight for model, weight in zip(range(pred.shape[0]), self.weight)]
            w.append(np.sum(single))
        return w


lasso = Lasso(alpha=0.0005, max_iter=10000)
ridge = Ridge(alpha=60)
svr = SVR(gamma=0.0004, kernel='rbf', C=13, epsilon=0.009)
ker = KernelRidge(alpha=0.2, kernel='polynomial', degree=3, coef0=0.8)
ela = ElasticNet(alpha=0.005, l1_ratio=0.08, max_iter=10000)
bay = BayesianRidge()

w1 = 0.02
w2 = 0.2
w3 = 0.25
w4 = 0.3
w5 = 0.03
w6 = 0.2

weight_avg = AverageWeight(mod=[lasso, ridge, svr, ker, ela, bay], weight=[w1, w2, w3, w4, w5, w6])

rmse_cv(weight_avg, X_scaled, y_log), rmse_cv(weight_avg, X_scaled, y_log).mean()

weight_avg = AverageWeight(mod=[svr, ker], weight=[0.5, 0.5])

rmse_cv(weight_avg, X_scaled, y_log), rmse_cv(weight_avg, X_scaled, y_log).mean()


# Stacking
class stacking(BaseEstimator, RegressorMixin, TransformerMixin):
    def __init__(self, mod, meta_model):
        self.mod = mod
        self.meta_model = meta_model
        self.kf = KFold(n_splits=5, random_state=42, shuffle=True)

    def fit(self, X, y):
        self.saved_model = [list() for i in self.mod]
        oof_train = np.zeros((X.shape[0], len(self.mod)))

        for i, model in enumerate(self.mod):
            for train_index, val_index in self.kf.split(X, y):
                renew_model = clone(model)
                renew_model.fit(X[train_index], y[train_index])
                self.saved_model[i].append(renew_model)
                oof_train[val_index, i] = renew_model.predict(X[val_index])

        self.meta_model.fit(oof_train, y)
        return self

    def predict(self, X):
        whole_test = np.column_stack([np.column_stack(model.predict(X) for model in single_model).mean(axis=1)
                                      for single_model in self.saved_model])
        return self.meta_model.predict(whole_test)

    def get_oof(self, X, y, test_X):
        oof = np.zeros((X.shape[0], len(self.mod)))
        test_single = np.zeros((test_X.shape[0], 5))
        test_mean = np.zeros((test_X.shape[0], len(self.mod)))
        for i, model in enumerate(self.mod):
            for j, (train_index, val_index) in enumerate(self.kf.split(X, y)):
                clone_model = clone(model)
                clone_model.fit(X[train_index], y[train_index])
                oof[val_index, i] = clone_model.predict(X[val_index])
                test_single[:, j] = clone_model.predict(test_X)
            test_mean[:, i] = test_single.mean(axis=1)
        return oof, test_mean


a = Imputer().fit_transform(X_scaled)
b = Imputer().fit_transform(y_log.values.reshape(-1, 1)).ravel()

stack_model = stacking(mod=[lasso, ridge, svr, ker, ela, bay], meta_model=ker)

print(rmse_cv(stack_model, a, b))
print(rmse_cv(stack_model, a, b).mean())

X_train_stack, X_test_stack = stack_model.get_oof(a, b, test_X_scaled)

X_train_add = np.hstack((a, X_train_stack))

X_test_add = np.hstack((test_X_scaled, X_test_stack))

print(rmse_cv(stack_model, X_train_add, b))
print(rmse_cv(stack_model, X_train_add, b).mean())

# 选择需要使用
stack_model = stacking(mod=[lasso, ridge, svr, ker, ela, bay], meta_model=ker)

stack_model.fit(a, b)

pred_train = np.exp(stack_model.predict(X_scaled))
result = pd.DataFrame({'Id': train.Id, 'SalePrice': pred_train})
result.to_csv("train_pred.csv", index=False)  # 训练集的估计

pred = np.exp(stack_model.predict(test_X_scaled))
result = pd.DataFrame({'Id': test.Id, 'SalePrice': pred})
result.to_csv("submission.csv", index=False)

# --------------------------------------------------------

diff = pred_train - y
print(diff)

n_train = X_scaled.shape[0]
train_features = nd.array(X_scaled)
test_features = nd.array(test_X_scaled)
train_labels = nd.array(diff).reshape((-1, 1))

print(train_features.shape)
print(test_features.shape)
print(train_labels.shape)

loss = gloss.L2Loss()

def get_net():
    net = nn.Sequential()
    net.add(nn.Dense(300, activation='relu'),
        nn.Dense(1))
    net.initialize()
    return net


def log_rmse(net, features, labels):
    # 将小于1的值设成1，使得取对数时数值更稳定
    clipped_preds = nd.clip(net(features), 1, float('inf'))
    rmse = nd.sqrt(2 * loss(clipped_preds, labels).mean())
    return rmse.asscalar()


def train(net, train_features, train_labels, test_features, test_labels,
          num_epochs, learning_rate, weight_decay, batch_size):
    train_ls, test_ls = [], []
    train_iter = gdata.DataLoader(gdata.ArrayDataset(
        train_features, train_labels), batch_size, shuffle=True)
    # 这里使用了Adam优化算法
    trainer = gluon.Trainer(net.collect_params(), 'adam', {
        'learning_rate': learning_rate, 'wd': weight_decay})
    for epoch in range(num_epochs):
        for X, y in train_iter:
            with autograd.record():
                l = loss(net(X), y)
            l.backward()
            trainer.step(batch_size)
        train_ls.append(log_rmse(net, train_features, train_labels))
        if test_labels is not None:
            test_ls.append(log_rmse(net, test_features, test_labels))
    return train_ls, test_ls


def get_k_fold_data(k, i, X, y):
    assert k > 1
    fold_size = X.shape[0] // k
    X_train, y_train = None, None
    for j in range(k):
        idx = slice(j * fold_size, (j + 1) * fold_size)
        X_part, y_part = X[idx, :], y[idx]
        if j == i:
            X_valid, y_valid = X_part, y_part
        elif X_train is None:
            X_train, y_train = X_part, y_part
        else:
            X_train = nd.concat(X_train, X_part, dim=0)
            y_train = nd.concat(y_train, y_part, dim=0)
    return X_train, y_train, X_valid, y_valid


def k_fold(k, X_train, y_train, num_epochs,
           learning_rate, weight_decay, batch_size):
    train_l_sum, valid_l_sum = 0, 0
    for i in range(k):
        data = get_k_fold_data(k, i, X_train, y_train)
        net = get_net()
        train_ls, valid_ls = train(net, *data, num_epochs, learning_rate,
                                   weight_decay, batch_size)
        train_l_sum += train_ls[-1]
        valid_l_sum += valid_ls[-1]
        if i == 0:
            d2l.semilogy(range(1, num_epochs + 1), train_ls, 'epochs', 'rmse',
                         range(1, num_epochs + 1), valid_ls,
                         ['train', 'valid'])
        print('fold %d, train rmse %f, valid rmse %f'
              % (i, train_ls[-1], valid_ls[-1]))
    return train_l_sum / k, valid_l_sum / k


k, num_epochs, lr, weight_decay, batch_size = 5, 100, 5, 1, 64
train_l, valid_l = k_fold(k, train_features, train_labels, num_epochs, lr, weight_decay, batch_size)
print('%d-fold validation: avg train rmse %f, avg valid rmse %f'
      % (k, train_l, valid_l))


def train_and_pred(train_features, test_features, train_labels, test_data,
                   num_epochs, lr, weight_decay, batch_size):
    net = get_net()
    train_ls, _ = train(net, train_features, train_labels, None, None,
                        num_epochs, lr, weight_decay, batch_size)
    d2l.semilogy(range(1, num_epochs + 1), train_ls, 'epochs', 'rmse')
    print('train rmse %f' % train_ls[-1])
    preds = net(test_features).asnumpy()
    test_data['SalePrice'] = pd.Series(preds.reshape(1, -1)[0])
    submission = pd.concat([test_data['Id'], test_data['SalePrice']], axis=1)
    submission.to_csv('diff_pred.csv', index=False)


train_and_pred(train_features, test_features, train_labels, test, num_epochs, lr, weight_decay, batch_size)
