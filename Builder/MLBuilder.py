# encoding: utf-8
"""
@author: fonttian
@contact: fonttian@gmail.com
@license: by-nc-sa
@file: MLBuilder.py
@time: 2020/7/31 上午10:47
"""

from Tools import work_path
from Tools.JSONParser import (
    config2dict,
    config2str,
    get_node_by_id,
    get_node_by_index,
    get_real_values,
    get_internal_name_values_from_parameter,
    get_id_by_index_list,
)


# 导入builder
def import_builder(json_array):
    # 定义需要导入的库
    return_list = [
        "from DataReader.PythonML import load_data_by_csv, load_data_by_pandas, download_data_by_pandas",
        "from sklearn.preprocessing import Binarizer, FunctionTransformer, KBinsDiscretizer, KernelCenterer, LabelBinarizer, LabelEncoder, MultiLabelBinarizer, MinMaxScaler, MaxAbsScaler, QuantileTransformer, Normalizer, OneHotEncoder, OrdinalEncoder, PowerTransformer, RobustScaler, StandardScaler, add_dummy_feature, PolynomialFeatures, binarize, normalize, scale, robust_scale, maxabs_scale, minmax_scale, label_binarize, quantile_transform, power_transform",
        "from sklearn.model_selection import BaseCrossValidator, GridSearchCV, TimeSeriesSplit, KFold, GroupKFold, GroupShuffleSplit, LeaveOneGroupOut, LeaveOneOut, LeavePGroupsOut, LeavePOut, RepeatedKFold, RepeatedStratifiedKFold, ParameterGrid, ParameterSampler, PredefinedSplit, RandomizedSearchCV, ShuffleSplit, StratifiedKFold, StratifiedShuffleSplit, check_cv, cross_val_predict, cross_val_score, cross_validate, fit_grid_point, learning_curve, permutation_test_score, train_test_split, validation_curve",
        "from sklearn.cluster import AffinityPropagation, AgglomerativeClustering, Birch, DBSCAN, OPTICS, cluster_optics_dbscan, cluster_optics_xi, compute_optics_graph, KMeans, FeatureAgglomeration, MeanShift, MiniBatchKMeans, SpectralClustering, affinity_propagation, dbscan, estimate_bandwidth, get_bin_seeds, k_means, linkage_tree, mean_shift, spectral_clustering, ward_tree, SpectralBiclustering, SpectralCoclustering",
        "from sklearn.random_projection import GaussianRandomProjection",
        "from sklearn.datasets import clear_data_home, dump_svmlight_file, fetch_20newsgroups, fetch_20newsgroups_vectorized, fetch_lfw_pairs, fetch_lfw_people, fetch_olivetti_faces, fetch_species_distributions, fetch_california_housing, fetch_covtype, fetch_rcv1, fetch_kddcup99, fetch_openml, get_data_home, load_boston, load_diabetes, load_digits, load_files, load_iris, load_breast_cancer, load_linnerud, load_sample_image, load_sample_images, load_svmlight_file, load_svmlight_files, load_wine, make_biclusters, make_blobs, make_circles, make_classification, make_checkerboard, make_friedman1, make_friedman2, make_friedman3, make_gaussian_quantiles, make_hastie_10_2, make_low_rank_matrix, make_moons, make_multilabel_classification, make_regression, make_s_curve, make_sparse_coded_signal, make_sparse_spd_matrix, make_sparse_uncorrelated, make_spd_matrix, make_swiss_roll",
        "from sklearn.tree import BaseDecisionTree, DecisionTreeClassifier, DecisionTreeRegressor, ExtraTreeClassifier, ExtraTreeRegressor, export_graphviz, plot_tree, export_text",
        "from sklearn.decomposition import DictionaryLearning, FastICA, IncrementalPCA, KernelPCA, MiniBatchDictionaryLearning, MiniBatchSparsePCA, NMF, PCA, SparseCoder, SparsePCA, dict_learning, dict_learning_online, fastica, non_negative_factorization, randomized_svd, sparse_encode, FactorAnalysis, TruncatedSVD, LatentDirichletAllocation",
        "from sklearn.linear_model import ARDRegression, BayesianRidge, ElasticNet, ElasticNetCV, Hinge, Huber, HuberRegressor, Lars, LarsCV, Lasso, LassoCV, LassoLars, LassoLarsCV, LassoLarsIC, LinearRegression, Log, LogisticRegression, LogisticRegressionCV, ModifiedHuber, MultiTaskElasticNet, MultiTaskElasticNetCV, MultiTaskLasso, MultiTaskLassoCV, OrthogonalMatchingPursuit, OrthogonalMatchingPursuitCV, PassiveAggressiveClassifier, PassiveAggressiveRegressor, Perceptron, Ridge, RidgeCV, RidgeClassifier, RidgeClassifierCV, SGDClassifier, SGDRegressor, SquaredLoss, TheilSenRegressor, enet_path, lars_path, lars_path_gram, lasso_path, orthogonal_mp, orthogonal_mp_gram, ridge_regression, RANSACRegressor, PoissonRegressor, GammaRegressor, TweedieRegressor",
        "from sklearn.naive_bayes import BernoulliNB, GaussianNB, MultinomialNB, ComplementNB, CategoricalNB",
        "from sklearn.ensemble import BaseEnsemble, RandomForestClassifier, RandomForestRegressor, RandomTreesEmbedding, ExtraTreesClassifier, ExtraTreesRegressor, BaggingClassifier, BaggingRegressor, IsolationForest, GradientBoostingClassifier, GradientBoostingRegressor, AdaBoostClassifier, AdaBoostRegressor, VotingClassifier, VotingRegressor, StackingClassifier, StackingRegressor",
        "from sklearn.gaussian_process import GaussianProcessRegressor, GaussianProcessClassifier, kernels",
        "from sklearn.discriminant_analysis import LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis",
        "from sklearn.neighbors import BallTree, DistanceMetric, KDTree, KNeighborsClassifier, KNeighborsRegressor, KNeighborsTransformer, NearestCentroid, NearestNeighbors, RadiusNeighborsClassifier, RadiusNeighborsRegressor, RadiusNeighborsTransformer, kneighbors_graph, radius_neighbors_graph, KernelDensity, LocalOutlierFactor, NeighborhoodComponentsAnalysis, VALID_METRICS, VALID_METRICS_SPARSE",
        "from sklearn.svm import LinearSVC, LinearSVR, NuSVC, NuSVR, OneClassSVM, SVC, SVR, l1_min_c",
        "from sklearn.neural_network import BernoulliRBM, MLPClassifier, MLPRegressor",
        "from sklearn.pipeline import Pipeline",
        "from sklearn.pipeline import FeatureUnion",
        "from sklearn.pipeline import make_pipeline",
        "from sklearn.pipeline import make_union",
        "from sklearn.metrics import accuracy_score, adjusted_mutual_info_score, adjusted_rand_score, auc, average_precision_score, balanced_accuracy_score, calinski_harabasz_score, check_scoring, classification_report, cluster, cohen_kappa_score, completeness_score, ConfusionMatrixDisplay, confusion_matrix, consensus_score, coverage_error, dcg_score, davies_bouldin_score, euclidean_distances, explained_variance_score, f1_score, fbeta_score, fowlkes_mallows_score, get_scorer, hamming_loss, hinge_loss, homogeneity_completeness_v_measure, homogeneity_score, jaccard_score, label_ranking_average_precision_score, label_ranking_loss, log_loss, make_scorer, nan_euclidean_distances, matthews_corrcoef, max_error, mean_absolute_error, mean_squared_error, mean_squared_log_error, mean_poisson_deviance, mean_gamma_deviance, mean_tweedie_deviance, median_absolute_error, multilabel_confusion_matrix, mutual_info_score, ndcg_score, normalized_mutual_info_score, pairwise_distances, pairwise_distances_argmin, pairwise_distances_argmin_min, pairwise_distances_chunked, pairwise_kernels, plot_confusion_matrix, plot_precision_recall_curve, plot_roc_curve, PrecisionRecallDisplay, precision_recall_curve, precision_recall_fscore_support, precision_score, r2_score, recall_score, RocCurveDisplay, roc_auc_score, roc_curve, SCORERS, silhouette_samples, silhouette_score, v_measure_score, zero_one_loss, brier_score_loss",
        "from xgboost import DMatrix, DeviceQuantileDMatrix, Booster, train, cv, RabitTracker, XGBModel, XGBClassifier, XGBRegressor, XGBRanker, XGBRFClassifier, XGBRFRegressor, plot_importance, plot_tree, to_graphviz, dask",
        "from lightgbm import Dataset, Booster, CVBooster, train, cv, LGBMModel, LGBMRegressor, LGBMClassifier, LGBMRanker, print_evaluation, record_evaluation, reset_parameter, early_stopping, plot_importance, plot_split_value_histogram, plot_metric, plot_tree, create_tree_digraph",
        "import joblib",
        "from sklearn.feature_selection import GenericUnivariateSelect, RFE, RFECV, SelectFdr, SelectFpr, SelectFwe, SelectKBest, SelectFromModel, SelectPercentile, VarianceThreshold, chi2, f_classif, f_oneway, f_regression, mutual_info_classif, mutual_info_regression, SelectorMixin",
        "import pandas as pd",
        "import numpy as np",
    ]

    # return_list.extend(redis_client(get_node_by_id(json_array, "0")))

    return return_list


