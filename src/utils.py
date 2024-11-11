import pandas as pd

def prepare_input_data(form_data):
    """
    This function will be used to prepare the input data for the model.
    """

    data = {
        'area': int(form_data.get('area')),
        'locality': form_data.get('locality'),
        'city': form_data.get('city'),
        'property_type': form_data.get('property_type'),
        'bedroom_num': int(form_data.get('bedroom_num')),
        'bathroom_num': int(form_data.get('bathroom_num')),
        'balcony_num': int(form_data.get('balcony_num')),
        'furnished': form_data.get('furnished'),
        'age': int(form_data.get('age')),
        'total_floors': form_data.get('total_floors')
    }

    return pd.DataFrame([data])