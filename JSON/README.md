# json字段解释
json一共分类三个基本级别,核心单位为Object,模块.为了渲染结果便于展示,它的上级还有ModuleGroup.
Module是为了便于前台展示存在的,当一个Module下存在较多Object时,也会使用更多的Module对
Object进行分组.

## 具体解释如下:
 - external_name: 外部名称,通用字段,用于前台展示.
 - internal_name：内部名称,返回后台使用的名字
 - description: 描述,通用字段.该模块的文字描述和说明
 - type: 通用字段,用于区分Object、Module、hyperparameter
 - spec:空间,Module专属,包含下一级模块
   - ~~name: 名字,通用字段,用于前台展示.~~
   - external_name:外部名称,通用字段,用于前台展示.
   - internal_name:内部名称,返回后台使用的名字
   - type: 通用字段,用于区分Object、Module、hyperparameter
   - description: 通用字段,用于区分Object与Module
   - ~~func: Object专属,部分Module也有,对应该Object对应的实际函数或者Module所对应的类库中的模块名~~
   - connection:Object专属,与连接有关的参数
       - index:Object专属,用于标识该Object所属整个机器学习流水线的序列
       - id: Object的ID,唯一标识
       - following:专属字段,该模块可以向上连接的模块的index
       - followers:专属字段,该模块可以向下连接的模块的index
   - ~~config:Object专属,包含超参数~~
   - parameter:Object专属,包含超参数
     - ~~hyperparameter:专属字段,超参数的名字~~
     - external_name:外部名称,通用字段,用于前台展示.
     - internal_name:内部名称,返回后台使用的名字
     - ~~class_name:专属字段,超参数的数据类型~~
     - input_type:专属字段,超参数的数据类型
     - description:描述,通用字段.该超参数的文字描述和说明
     - values:专属字段,当class_name为选择时,用于选择的数组
     - default:默认参数,专属字段
     - conditions:专属字段,用于判断输入类型.为空表示不作任何判断
     
## 具体字段解释
## 数组类values含义解释
## following 与 followers

~~该模块可以连接的模块~~
 - ~~starting_node: 表示该节点为起始节点~~
 - ~~end_node: 表示该节点为终止节点~~
 - ~~superior: 上级~~
 - ~~same_level: 同级~~
 - ~~subordinate: 下级~~
 - ~~no_node: 不可连接~~

根据数字判断，比如数字为3 ，表示可以向上或者向下连接index为3的Object。
特殊字符 no_node 表示 没有连接
特殊字符 starting_node 表示 该节点为开始节点

### class_name
 - user_filepath:用户路径
 - single_choice:单项选择
 - single_choice_object:单项选择，但是选择的对象为object
 - multiple_choice:多项选择
 - boolean:布尔
 - int:int类型,整型
 - float:浮点数
 - scientific-notation: 科学计数法
 - str:字符串
 - None:Python中的None
 - estimator:学习器或者估计器,这里指的是机器学习模型
 - callable: 可调用,
 - object:输入应为类的ID,声明独立类,并将独立类的ID传入.所有的object皆为必选项.
 - dict:字典
 - ~~estimator:学习器或者说估计器，也就是直接拖拽左侧的类~~
 - ~~estimator_list:类列表，也就是直接拖拽左侧的类（可多个）~~
 - url:网络链接
 
### conditions

conditions是输入数据的判断依据,当参数不需要输入,只需要选择时,无需管理该部分,否则需要调用该部分中的限制条件进行检测.
 
 - int:int数据类型
 - float:浮点数
 - positive-float:正浮点数
 - negative-float:负浮点数
 - non-positive-float:非正浮点数
 - non-negative-float:非负浮点数
 - integer: 整数
 - non-one: 不等于一
 - non-negative: 非负
 - non-positive: 非正
 - percentage: 百分比(实际指数字在0和1之间)
 - over-half-percentage: 过半百分比(实际指数字在0.5和1之间)
 - negative: 负数
 - positive: 正数
 - positive-integer: 正整数
 - negative-integer: 负整数
 - non-positive-integer: 非正整数
 - non-negative-integer: 非负整数
 - tuple: 元组
 - required:必选
 - range@[0,1]
- ~~index@n:estimator_list或者estimator的限制条件，n表示index~~
- ~~id@n:estimator_list或者estimator的限制条件，n表示id~~

## 算法中的特殊参数
### Real world datasets 与 Toy datasets

自带默认参数`return_X_y=True`

### XGB
XGBRegressor与XGBClassifier中的参数:(1)eval_metric;(2)early_stopping_rounds;他们都是训练(fit方法)参数,而非构建时传入的参数
### LGBM
LGBMClassifier与LGBMRegressor中的参数：(1)early_stopping_rounds;该参数是训练(fit方法)参数,而非构建时传入的参数

### .1 老版本注释

老版本注释，包含"data_applications.json" , "data_automl.json"  ,"data_keras.json"三个文件

| 汉语|    英文    |代码|
|  ----  | ----  | ----  |
| 正整数 |   Positive integer   | PositiveInteger|
|正数  |  Positive number   | PositiveFloat|
|整数 |Integer |Integer|
|正浮点数|     positive float    |PositiveFloat|
|非负数|    Non-negative   | Non-negative|
|非正数|    Non-positive  |  Non-positive|
|用户文件夹路径|    User folder path |UserFolderPath|
|(0,1) |   bet01  |  between 0 and 1.|
|任意 |   Arbitrary    |Arbitrary|
|元组 |   tuple  | tuple|
|整数元组| Integer tuple|IntegerTuple|
|两个整数组成的整数元组 |Integer tuple| IntegerTuple2|
|三个整数组成的整数元组 |Integer tuple| IntegerTuple3|