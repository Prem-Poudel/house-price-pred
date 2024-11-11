from flask import Flask, render_template, request, jsonify


from src.loader import unique_values_load, pipeline_load
from src.custom_transformer import ColumnDropper, AgeGroupAdder, MedianPriceAdder
from src.utils import prepare_input_data

app = Flask(__name__)

unique_cities, unique_localities, unique_property_types, unique_furnished = unique_values_load()
pipeline, median_adder = pipeline_load()

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    error_message = None

    if request.method == 'POST':
        try:
            input_df = prepare_input_data(request.form)

            # Apply median encoding
            input_df = median_adder.transform(input_df)

            # remove some cols
            input_df = input_df.drop(columns=["locality"], axis=0)

            # make prediction
            prediction = pipeline.predict(input_df).astype(int)[0]
        except Exception as e:
            error_message = str(e)
        
        if prediction is not None:
            return jsonify({'prediction': str(prediction)})
        elif error_message:
            return jsonify({'error': error_message})

    return render_template('index.html', unique_cities=unique_cities, unique_localities=unique_localities, property_types=unique_property_types, furnished=unique_furnished)


   
    



if __name__ == '__main__':
    app.run(debug=True)