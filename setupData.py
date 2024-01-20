from ucimlrepo import fetch_ucirepo 
import pandas as pd




def clean(dataset):
  X = dataset.features
  Y = dataset.targets
  missing_rows_features = X.isnull().any(axis=1)
  missing_rows_targets = Y.isnull().any(axis=1)
  missing_rows = missing_rows_features | missing_rows_targets
  
  print(f"features_missing: {missing_rows_features.sum()}")
  print(f"targets_missing: {missing_rows_targets.sum()}")

  X_clean = X[-missing_rows]
  Y_clean = Y[-missing_rows]

  # if (missing_rows.sum()) > 0: 
  #     print(X[missing_rows])
  #     print(Y[missing_rows])

  print(f'{missing_rows.sum()} rows deleted')
  dataset.features = X_clean
  dataset.targets = Y_clean

  return dataset

def grouped_target_stats(dataset):
    # grouped by the target
    X = dataset.features
    Y = dataset.targets

    XY = pd.concat([X,Y], axis=1)
    XY_grouped = XY.groupby(Y.columns[0])
    XY_mean = XY_grouped.mean()
    print(XY_mean)



  



def main():
  print("Hello world")
  # # DATASET 1: NHANES age prediction.csv
  national_health_and_nutrition_health_survey_2013_2014_nhanes_age_prediction_subset = fetch_ucirepo(id=887) 
  dataset_1 = national_health_and_nutrition_health_survey_2013_2014_nhanes_age_prediction_subset.data
  dataset_1 = clean(dataset_1)
  X_1 = dataset_1.features 
  y_1 = dataset_1.targets 

  # # DATASET 2: Breast Cancer Wisconsin
  breast_cancer_wisconsin_original = fetch_ucirepo(id=15) 
  dataset_2 = breast_cancer_wisconsin_original.data
  dataset_2 = clean(dataset_2)

  grouped_target_stats(dataset_1)
  grouped_target_stats(dataset_2)



  


if __name__ == "__main__":
  main()




  