# 数据读取builder
def data_reader_builder(data_reader_node, return_type=1):
    # 根据return_type返回不同类型的数据读取代码
    if return_type == 1:
        if data_reader_node["internal_name"] == "datasets":
            return "data, target = " + get_real_values(data_reader_node["parameter"][0]["values"]).replace("\"", "") + "(return_X_y=True)"
        else:
            return (
                    "data, target = "
                    + data_reader_node["internal_name"]
                    + "("
                    + config2str(data_reader_node)
                    + ")"
            )
    if return_type == 2:
        return (
                "train_data, train_target = "
                + data_reader_node["internal_name"]
                + "("
                + config2str(data_reader_node)
                + ")"
        )
    if return_type == 3:
        return (
                "test_data, test_target = "
                + data_reader_node["internal_name"]
                + "("
                + config2str(data_reader_node)
                + ")"
        )


# 起始节点builder
def starting_node_builder(data_loader_node, json_array):
    # 根据data_loader_node的internal_name返回不同类型的数据读取代码
    return_list = []
    tmp_dict = config2dict(data_loader_node)
    if data_loader_node["internal_name"] == "train_and_test":
        return_list.append(data_reader_builder(get_node_by_index(json_array, 1)))
        return_list.append(data_reader_builder(tmp_dict["train_data"], 2))
        return_list.append(data_reader_builder(tmp_dict["test_data"], 3))
    if data_loader_node["internal_name"] == "train_test_split":
        return_list.append(data_reader_builder(get_node_by_index(json_array, 1)))
        return_list.append(
            ("train_data, test_data, train_target, test_target = train_test_split(data, "
             "target, test_size={test_size}, random_state={random_state})").format_map(
                tmp_dict
            )
        )

    return return_list


