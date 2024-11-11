from sklearn.base import BaseEstimator, TransformerMixin


class AgeGroupAdder(BaseEstimator, TransformerMixin):
    """
    This class adds an 'age_group' column to the input DataFrame based on the 'age' column.
    """
    def __init__(self):
        # Define regular methods for age group conditions
        self.age_groups = {
            'below_15': self.below_15,
            'between_16_30': self.between_16_30,
            'between_31_45': self.between_31_45,
            'between_46_60': self.between_46_60,
        }

    def fit(self, X, y=None):
        return self

    def transform(self, X): 
        if 'age' not in X.columns:
            raise ValueError("The input dataframe must contain age column")
        X = X.copy()
        X["age_group"] = X["age"].apply(self.get_age_groups)
        return X

    def get_age_groups(self, age):
        for group, condition in self.age_groups.items():
            if condition(age):
                return group
        return 'unknown'  # Default value if no condition matches

    # Individual methods to check age conditions
    def below_15(self, age):
        return age <= 15

    def between_16_30(self, age):
        return 16 <= age <= 30

    def between_31_45(self, age):
        return 31 <= age <= 45

    def between_46_60(self, age):
        return 46 <= age <= 60
    


# column dropper
class ColumnDropper(BaseEstimator, TransformerMixin):
    """
    This class drops specified columns from the input DataFrame.
    """
    def __init__(self, columns_to_drop):
        self.columns_to_drop = columns_to_drop

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        missing_cols = [col for col in self.columns_to_drop if col not in X.columns]
        if missing_cols:
            raise ValueError(f"The following columns are missing in the DataFrame: {missing_cols}")
        return X.drop(columns=self.columns_to_drop)


# A custom transformer that add median price column in the data
class MedianPriceAdder(BaseEstimator, TransformerMixin):
    def __init__(self, group_cols, target_col):
        self.group_cols = group_cols
        self.target_col = target_col
        self.median_map = None
    
    def fit(self, X, y=None):
        # Compute median price for each group
        self.median_map = X.groupby(self.group_cols).agg(median_price=(self.target_col, 'median')).astype(int)
        self.median_map = self.median_map.reset_index()
        
        # Create a dictionary mapping (grouped columns) to median values
        self.median_dict = self.median_map.set_index(self.group_cols)['median_price'].to_dict()
        
        return self
    
    def transform(self, X):
        # Create a new column 'median_price' by mapping based on group columns
        X['median_price'] = X.apply(
            lambda row: self.median_dict.get(tuple(row[self.group_cols]), None),
            axis=1
        )
        return X