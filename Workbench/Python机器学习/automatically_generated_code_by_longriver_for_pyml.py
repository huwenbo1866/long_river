# encoding: utf-8 
from DataReader.PythonML import load_data_by_csv, load_data_by_pandas, download_data_by_pandas
from sklearn.preprocessing import Binarizer, FunctionTransformer, KBinsDiscretizer, KernelCenterer, LabelBinarizer, LabelEncoder, MultiLabelBinarizer, MinMaxScaler, MaxAbsScaler, QuantileTransformer, Normalizer, OneHotEncoder, OrdinalEncoder, PowerTransformer, RobustScaler, StandardScaler, add_dummy_feature, PolynomialFeatures, binarize, normalize, scale, robust_scale, maxabs_scale, minmax_scale, label_binarize, quantile_transform, power_transform
from sklearn.model_selection import BaseCrossValidator, GridSearchCV, TimeSeriesSplit, KFold, GroupKFold, GroupShuffleSplit, LeaveOneGroupOut, LeaveOneOut, LeavePGroupsOut, LeavePOut, RepeatedKFold, RepeatedStratifiedKFold, ParameterGrid, ParameterSampler, PredefinedSplit, RandomizedSearchCV, ShuffleSplit, StratifiedKFold, StratifiedShuffleSplit, check_cv, cross_val_predict, cross_val_score, cross_validate, fit_grid_point, learning_curve, permutation_test_score, train_test_split, validation_curve
from sklearn.cluster import AffinityPropagation, AgglomerativeClustering, Birch, DBSCAN, OPTICS, cluster_optics_dbscan, cluster_optics_xi, compute_optics_graph, KMeans, FeatureAgglomeration, MeanShift, MiniBatchKMeans, SpectralClustering, affinity_propagation, dbscan, estimate_bandwidth, get_bin_seeds, k_means, linkage_tree, mean_shift, spectral_clustering, ward_tree, SpectralBiclustering, SpectralCoclustering
from sklearn.random_projection import GaussianRandomProjection
from sklearn.datasets import clear_data_home, dump_svmlight_file, fetch_20newsgroups, fetch_20newsgroups_vectorized, fetch_lfw_pairs, fetch_lfw_people, fetch_olivetti_faces, fetch_species_distributions, fetch_california_housing, fetch_covtype, fetch_rcv1, fetch_kddcup99, fetch_openml, get_data_home, load_boston, load_diabetes, load_digits, load_files, load_iris, load_breast_cancer, load_linnerud, load_sample_image, load_sample_images, load_svmlight_file, load_svmlight_files, load_wine, make_biclusters, make_blobs, make_circles, make_classification, make_checkerboard, make_friedman1, make_friedman2, make_friedman3, make_gaussian_quantiles, make_hastie_10_2, make_low_rank_matrix, make_moons, make_multilabel_classification, make_regression, make_s_curve, make_sparse_coded_signal, make_sparse_spd_matrix, make_sparse_uncorrelated, make_spd_matrix, make_swiss_roll
from sklearn.tree import BaseDecisionTree, DecisionTreeClassifier, DecisionTreeRegressor, ExtraTreeClassifier, ExtraTreeRegressor, export_graphviz, plot_tree, export_text
from sklearn.decomposition import DictionaryLearning, FastICA, IncrementalPCA, KernelPCA, MiniBatchDictionaryLearning, MiniBatchSparsePCA, NMF, PCA, SparseCoder, SparsePCA, dict_learning, dict_learning_online, fastica, non_negative_factorization, randomized_svd, sparse_encode, FactorAnalysis, TruncatedSVD, LatentDirichletAllocation
from sklearn.linear_model import ARDRegression, BayesianRidge, ElasticNet, ElasticNetCV, Hinge, Huber, HuberRegressor, Lars, LarsCV, Lasso, LassoCV, LassoLars, LassoLarsCV, LassoLarsIC, LinearRegression, Log, LogisticRegression, LogisticRegressionCV, ModifiedHuber, MultiTaskElasticNet, MultiTaskElasticNetCV, MultiTaskLasso, MultiTaskLassoCV, OrthogonalMatchingPursuit, OrthogonalMatchingPursuitCV, PassiveAggressiveClassifier, PassiveAggressiveRegressor, Perceptron, Ridge, RidgeCV, RidgeClassifier, RidgeClassifierCV, SGDClassifier, SGDRegressor, SquaredLoss, TheilSenRegressor, enet_path, lars_path, lars_path_gram, lasso_path, orthogonal_mp, orthogonal_mp_gram, ridge_regression, RANSACRegressor, PoissonRegressor, GammaRegressor, TweedieRegressor
from sklearn.naive_bayes import BernoulliNB, GaussianNB, MultinomialNB, ComplementNB, CategoricalNB
from sklearn.ensemble import BaseEnsemble, RandomForestClassifier, RandomForestRegressor, RandomTreesEmbedding, ExtraTreesClassifier, ExtraTreesRegressor, BaggingClassifier, BaggingRegressor, IsolationForest, GradientBoostingClassifier, GradientBoostingRegressor, AdaBoostClassifier, AdaBoostRegressor, VotingClassifier, VotingRegressor, StackingClassifier, StackingRegressor
from sklearn.gaussian_process import GaussianProcessRegressor, GaussianProcessClassifier, kernels
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis
from sklearn.neighbors import BallTree, DistanceMetric, KDTree, KNeighborsClassifier, KNeighborsRegressor, KNeighborsTransformer, NearestCentroid, NearestNeighbors, RadiusNeighborsClassifier, RadiusNeighborsRegressor, RadiusNeighborsTransformer, kneighbors_graph, radius_neighbors_graph, KernelDensity, LocalOutlierFactor, NeighborhoodComponentsAnalysis, VALID_METRICS, VALID_METRICS_SPARSE
from sklearn.svm import LinearSVC, LinearSVR, NuSVC, NuSVR, OneClassSVM, SVC, SVR, l1_min_c
from sklearn.neural_network import BernoulliRBM, MLPClassifier, MLPRegressor
from sklearn.pipeline import Pipeline
from sklearn.pipeline import FeatureUnion
from sklearn.pipeline import make_pipeline
from sklearn.pipeline import make_union
from sklearn.metrics import accuracy_score, adjusted_mutual_info_score, adjusted_rand_score, auc, average_precision_score, balanced_accuracy_score, calinski_harabasz_score, check_scoring, classification_report, cluster, cohen_kappa_score, completeness_score, ConfusionMatrixDisplay, confusion_matrix, consensus_score, coverage_error, dcg_score, davies_bouldin_score, euclidean_distances, explained_variance_score, f1_score, fbeta_score, fowlkes_mallows_score, get_scorer, hamming_loss, hinge_loss, homogeneity_completeness_v_measure, homogeneity_score, jaccard_score, label_ranking_average_precision_score, label_ranking_loss, log_loss, make_scorer, nan_euclidean_distances, matthews_corrcoef, max_error, mean_absolute_error, mean_squared_error, mean_squared_log_error, mean_poisson_deviance, mean_gamma_deviance, mean_tweedie_deviance, median_absolute_error, multilabel_confusion_matrix, mutual_info_score, ndcg_score, normalized_mutual_info_score, pairwise_distances, pairwise_distances_argmin, pairwise_distances_argmin_min, pairwise_distances_chunked, pairwise_kernels, plot_confusion_matrix, plot_precision_recall_curve, plot_roc_curve, PrecisionRecallDisplay, precision_recall_curve, precision_recall_fscore_support, precision_score, r2_score, recall_score, RocCurveDisplay, roc_auc_score, roc_curve, SCORERS, silhouette_samples, silhouette_score, v_measure_score, zero_one_loss, brier_score_loss
from xgboost import DMatrix, DeviceQuantileDMatrix, Booster, train, cv, RabitTracker, XGBModel, XGBClassifier, XGBRegressor, XGBRanker, XGBRFClassifier, XGBRFRegressor, plot_importance, plot_tree, to_graphviz, dask
from lightgbm import Dataset, Booster, CVBooster, train, cv, LGBMModel, LGBMRegressor, LGBMClassifier, LGBMRanker, print_evaluation, record_evaluation, reset_parameter, early_stopping, plot_importance, plot_split_value_histogram, plot_metric, plot_tree, create_tree_digraph
import joblib
from sklearn.feature_selection import GenericUnivariateSelect, RFE, RFECV, SelectFdr, SelectFpr, SelectFwe, SelectKBest, SelectFromModel, SelectPercentile, VarianceThreshold, chi2, f_classif, f_oneway, f_regression, mutual_info_classif, mutual_info_regression, SelectorMixin
import pandas as pd
import numpy as np

data, target = load_boston(return_X_y=True)
train_data, test_data, train_target, test_target = train_test_split(data, target, test_size=None, random_state=None)
pipeline_model=Pipeline([("StandardScaler_3",StandardScaler(copy=True, with_mean=True, with_std=True, )),("LinearRegression_4",LinearRegression(fit_intercept=True, normalize=False, copy_X=True, n_jobs=None, )),])
pipeline_model.fit(train_data, train_target)
score_train = pipeline_model.score(train_data, train_target)
score_test = pipeline_model.score(test_data, test_target)
prediction = pipeline_model.predict(test_data)
score_test_accuracy_score = accuracy_score(test_target, prediction)
score_test_accuracy_score = None
score_test_jaccard_score = jaccard_score(test_target, prediction)
score_test_jaccard_score = None
score_test_log_loss = log_loss(test_target, prediction)
score_test_log_loss = None
joblib.dump(pipeline_model, "./pipeline_model.pkl")
