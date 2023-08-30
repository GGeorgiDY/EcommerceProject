const searchInput = document.getElementById('search-input');
const searchPredictions = document.getElementById('search-predictions');

searchInput.addEventListener('input', () => {
    const query = searchInput.value;

    if (query.trim() !== '') {
        fetch(`/cart/search-predictions/?query=${query}`)
            .then(response => response.json())
            .then(predictions => {
                // Clear previous predictions
                searchPredictions.innerHTML = '';

                // Display new predictions
                predictions.forEach(prediction => {
                    const predictionElement = document.createElement('div');
                    predictionElement.classList.add('productSuggest');
                    predictionElement.classList.add('search-suggest-item');
                    predictionElement.textContent = prediction[0];
                    predictionElement.addEventListener('click', () => {
                        fetch(`/product-detail/${prediction[1]}`)
                            .then( (res) => {
                                if (res.status === 500 || res.status === 404) {
                                    throw new Error('Bad Request')
                                } else if (res.status === 200) {
                                    window.location.href = res.url
                                }
                            })
                            .catch(error => {
                                console.error(error)
                                // да си добавя ново error view - page not found
                            })
                    })
                    searchPredictions.appendChild(predictionElement);
                });
            });
    } else {
        // Clear predictions when input is empty
        searchPredictions.innerHTML = '';
    }
});
