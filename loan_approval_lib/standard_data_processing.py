import pandas

from sklearn.preprocessing import OneHotEncoder


def data_cleaning_algorithm(data):
    columns = [
        'person_age',
        'person_income',
        'person_emp_length',
        'loan_amnt',
        'loan_int_rate',
        'loan_percent_income',
        'cb_person_default_on_file'
    ]
    
    for column in columns:
        row_count_1 = len(data)
    
        if column == 'person_age':
            data = data[data['person_age'] <= 100]
    
        if column == 'person_emp_length':
            data = data[data['person_emp_length'] <= 100]
    
        data = data[data[column].isna() == False]
        
        row_count_2 = len(data)
        row_count_diff = row_count_1 - row_count_2
        print(f'column {column}, number of removed rows: {row_count_diff}')

    return data


def create_loan_grade_numerical_from_loan_grade(data, data_train, data_test):
    loan_grades = list(sorted(data['loan_grade'].unique()))
    
    for loan_grade in loan_grades:
        data.loc[data['loan_grade'] == loan_grade, 'loan_grade_numerical'] = ord(loan_grade) - ord('A')
    
        data_train.loc[data_train['loan_grade'] == loan_grade, 'loan_grade_numerical'] = ord(loan_grade) - ord('A')
        
        data_test.loc[data_test['loan_grade'] == loan_grade, 'loan_grade_numerical'] = ord(loan_grade) - ord('A')


def create_person_home_ownership_one_hot_encoder(data):
    encoder = OneHotEncoder(sparse_output=False)
    encoder.fit(data[['person_home_ownership']])
    return encoder

def create_person_home_ownership_one_hot(encoder, data):
    transformed = encoder.transform(data[['person_home_ownership']])
    
    data = pandas.concat(
        [
            data,
            pandas.DataFrame(
                transformed,
                index=data.index,
                columns=encoder.get_feature_names_out(['person_home_ownership']),
            ),
        ],
        axis=1,
    )
    return data


def create_loan_intent_one_hot_encoder(data):
    encoder = OneHotEncoder(sparse_output=False)
    encoder.fit(data[['loan_intent']])
    return encoder

def create_loan_intent_one_hot(encoder, data):
    transformed = encoder.transform(data[['loan_intent']])
    
    data = pandas.concat(
        [
            data,
            pandas.DataFrame(
                transformed,
                index=data.index,
                #columns = [f'person_home_ownership_{category}' for category in encoder.categories_],
                columns=encoder.get_feature_names_out(['loan_intent']),
            ),
        ],
        axis=1,
    )
    return data


def map_cb_person_default_on_file(data):
    data['cb_person_default_on_file'] = data['cb_person_default_on_file'].map(lambda x: 1 if x == 'Y' else 0)
    return data


def create_decision_tree_columns():
    decision_tree_columns = [
        'person_age',
        'person_income',
        'person_emp_length',
        'loan_amnt',
        'loan_int_rate',
        'loan_percent_income',
        'cb_person_cred_hist_length',
        'loan_grade_numerical',
        'person_home_ownership_MORTGAGE',
        'person_home_ownership_OTHER',
        'person_home_ownership_OWN',
        'person_home_ownership_RENT',
        'loan_intent_DEBTCONSOLIDATION',
        'loan_intent_EDUCATION',
        'loan_intent_HOMEIMPROVEMENT',
        'loan_intent_MEDICAL',
        'loan_intent_PERSONAL',
        'loan_intent_VENTURE',
        'cb_person_default_on_file',
    ]
    return decision_tree_columns


def create_decision_tree_columns_with_id():
    decision_tree_columns = create_decision_tree_columns()
    
    decision_tree_columns_with_id = [
        column for column in decision_tree_columns
    ]
    decision_tree_columns_with_id.append('id')
    
    return decision_tree_columns_with_id


def create_dataframe_copy_and_drop_columns(data):
    data_copy = data.copy()

    data_copy.drop(
        columns=[
            'person_home_ownership',
            'loan_intent',
            'loan_grade',
        ],
        inplace=True,
    )
    
    return data_copy
