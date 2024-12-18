// fetch data from server
document.getElementById("predict-form").addEventListener("submit", function(e){
    e.preventDefault();

    const formData = new FormData(this);


    fetch('/', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json()) 
    .then(data => {
       
        if (data.prediction) {
            document.getElementById('prediction-result').innerHTML = `Predicted Price: ${data.prediction}`;
        } else if (data.error) {
            document.getElementById('prediction-result').innerHTML = `Error: ${data.error}`;
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('prediction-result').innerHTML = 'An error occurred.';
    });
    
})