# pipeline节点builder
def pipeline_node_builder(pipeline_node, is_tuple=False):
    params_str = config2str(pipeline_node)

    # 修 LinearRegression 参数名
    if pipeline_node["internal_name"] == "LinearRegression":
        params_str = params_str.replace("copy=", "copy_X=")

    if is_tuple:
        return (
            '("'
            + pipeline_node["internal_name"]
            + "_"
            + pipeline_node["connection"]["id"]
            + '",'
            + pipeline_node["internal_name"]
            + "("
            + params_str
            + "))"
        )
    else:
        return pipeline_node["internal_name"] + "(" + params_str + ")"


# pipeline builder
def pipeline_builder(json_array, id_list, pipeline_name=None):
    # 根据id_list生成pipeline代码
    return_str = pipeline_name + "=Pipeline(["
    for item in id_list:
        return_str += (
                pipeline_node_builder(
                    get_node_by_id(
                        json_array,
                        item),
                    is_tuple=True) +
                ",")
    return return_str + "])"


# metrics节点builder
def metrics_node_builder(metrics_node, model_name):
    return_list = [
        "score_train = " + model_name + ".score(train_data, train_target)",
        "score_test = " + model_name + ".score(test_data, test_target)",
        "prediction = " + model_name + ".predict(test_data)",
        'print("score_train =", score_train)',
        'print("score_test =", score_test)',
    ]

    return_list_metrics = ["score_train", "score_test"]

    str_list = get_real_values(
        get_internal_name_values_from_parameter(metrics_node["parameter"], "methods")
    ).replace("[", "").replace("]", "").replace("\"", "").split(",")

    metrics_code_list, metrics_list = generate_metrics_code(str_list)
    return_list.extend(metrics_code_list)
    return_list_metrics.extend(metrics_list)

    return return_list, return_list_metrics


