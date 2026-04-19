import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from xgboost import XGBClassifier

# Assume X (cleaned reviews) and y (labels) are already prepared
# X_train, X_test, y_train, y_test from train_test_split

models = {
    'LogisticRegression': {
        'model': LogisticRegression(max_iter=1000, random_state=42),
        'params': {'clf__C': [0.1, 1.0, 10.0]}
    },
    'DecisionTree': {
        'model': DecisionTreeClassifier(random_state=42),
        'params': {'clf__max_depth': [10, 20, None]}
    },
    'RandomForest': {
        'model': RandomForestClassifier(random_state=42),
        'params': {'clf__n_estimators': [100, 200], 'clf__max_depth': [10, 20]}
    },
    'MultinomialNB': {
        'model': MultinomialNB(),
        'params': {'clf__alpha': [0.1, 0.5, 1.0]}
    },
    'SVM': {
        'model': SVC(random_state=42),
        'params': {'clf__C': [0.1, 1, 10], 'clf__kernel': ['linear', 'rbf']}
    },
    'XGBoost': {
        'model': XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42),
        'params': {'clf__n_estimators': [100, 200], 'clf__max_depth': [3, 5]}
    }
}

tfidf = TfidfVectorizer(max_features=5000, ngram_range=(1,2))
results = []

for name, mp in models.items():
    pipeline = Pipeline([('tfidf', tfidf), ('clf', mp['model'])])
    grid = GridSearchCV(pipeline, mp['params'], cv=5, scoring='accuracy', n_jobs=-1)
    grid.fit(X_train, y_train)
    
    best_model = grid.best_estimator_
    train_acc = accuracy_score(y_train, best_model.predict(X_train))
    test_acc = accuracy_score(y_test, best_model.predict(X_test))
    
    results.append({
        'Model': name,
        'Best Params': str(grid.best_params_),
        'CV Mean Accuracy': grid.best_score_,
        'Train Accuracy (bias)': train_acc,
        'Test Accuracy (variance)': test_acc,
        'Train-Test Gap': train_acc - test_acc
    })

df_results = pd.DataFrame(results)
print(df_results)