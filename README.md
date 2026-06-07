# DataScience_NareshIt

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-orange?logo=jupyter)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-green)
![Deep Learning](https://img.shields.io/badge/Deep%20Learning-TensorFlow%20%7C%20PyTorch-red)
![MLOps](https://img.shields.io/badge/MLOps-MLflow-purple)
![Apps](https://img.shields.io/badge/Apps-Streamlit%20%7C%20Flask%20%7C%20Tkinter-lightgrey)

## 📌 Project Overview

`DataScience_NareshIt` is a comprehensive Data Science learning, practice, and portfolio repository. It combines course-style notebooks, task solutions, interview preparation, machine learning experiments, deep learning practice, SQL work, NLP, computer vision, MLOps, and small deployable UI applications.

The repository is best understood as a full learning path rather than a single production project. It starts with Python fundamentals, moves through statistics and data analysis libraries, then progresses into classical machine learning, deep learning, NLP, computer vision, SQL, MLOps, and end-to-end mini projects. For recruiters, it demonstrates practical breadth: coding foundations, data preparation, visualization, modeling, evaluation, experiment tracking, and simple application deployment.

### What This Repository Demonstrates

- Strong Python programming foundations with notebooks and scripts.
- Practical data analysis using NumPy, Pandas, Matplotlib, Seaborn, Plotly, and OpenCV.
- Statistical thinking, probability, sampling, confidence intervals, and hypothesis testing.
- Classical ML algorithms for regression, classification, clustering, dimensionality reduction, and ensembles.
- Deep learning with TensorFlow/Keras and PyTorch, including ANN, CNN, RNN, LSTM, transfer learning, and pretrained models.
- NLP using text preprocessing, TF-IDF, Word2Vec, spaCy, NLTK, and chatbot/NLU scripts.
- MLOps basics using MLflow, model logging, artifacts, metrics, and model registration.
- UI/application practice using Streamlit, Flask, Tkinter, Gradio, and SQL connectivity.

## 🧭 Repository Highlights

| Metric | Count / Summary |
| --- | --- |
| Jupyter notebooks | 185 notebooks |
| Python scripts | 67 scripts |
| Data/model assets | 14 CSV files, 3 Excel files, 2 DB files, 6 pickle files, 3 PyTorch/YOLO weight files |
| SQL scripts | 4 SQL files |
| Major algorithm families | Regression, classification, clustering, PCA/SVD, ensembles, ANN/CNN/RNN/LSTM, NLP vectors, CV detection |
| Mini projects and apps | Bitcoin regression, churn prediction, EDA automation with LLM, color detection, student result system, web scraping, text-to-speech, dice simulator, SQL restaurant analysis, NLP utilities |

> Note: Generated folders such as virtual environments, notebook checkpoints, MLflow run folders, Gradio flags, and `node_modules` are present in the working tree but are not treated as learning modules.

## 🏗️ Repository Architecture

```text
DataScience_NareshIt/
├── Advance_Python/
│   ├── AI/
│   ├── module/
│   └── OOPs/
├── DEEPLEARNING/
│   ├── churn_modeling/
│   ├── deep_learning/
│   │   ├── back_prapogation/
│   │   └── projects/
│   ├── open-cv/
│   │   └── COLOR DETECTION PROJECT/
│   ├── open_med/
│   │   └── MEDIAPIPE-LIBRARY-main/
│   ├── pytorch/
│   ├── RNN/
│   └── yolo/
├── Machine_learning/
│   ├── Classification/
│   │   ├── classification_metrix/
│   │   ├── CLUSTERING/
│   │   ├── DecisionTree/
│   │   ├── Ensemble-Learning/
│   │   │   ├── Bagging/
│   │   │   ├── Boosting/
│   │   │   │   └── XGboost/
│   │   │   ├── Random_Forest/
│   │   │   └── Voting/
│   │   ├── knn/
│   │   ├── Logistics_regression/
│   │   ├── Naive Bayes/
│   │   ├── PCA/
│   │   └── SVM/
│   ├── Data Preprocessing/
│   ├── HyperparameterTunning/
│   └── LinearRegression/
│       └── laptop_price_predictor/
├── MLOPS/
├── MySql/
│   └── sql_data/
├── NLP/
│   └── NLP_Projects/
├── Projects/
│   └── Bitcoin_Regression/
├── Python_Basics/
│   └── PROJECTS/
│       ├── TEXTTOSPEECH/
│       └── dice_simulator/
├── Python_libraries/
│   ├── Analysis_lib/
│   │   └── EDA_INTEGRATION_LLM/
│   │       └── EDA_LLM Integration/
│   ├── opencv/
│   └── Projects/
├── statistics/
│   ├── Statistics_S/
│   └── statistics_R/
├── Task_Solutions/
│   ├── basic_python/
│   ├── pandas/
│   └── plotly/
├── UI/
│   ├── Backend/
│   └── frontend/
│       └── student_result/
├── requirements.txt
└── README.md
```

## 📂 Detailed Component Breakdown

| Component | Purpose | Topics Covered | Skills Learned | Important Files |
| --- | --- | --- | --- | --- |
| `Python_Basics/` | Python foundation module | Syntax, data types, operators, number systems, conditionals, functions, data structures | Writing clean Python notebooks and scripts | `Intro_Python.ipynb`, `DataTypes.ipynb`, `DataStructure.ipynb`, `functions.ipynb`, `Conditional_Statements.ipynb` |
| `Python_Basics/PROJECTS/` | Beginner Python projects | GUI, text-to-speech, random simulation | Turning beginner logic into small apps | `TEXTTOSPEECH/app.py`, `dice_simulator/dice.py` |
| `Advance_Python/` | Advanced language concepts | OOP, exception handling, modules, reusable code | Object-oriented thinking, modular programming, error handling | `OOP.ipynb`, `Object_Oriented _Programming_full.ipynb`, `Exception-Handing.ipynb` |
| `Advance_Python/AI/` | Introductory AI API practice | LangChain, OpenAI/Gemini-style workflows | Prompt/API experimentation and LLM integration basics | `openai_testing.ipynb`, `langchain_with_gemeni.ipynb` |
| `statistics/` | Statistics learning path | Descriptive statistics, sampling, CLT, inference, hypothesis testing | Statistical reasoning for data science interviews and model interpretation | `Statistics.ipynb`, `Sampling_CLT.ipynb`, `hypothesis.ipynb`, `stats.ipynb` |
| `Python_libraries/` | Data analysis library practice | NumPy, Pandas, Matplotlib, Seaborn, Plotly, OpenCV | Data manipulation, plotting, exploratory analysis | `Analysis_lib/Pandas.ipynb`, `Array_Numpy.ipynb`, `Seaborn.ipynb`, `matplotlib.ipynb` |
| `Python_libraries/Analysis_lib/EDA_INTEGRATION_LLM/` | EDA automation prototype | Titanic EDA, Ollama/Mistral-style LLM workflow, Gradio UI | Automated summaries, EDA reports, LLM-assisted analysis | `EDA_LLM Integration/code.ipynb`, `app.py`, `titanic_ dataset_final.csv` |
| `Task_Solutions/` | Practice and interview preparation | Python tasks, NumPy, Pandas, Matplotlib, Plotly, interview questions | Problem solving, notebook fluency, interview review | `python_interview_questions.ipynb`, `Numpy_Array.ipynb`, `pandas/Pandas.ipynb` |
| `Machine_learning/` | Classical ML curriculum | Preprocessing, regression, classification, clustering, model evaluation | Building and evaluating Scikit-Learn models | `Daily_notes.ipynb`, `Data Preprocessing/`, `LinearRegression/`, `Classification/` |
| `Machine_learning/Data Preprocessing/` | Feature engineering and preprocessing | Imputation, scaling, normalization, encoding, column transformer, Titanic preprocessing | Preparing tabular data for ML pipelines | `DataPreprocessing.ipynb`, `Column_Transformer.ipynb`, `Standardization.ipynb`, `OneHotEncoding.ipynb` |
| `Machine_learning/LinearRegression/` | Regression algorithms | Simple/multiple/polynomial regression, regularization, SVR, KNN regression, multicollinearity | Regression modeling, coefficients, residuals, model persistence | `Simple_Linear_Regression.ipynb`, `multiple_linear_regression.ipynb`, `Regularization.ipynb`, `svr_knn_syder.py` |
| `Machine_learning/Classification/` | Classification algorithms | Logistic regression, SVM, KNN, Naive Bayes, Decision Tree, PCA, metrics | Supervised classification and model evaluation | `Classification.ipynb`, algorithm subfolders |
| `Machine_learning/Classification/Ensemble-Learning/` | Ensemble methods | Bagging, Random Forest, Voting, Gradient Boosting, XGBoost | Improving model robustness and comparing ensemble strategies | `Voting_Classifier.ipynb`, `random_forest.ipynb`, `Gradient-Boosting.ipynb` |
| `Machine_learning/HyperparameterTunning/` | Model validation and tuning | Cross-validation, KNN tuning, parameter search | Avoiding overfit and selecting better model parameters | `Cross_Validation.ipynb`, `hyperparametercode.ipynb` |
| `DEEPLEARNING/` | Neural network learning path | ANN, CNN, RNN, LSTM, transfer learning, pretrained models, PyTorch, TensorFlow | Deep learning model construction and experimentation | `deeplearning-intro.ipynb`, `deep_learning/`, `pytorch/`, `open-cv/` |
| `DEEPLEARNING/deep_learning/` | TensorFlow/Keras practice | Backpropagation, dropout, batch normalization, early stopping, CNN, transfer learning | Training neural networks and diagnosing learning behavior | `backpropagation_classification.ipynb`, `cnn.ipynb`, `Transfer_Learning.ipynb` |
| `DEEPLEARNING/pytorch/` | PyTorch practice | Tensors, autograd, Dataset/DataLoader, ANN, CNN, RNN, Optuna | PyTorch training loops, GPU workflows, hyperparameter optimization | `tensor_in_pytorch.ipynb`, `training_pipeline.ipynb`, `cnn_optuna.ipynb` |
| `DEEPLEARNING/open-cv/` | Computer vision practice | Image processing, OCR, lane detection, face/eye cascades, color detection | CV preprocessing and real-time app thinking | `open-cv.ipynb`, `ocr.ipynb`, `COLOR DETECTION PROJECT/app.py` |
| `DEEPLEARNING/open_med/` | MediaPipe examples | Pose, hands, face mesh, objectron, webcam detection | Landmark detection and real-time CV pipelines | `MEDIAPIPE-LIBRARY-main/*.py` |
| `DEEPLEARNING/churn_modeling/` | Deep learning classification app | Customer churn modeling, Streamlit inference | ANN deployment-style workflow | `churn.ipynb`, `app.py` |
| `DEEPLEARNING/yolo/` | Object detection | YOLO inference on images | Object detection workflow basics | `yolo_intro.py`, YOLO weight files |
| `NLP/` | Natural language processing | Tokenization, preprocessing, POS tagging, TF-IDF, Word2Vec, spaCy | Text representation and NLP classification workflows | `NLP-INTRO.ipynb`, `text-reprentation!bow!tfidf.ipynb`, `word2vec.ipynb` |
| `NLP/NLP_Projects/` | NLP mini applications | Chatbot, language detection, translation, TTS-style utilities | Building interactive NLP utilities | `chatbot.py`, `nlu.py` |
| `MLOPS/` | ML experiment tracking | MLflow experiments, metrics, artifacts, model registry | Reproducible model training and model lifecycle basics | `1st code experiment.ipynb`, `2nd_mlflow_binaryclassification.ipynb`, `3rd_ mlflow_model_registiration.ipynb` |
| `MySql/` | SQL practice | DDL, SQLite/MySQL-style scripts, joins, restaurant project | Database querying and Python-SQL connectivity | `sql_project.sql`, `sql_practice.sql`, `restourant_sql_project.ipynb` |
| `Projects/` | Portfolio project notebooks | Web scraping, Adult UCI analysis, logistic/PCA, Bitcoin regression | Applying multiple concepts to realistic workflows | `webscrapping.ipynb`, `adult_uci.ipynb`, `Bitcoin_Regression/bitcoin.ipynb` |
| `UI/` | Frontend/backend demos | Flask, Streamlit, Tkinter, student result management | Turning Python logic into basic interfaces | `Backend/flask_ui.py`, `frontend/app1.py`, `frontend/student_result/app.py` |

## 🧪 Notebooks and Scripts Analysis

The repository contains many notebook-based lessons. The table below groups every `.ipynb` and `.py` file by directory. For each group, the objective, datasets, libraries, algorithms, inputs, outputs, and learning outcomes are summarized from the file names, imports, and referenced assets.

<details>
<summary><strong>Complete notebook and script inventory</strong></summary>

| Directory | Files Included | Objective / Dataset / Libraries / Algorithms / Outputs / Key Learnings |
| --- | --- | --- |
| `Python_Basics/` | `Intro_Python.ipynb`, `python_functionality.ipynb`, `DataTypes.ipynb`, `DataStructure.ipynb`, `Conditional_Statements.ipynb`, `functions.ipynb`, `Number system.ipynb`, `console__representation_statements.py` | Learn Python syntax, variables, control flow, functions, basic structures, and console output. Inputs are classroom examples; outputs are executed cells and console demonstrations. |
| `Python_Basics/PROJECTS/TEXTTOSPEECH/` | `app.py`, `tempCodeRunnerFile.py` | Text-to-speech GUI practice using Tkinter, NLTK, and `pyttsx3`. Input is user text; output is spoken audio behavior and GUI interaction. |
| `Python_Basics/PROJECTS/dice_simulator/` | `dice.py` | Dice simulator using Tkinter and Pillow assets `die1.png` to `die6.png`. Demonstrates random choice, GUI images, and event handling. |
| `Advance_Python/` | `OOP.ipynb`, `Object_Oriented _Programming_full.ipynb`, `Exception-Handing.ipynb` | Advanced Python practice: classes, inheritance, encapsulation, exceptions, modules, and reusable patterns. |
| `Advance_Python/AI/` | `openai_testing.ipynb`, `langchain_with_gemeni.ipynb` | LLM experimentation with LangChain-style tooling. Inputs are prompts; outputs are model responses and integration examples. |
| `Advance_Python/module/` | `mymodule.py`, `test.py` | Demonstrates custom module creation and import-based reuse. |
| `Advance_Python/OOPs/` | `Introduction.ipynb` | Object-oriented programming introduction with visual examples. |
| `statistics/statistics_R/` | `Statistics.ipynb`, `Sampling_CLT.ipynb`, `sampling.ipynb`, `hypothesis.ipynb`, `Assignments.ipynb`, `assignment1.ipynb` | Statistics practice using Pandas, NumPy, SciPy, Seaborn, and Statsmodels. Datasets include `Order_Table.csv`, `df_marketing.csv`, revenue/churn files, and assignment data. Outputs include descriptive summaries, distributions, confidence intervals, and hypothesis test results. |
| `statistics/Statistics_S/` | `Statetics_Introduction.ipynb`, `Inference_Statestics.ipynb`, `stats.ipynb`, `app.py`, `practiceapp.py` | Statistics notes and Streamlit apps for descriptive/inferential statistics. Inputs are uploaded or notebook datasets; outputs are plots, summary statistics, and interactive dashboards. |
| `Python_libraries/Analysis_lib/` | `Array_Numpy.ipynb`, `Pandas.ipynb`, `matplotlib.ipynb`, `Seaborn.ipynb`, `Seaborn_campus.ipynb`, `ML_EDA.ipynb`, `imdb_movies.ipynb`, `poc1_ipl_data_analysis.ipynb` | Data analysis practice with NumPy, Pandas, Matplotlib, Seaborn, Plotly, Gradio, and EDA workflows. Datasets include `data.xlsx`, `tips.csv`, movie/rating/tag data, IPL data, and cleaned EDA data. |
| `Python_libraries/Analysis_lib/EDA_INTEGRATION_LLM/EDA_LLM Integration/` | `code.ipynb`, `app.py` | EDA automation using Pandas, Seaborn, Gradio, Ollama/Mistral-style LLM prompts, and Titanic data. Outputs include distribution charts, correlation heatmaps, and natural-language EDA summaries. |
| `Python_libraries/opencv/` | `opencv_plt.ipynb` | Intro OpenCV and Matplotlib image display using image assets such as `dog1.jpg` and `new_gen_ai_image.jpg`. |
| `Python_libraries/Projects/` | `seaborn_visualization.py`, `Plotly_india_data.py` | Streamlit visualization apps using Seaborn/Plotly and datasets such as `tips.csv` and `india.csv`. |
| `Task_Solutions/` | `python_interview_questions.ipynb`, `Numpy_Array.ipynb`, `matplotlib.ipynb`, `my_prac.ipynb` | Practice notebooks for interviews, NumPy arrays, Matplotlib/Seaborn/Gradio plotting, and exploratory tasks. Uses IPL and batting datasets where available. |
| `Task_Solutions/basic_python/` | `Task1_Solutions.ipynb`, `Task2_Solutions_list.ipynb`, `Task_Solution_Tuple.ipynb`, `Sets&dict.ipynb`, `conditional_statements.ipynb`, `function.ipynb`, `regularexpression.ipynb` | Python task solutions covering lists, tuples, sets, dictionaries, conditionals, functions, regex, and problem-solving patterns. |
| `Task_Solutions/pandas/` | `Pandas.ipynb`, `Pandas_Series.ipynb`, `groupbypandas.ipynb` | Pandas practice using IPL, movies, IMDb, Kohli, Bollywood, and batter datasets. Outputs include series operations, groupby summaries, and tabular analysis. |
| `Task_Solutions/plotly/` | `Plotly.ipynb`, `Plotlybasics.ipynb` | Plotly visualization practice with IPL deliveries and match data. Outputs include interactive HTML-style plots. |
| `Machine_learning/Data Preprocessing/` | `machinelearning-intro.ipynb`, `DataPreprocessing.ipynb`, `Titanic_Data_Preprocessing.ipynb`, `Column_Transformer.ipynb`, `Standardization.ipynb`, `Normalization.ipynb`, `OneHotEncoding.ipynb`, `Ordinal_Encoding.ipynb`, `simple_imputer.py`, `simple_imputer_spyder.py`, `DB.py`, `logistic_Regession.py`, `knn.py`, `svm.py`, `naive_bayes.py`, `decisiontree.py`, `RandomForest.py`, `k-means-clustering.py`, `K-MEANS-STREMLIT.py`, `hierarchical.py`, `hyper-parameter-tunning.py`, `boosting.py`, `customer.py`, `customer1.py`, `customer-review.py`, `embeding.py`, `nlg.py` | End-to-end preprocessing and first ML pipelines using Scikit-Learn. Datasets include Titanic, Social Network Ads, wine, cars, customer, Mall Customers, churn, and review data. Algorithms include Logistic Regression, KNN, SVM, Naive Bayes, Decision Tree, Random Forest, K-Means, hierarchical clustering, XGBoost/LightGBM, TF-IDF, Word2Vec, and review classifiers. Outputs include predictions, clustered customer files, pickled classifiers, and dashboards. |
| `Machine_learning/LinearRegression/` | `Simple_Linear_Regression.ipynb`, `multiple_linear_regression.ipynb`, `Polynomial Regression.ipynb`, `Regularization.ipynb`, `Elasticnet.ipynb`, `HouseRegression.ipynb`, `Avacado.ipynb`, `Multicolinarity.ipynb`, `Multicolinarity_code.ipynb`, `SVR_KNN_Regression.ipynb`, `assigment.ipynb`, `simple_linear_regression_spyder.py`, `simple_linear_model_app.py`, `regularization.py`, `svr_knn_syder.py` | Regression study track with Salary, House, electricity, placement, investment, avocado, car MPG, employee salary, and laptop datasets. Algorithms include Linear Regression, multiple/polynomial regression, Ridge/Lasso/ElasticNet-style regularization, SVR, KNN, Decision Tree, Random Forest, and Gradio/Streamlit inference. |
| `Machine_learning/LinearRegression/laptop_price_predictor/` | `Untitled.ipynb` | Laptop price analysis using `laptop_data.csv`, Pandas, Seaborn, Matplotlib, and regression-style preparation. |
| `Machine_learning/HyperparameterTunning/` | `Cross_Validation.ipynb`, `cross_validation_code.ipynb`, `Hyperparameter.ipynb`, `hyperparametercode.ipynb`, `hyperparmetertunning.ipynb` | Cross-validation and tuning demos using Boston Housing/KNN/logistic examples. Key learning: validate before trusting metrics. |
| `Machine_learning/Classification/` | `Classification.ipynb` | Conceptual classification notes and visual explanations. |
| `Machine_learning/Classification/Logistics_regression/` | `Logistic_Regression.ipynb`, `Softmax_logistic.ipynb`, `gredient_decent.ipynb`, `perceptron_lr.ipynb` | Logistic regression, softmax, gradient descent, and perceptron foundations. Datasets include Titanic and Boston-style examples. |
| `Machine_learning/Classification/SVM/` | `SVM.ipynb`, `SVM-kernel.ipynb`, `SVM_Demo.ipynb` | Support Vector Machine theory and SVC/SVR demos with kernels and decision boundaries. |
| `Machine_learning/Classification/knn/` | `KNN-Intution.ipynb` | KNN intuition, distance-based classification, and neighborhood decision logic. |
| `Machine_learning/Classification/Naive Bayes/` | `Naive_Bayes.ipynb`, `Probability.ipynb`, `naive_bayes_code.ipynb`, `RegressionTree.ipynb` | Probability, Naive Bayes, text examples with IMDB/PlayTennis, and tree comparison. |
| `Machine_learning/Classification/DecisionTree/` | `Decision_Tree.ipynb`, `Decisiontree_code.ipynb`, `DecisionTreeRegressor.ipynb`, `FullDecisionTree.ipynb`, `decision_tree_viewer.py` | Decision Tree classification/regression with Social Network Ads, Boston Housing, Streamlit visualization, and tree interpretation. |
| `Machine_learning/Classification/PCA/` | `PCA.ipynb`, `pca_code.ipynb`, `pca_vetors.ipynb`, `SVD.ipynb` | Dimensionality reduction using PCA and SVD with NumPy, Scikit-Learn, Plotly, and SciPy. Outputs include component plots and variance explanations. |
| `Machine_learning/Classification/CLUSTERING/` | `Algorithmic_clustering.ipynb` | Clustering with shopping/customer data, hierarchical clustering, SciPy linkage, and visualization. |
| `Machine_learning/Classification/classification_metrix/` | `Classification_Metrix.ipynb`, `classification_metrix_multilabel.ipynb`, `multilabel_model_evaluation.ipynb` | Model evaluation using confusion matrix, precision, recall, F1, multilabel metrics, and heart dataset examples. |
| `Machine_learning/Classification/Ensemble-Learning/Bagging/` | `bagging-learning.ipynb`, `bagging_demo.ipynb`, `bagging_regressor.ipynb` | Bagging classifier/regressor demos with Decision Tree, SVC, KNN, Linear Regression, and Boston Housing. |
| `Machine_learning/Classification/Ensemble-Learning/Random_Forest/` | `random_forest.ipynb`, `random_forest.py`, `random-forest-demo.ipynb`, `rf-learning-tool.ipynb`, `bagging-vs-random forest.ipynb` | Random Forest learning, comparison with bagging, Streamlit tool, and synthetic/classification datasets. |
| `Machine_learning/Classification/Ensemble-Learning/Voting/` | `Voting_Classifier.ipynb`, `Voting_Regressor.ipynb` | Voting ensembles combining Logistic Regression, SVC, KNN, Random Forest, Linear Regression, SVR, and Decision Tree. |
| `Machine_learning/Classification/Ensemble-Learning/Boosting/` | `Gradient-Boosting.ipynb`, `Gradient-Boosting-Classification.ipynb`, `Gradient-Boosting-classification-part2.ipynb` | Gradient boosting for regression/classification with staged learning and visual comparisons. |
| `Machine_learning/Classification/Ensemble-Learning/Boosting/XGboost/` | `data-extraction.ipynb` | XGBoost-related data extraction/config practice using YAML, Pandas, NumPy, and progress utilities. |
| `Machine_learning/` | `Daily_notes.ipynb` | Consolidated ML notes covering algorithms such as SVR, PCA, XGBoost, and bagging. |
| `Projects/` | `webscrapping.ipynb`, `adult_uci.ipynb`, `eda_logistic_PCA.ipynb` | Portfolio notebooks for scraping, Adult UCI analysis, EDA, logistic/PCA workflows. Outputs include scraped CSVs and model-ready analysis. |
| `Projects/Bitcoin_Regression/` | `bitcoin.ipynb`, `app.py` | Bitcoin price regression using yfinance, Pandas, Seaborn, Scikit-Learn, Random Forest, model/scaler pickle files, and Streamlit inference. |
| `MySql/` | `databasecreation.ipynb`, `restourant_sql_project.ipynb`, `sql_connector.py` | SQL database creation, restaurant data analysis, Python ODBC connectivity, and join practice using `sql_data/*.csv`. |
| `NLP/` | `NLP-INTRO.ipynb`, `Data-Extraction&Preproessing.ipynb`, `NLP_ALGORITHMS.ipynb`, `POS-TAGGING.ipynb`, `spacy.ipynb`, `text-reprentation!bow!tfidf.ipynb`, `word2vecintro.ipynb`, `word2vec.ipynb`, `w2v-ml-model.ipynb` | NLP fundamentals with NLTK, spaCy, TF-IDF, Word2Vec, Gensim, Scikit-Learn, and IMDB sentiment data. Outputs include vector representations, models, and visualizations. |
| `NLP/NLP_Projects/` | `chatbot.py`, `nlu.py` | NLP utility apps for chatbot logic, language detection, translation, and speech/text workflows. |
| `MLOPS/` | `1st code experiment.ipynb`, `2nd_mlflow_binaryclassification.ipynb`, `3rd_ mlflow_model_registiration.ipynb`, `mllop code-1.py`, `mlops using oops.py` | MLflow experiments using Logistic Regression, Random Forest, XGBoost, imbalanced learning, artifacts, metrics, confusion matrices, and model registry practice. |
| `DEEPLEARNING/` | `deeplearning-intro.ipynb`, `cnn_into.ipynb`, `pretrained_model.ipynb`, `pretrained_model_transformers.ipynb`, `rain_prediction.ipynb` | Deep learning overview, CNN intro, pretrained image models, transformer-style pretrained models, and weather/rain prediction with LSTM-style workflows. |
| `DEEPLEARNING/deep_learning/` | `perceptron_demo.ipynb`, `gradient_decent.ipynb`, `feature_scaling_ann.ipynb`, `backpropagation_classification.ipynb`, `backpropagation_regression.ipynb`, `backpropogation_regression.ipynb`, `batch_normalization.ipynb`, `Dropout_ANN.ipynb`, `Early_stoping_ann.ipynb`, `regularization_ann.ipynb`, `vanishing_gradient.ipynb`, `vanishing_problem_ann.ipynb`, `weights_intialization_techniques.ipynb`, `Weights_Initialization(Xavier_Glorat).ipynb`, `CNN_Padding.ipynb`, `CNN_Polling.ipynb`, `CNN_Visualization.ipynb`, `cnn.ipynb`, `Simple_RNN.ipynb`, `Transfer_Learning.ipynb`, `pretrained_model.ipynb` | TensorFlow/Keras notebooks covering ANN behavior, initialization, regularization, CNN operations, RNNs, transfer learning, and image prediction. |
| `DEEPLEARNING/deep_learning/back_prapogation/` | `classification.ipynb`, `backpropagation_regression.ipynb` | Manual/backpropagation learning for classification and regression. |
| `DEEPLEARNING/deep_learning/projects/` | `mnist-classification.ipynb`, `graduate-admision.ipynb`, `churn_prediction.ipynb` | Deep learning projects for MNIST, graduate admission prediction, and churn classification. |
| `DEEPLEARNING/pytorch/` | `tensor_in_pytorch.ipynb`, `autograd.ipynb`, `pytorch-NN-module.ipynb`, `dataset & dataloader.ipynb`, `training_pipeline.ipynb`, `training_pipeline_using_dataset_and_dataloader.ipynb`, `ann-fasion-emnist-pytorch.ipynb`, `ann_fasion_emnist_pytorch_gpu.ipynb`, `CNN_Fashion_EMnists_gpu.ipynb`, `cnn.ipynb`, `cnn_optuna.ipynb`, `fanshion_optimized.ipynb`, `fashion_emnist_hyper_optuna.ipynb`, `Rnn_pytorch.ipynb`, `pytorch_lstm_next_word_predictor.ipynb`, `pretrained_model.ipynb`, `transferlearning_fashion_emnist.ipynb` | PyTorch foundations, training loops, Fashion-MNIST, CNNs, RNN/LSTM, Optuna tuning, and transfer learning. |
| `DEEPLEARNING/open-cv/` | `14hoursopencv.ipynb`, `open-cv.ipynb`, `ocr.ipynb`, `pytessarct.ipynb`, `MEDIAPIPE.ipynb`, `cardetection.ipynb`, `Road Lane line.py` | Computer vision with OpenCV, OCR/Tesseract, MediaPipe, car/road detection, and image processing. |
| `DEEPLEARNING/open-cv/COLOR DETECTION PROJECT/` | `color_detection.py`, `app.py` | Color detection project using OpenCV, Pandas, Streamlit, `colors.csv`, image uploads, and coordinate-based interaction. |
| `DEEPLEARNING/open_med/MEDIAPIPE-LIBRARY-main/` | `3D Object Detection (3D Bounding Boxes) with MediaPipe Objectron.py`, `3D Object Detection from Video.py`, `Face and Hand Landmarks Detection using Python – Mediapipe, OpenCV.py`, `Hand landmarks detection using MediaPipe.py`, `Instant Motion Tracking with MediaPipe.py`, `MediaPipe 3D Face Transform Code 1.py`, `MediaPipe 3D Face Transform Code 2.py`, `MediaPipe 3D Face Transform Code 3.py`, `MediaPipe 3D Face Transform Code 4.py`, `Object Detection with Web Cam using MediaPipe.py`, `On-device, Real-time Body Pose Tracking with MediaPipe BlazePose.py`, `Pose landmark detection using MediaPipe.py`, `Real-time Body Pose Tracking with input video.py` | MediaPipe examples for body pose, hand landmarks, face mesh, webcam object detection, and Objectron. Inputs are images/video/webcam; outputs are annotated frames and landmarks. |
| `DEEPLEARNING/churn_modeling/` | `churn.ipynb`, `app.py` | Churn modeling with TensorFlow/Keras, Scikit-Learn, Pandas, Streamlit, and `Churn_Modelling.csv`. Outputs include predictions and `churn_predictions.csv`. |
| `DEEPLEARNING/RNN/` | `bert.py` | Streamlit/PyTorch/Transformers BERT-style sequence modeling demo. |
| `DEEPLEARNING/yolo/` | `yolo_intro.py` | YOLO object detection script using image inputs and model weights. |
| `UI/Backend/` | `app.py`, `flask_ui.py` | Backend/UI demos using Flask and HTML-safe rendering. |
| `UI/frontend/` | `app1.py`, `information.py`, `my_gui_tk.py` | Streamlit and Tkinter frontend practice. |
| `UI/frontend/student_result/` | `app.py` | Student Result Management System using Tkinter, hashing/bcrypt, CSV/database-style storage, charts, and report-style outputs. |

</details>

## 🧰 Technologies Used

| Category | Technologies |
| --- | --- |
| Language | Python, SQL |
| Notebook Environment | Jupyter Notebook |
| Data Analysis | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn, Plotly, WordCloud |
| Machine Learning | Scikit-Learn, XGBoost, LightGBM, imbalanced-learn |
| Deep Learning | TensorFlow, Keras, PyTorch, Torchvision |
| NLP | NLTK, spaCy, Gensim, TF-IDF, Word2Vec, Transformers |
| Computer Vision | OpenCV, MediaPipe, YOLO, Tesseract OCR |
| MLOps | MLflow, model artifacts, model registry practice |
| Apps/UI | Streamlit, Flask, Tkinter, Gradio |
| Databases | MySQL-style SQL, SQLite, SQL Server/ODBC examples |
| Utilities | yfinance, Selenium, BeautifulSoup, Pillow, Optuna |

## 🛣️ Data Science Roadmap Covered

| Stage | What You Learn |
| --- | --- |
| Python Programming | Syntax, data types, functions, loops, conditionals, OOP, modules, exceptions, and beginner applications. |
| Statistics | Descriptive statistics, probability, sampling, CLT, confidence intervals, inference, and hypothesis testing. |
| NumPy | Arrays, vectorized operations, numerical computation, image-array basics, and mathematical manipulation. |
| Pandas | Series/DataFrame operations, joins, groupby, cleaning, feature creation, and dataset exploration. |
| Data Cleaning | Missing values, imputation, scaling, normalization, encoding, column transformers, and Titanic-style preprocessing. |
| Data Visualization | Static and interactive plotting using Matplotlib, Seaborn, Plotly, and Streamlit dashboards. |
| Exploratory Data Analysis | Movie, IPL, Titanic, IMDB, and custom EDA workflows including LLM-assisted EDA. |
| Machine Learning | Regression, classification, clustering, dimensionality reduction, ensembles, tuning, and evaluation. |
| Deep Learning | ANN, CNN, RNN, LSTM, transfer learning, pretrained models, TensorFlow, Keras, and PyTorch. |
| Model Evaluation | Confusion matrix, classification metrics, cross-validation, hyperparameter tuning, and MLflow tracking. |
| Real-world Projects | Bitcoin regression, churn prediction, NLP tools, web scraping, color detection, SQL analysis, and UI apps. |

## 📚 Recommended Learning Path

1. Start with `Python_Basics/` to build syntax and programming confidence.
2. Move to `Task_Solutions/basic_python/` for practice and interview-style problems.
3. Study `Advance_Python/` for OOP, modules, exceptions, and reusable code.
4. Learn statistics through `statistics/statistics_R/` and `statistics/Statistics_S/`.
5. Practice NumPy, Pandas, Matplotlib, Seaborn, and Plotly in `Python_libraries/` and `Task_Solutions/`.
6. Learn preprocessing in `Machine_learning/Data Preprocessing/`.
7. Study regression in `Machine_learning/LinearRegression/`.
8. Study classification, metrics, clustering, PCA, SVM, Naive Bayes, and Decision Trees in `Machine_learning/Classification/`.
9. Add ensembles and tuning through `Ensemble-Learning/` and `HyperparameterTunning/`.
10. Build deeper models with `DEEPLEARNING/deep_learning/` and `DEEPLEARNING/pytorch/`.
11. Explore NLP with `NLP/` and computer vision with `DEEPLEARNING/open-cv/`.
12. Finish with `Projects/`, `MLOPS/`, and `UI/` to convert learning into portfolio-ready applications.

## 🚀 Projects Section

| Project | Problem Statement | Dataset | Approach / Algorithms | Results / Outputs | Business Impact |
| --- | --- | --- | --- | --- | --- |
| Bitcoin Regression | Predict or analyze Bitcoin price behavior | yfinance data plus saved model/scaler assets | EDA, feature engineering, Random Forest, regression comparisons | `random_forest_model.pkl`, `scaler.pkl`, Streamlit app | Demonstrates financial forecasting workflow and deployable inference. |
| Churn Modeling | Predict customer churn | `Churn_Modelling.csv` | Encoding, scaling, ANN/TensorFlow, Streamlit prediction app | Churn predictions and app interface | Helps businesses identify customers at risk of leaving. |
| Adult UCI / Logistic PCA | Analyze adult income-style data and dimensionality | UCI/Kaggle adult datasets | EDA, logistic modeling, PCA | Model-ready notebook outputs | Shows demographic/economic analysis workflow. |
| Web Scraping | Collect structured web data | Quotes/IPL-style scraped sources | Requests, Selenium, BeautifulSoup, Pandas | CSV outputs such as quotes/IPL match data | Automates data collection for analytics projects. |
| EDA with LLM Integration | Generate assisted EDA summaries | Titanic and custom CSV data | Pandas, Seaborn, Gradio, Ollama/Mistral-style LLM prompts | Charts, heatmaps, natural-language summaries | Speeds up initial data understanding and reporting. |
| Color Detection Project | Detect colors from images | `colors.csv`, uploaded images | OpenCV, Pandas, Streamlit, coordinate selection | Interactive color names/RGB values | Useful for design, image analytics, and CV demos. |
| Student Result Management System | Manage student results and reports | Local database/CSV-style storage | Tkinter, hashing, charts, report workflow | Admin/student UI, graphs, generated records | Demonstrates full desktop-style educational management software. |
| Text-to-Speech App | Convert text input to speech | User text | Tkinter, pyttsx3, NLTK | Spoken output and GUI | Accessibility and voice-interface practice. |
| SQL Restaurant Project | Analyze relational data | `sql_data/*.csv` | SQL joins, table creation, Pandas integration | Query outputs and joined tables | Demonstrates database analysis skills. |
| MLOps MLflow Experiments | Track experiments and register models | Iris/classification-style data | MLflow, Logistic Regression, Random Forest, XGBoost | Metrics, confusion matrices, artifacts, registered model metadata | Shows reproducible ML lifecycle thinking. |

## 🧠 Skills Demonstrated

| Skill | Level Demonstrated |
| --- | --- |
| Python | Advanced |
| NumPy | Intermediate |
| Pandas | Advanced |
| Statistics | Intermediate |
| Data Visualization | Advanced |
| SQL | Intermediate |
| Machine Learning | Advanced |
| Model Evaluation | Advanced |
| Deep Learning | Intermediate to Advanced |
| NLP | Intermediate |
| Computer Vision | Intermediate |
| MLOps / MLflow | Intermediate |
| Streamlit/Flask/Tkinter Apps | Intermediate |

## ⚙️ Installation Guide

Clone the repository:

```bash
git clone https://github.com/Ram2002-ai/DataScience_NareshIt.git
cd DataScience_NareshIt
```

Create and activate a virtual environment:

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

Install the base requirements:

```bash
pip install -r requirements.txt
```

Install common notebook dependencies used across the repository:

```bash
pip install jupyter notebook numpy pandas matplotlib seaborn plotly scikit-learn scipy statsmodels
pip install streamlit flask gradio opencv-python pillow
pip install tensorflow torch torchvision nltk spacy gensim mlflow optuna xgboost lightgbm
```

Start Jupyter Notebook:

```bash
jupyter notebook
```

Run selected apps:

```bash
streamlit run Projects/Bitcoin_Regression/app.py
streamlit run DEEPLEARNING/open-cv/"COLOR DETECTION PROJECT"/app.py
python UI/Backend/flask_ui.py
python Python_Basics/PROJECTS/dice_simulator/dice.py
```

> The root `requirements.txt` is minimal and focused on Streamlit/OpenCV-style apps. Some advanced notebooks require extra packages listed above or noted inside each notebook.

## 🧑‍💻 How to Use This Repository

### For Beginners

Start with Python basics, then solve the task notebooks before moving into NumPy and Pandas. Run every cell, change the sample inputs, and rewrite small functions from memory. This builds confidence before heavier machine learning content.

### For Intermediate Learners

Use the repository as a hands-on revision map. Pick a topic such as regularization, PCA, SVM, Word2Vec, or CNNs, open the corresponding folder, and compare conceptual notebooks with code notebooks. Re-run experiments with different datasets or parameters.

### For Job Seekers

Use this as interview and portfolio preparation. Prioritize the folders that demonstrate end-to-end thinking: `Projects/`, `Machine_learning/`, `DEEPLEARNING/`, `NLP/`, `MLOPS/`, and `UI/`. Prepare explanations for preprocessing choices, model evaluation, business impact, and deployment decisions.

## 🤝 Contribution Guidelines

Contributions are welcome. Suggested workflow:

1. Fork the repository from GitHub.
2. Clone your fork locally.
3. Create a feature branch and commit your work.

```bash
git clone https://github.com/<your-username>/DataScience_NareshIt.git
cd DataScience_NareshIt
git checkout -b feature/your-improvement
git add .
git commit -m "Add your improvement"
git push origin feature/your-improvement
```

Then open a pull request with:

- A short description of the change.
- The folder or notebook updated.
- Any dataset or dependency requirements.
- Screenshots for UI/visualization changes where useful.

Recommended contribution areas:

- Add missing dataset descriptions to notebooks.
- Add cleaner environment files for each major module.
- Convert repeated notebook experiments into reusable Python modules.
- Add evaluation reports and model cards for project notebooks.
- Add tests for Python scripts and app utilities.

## 🔮 Future Improvements

- Add a unified `requirements-dev.txt` or `environment.yml`.
- Add module-specific README files for ML, DL, NLP, SQL, and MLOps.
- Add more real-world projects with business problem statements and measurable results.
- Add NLP projects using transformers, RAG, and generative AI.
- Add MLOps deployment flows with Docker, CI/CD, model serving, and monitoring.
- Add Streamlit dashboards for more ML projects.
- Add Dockerfiles for apps and reproducible notebook environments.
- Add dataset cards and model cards for portfolio-grade documentation.
- Add unit tests for scripts and reusable utilities.
- Add a license file for open-source clarity.

## 📄 License

No license file is currently detected in this repository. Add a license such as MIT, Apache-2.0, or BSD-3-Clause if the project is intended for open-source reuse.

## 🙌 Final Note

This repository is a broad, hands-on Data Science learning archive. It is strongest as a portfolio of continuous practice: fundamentals, statistics, data analysis, machine learning, deep learning, NLP, computer vision, MLOps, SQL, and Python application building all live in one place.