def generate_metrics_code(str_list):
    return_list = []
    return_list_metrics = []

    for item in str_list:
        metrics_name = item
        return_list_metrics.append(metrics_name)

        return_list.extend([
            "try:",
            f"    score_test_{metrics_name} = {item}(test_target, prediction)",
            "except Exception as e:",
            f"    score_test_{metrics_name} = None",
            f"    print('skip metric {metrics_name}:', e)",
        ])

    return return_list, return_list_metrics


# 保存节点builder
def save_node_builder(save_node, model_name):
    """
    根据 save_node 生成模型保存代码。

    参数:
    save_node (dict): 保存节点信息。
    model_name (str): 模型名称。

    返回:
    list: 生成的模型保存代码。
    """
    methods_values = get_internal_name_values_from_parameter(save_node["parameter"], "methods")
    real_values = get_real_values(methods_values)
    
    if real_values == '"joblib"' or real_values == 'joblib':
        return [generate_joblib_save_code(model_name)]
    else:
        print("Error: get_real_values(methods_values) != 'joblib'")
        print(f"get_real_values(methods_values): {real_values}")
        return []


def generate_joblib_save_code(model_name):
    """
    生成 joblib 保存模型的代码。

    参数:
    model_name (str): 模型名称。

    返回:
    str: 生成的 joblib 保存模型代码。
    """
    return f'joblib.dump({model_name}, "{str(work_path + model_name).replace("//", "/")}.pkl")'


# pipeline builder all
def pipeline_builder_all(json_array, id_list_all):
    # pipeline_builder_all = pipeline_model + 评估评估 + 模型保存
    # pipeline_model = 特征处理 + 特征选择 + 学习器

    # 生成pipeline_model代码
    model_name = "pipeline_model"
    return_list = [
        pipeline_builder(
            json_array,
            get_id_by_index_list(json_array, ["3", "4"]),
            model_name,
        ),
        model_name + ".fit(train_data, train_target)",
    ]

    # 生成模型评估代码
    for item in id_list_all:
        node = get_node_by_id(json_array, item)
        if node["connection"]["index"] == "5":
            metrics_code_list, metrics_list = metrics_node_builder(
                node, model_name)
            # metrics_code_list.extend(metrics_list)
            # 监控问题需要再设计运行时存储方案
            # metrics_hset(
            #     redis_hashmap_name,
            #     metrics_list)
            return_list.extend(metrics_code_list)

    # 生成模型保存代码
    for item in id_list_all:
        node = get_node_by_id(json_array, item)
        if node["connection"]["index"] == "6":
            return_list.extend(save_node_builder(node, model_name))

    return return_list
